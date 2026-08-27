#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

class CalculadoraEdad:
    """Clase para calcular la edad de una persona"""
    
    def __init__(self):
        self.fecha_hoy = datetime.now()
    
    @staticmethod
    def es_valida_fecha(dia, mes, anio):
        """Valida si una fecha es correcta"""
        try:
            datetime(anio, mes, dia)
            return True
        except ValueError:
            return False
    
    def calcular_edad(self, dia_nac, mes_nac, anio_nac):
        """Calcula la edad en años, meses y días"""
        
        # Validar la fecha de nacimiento
        if not self.es_valida_fecha(dia_nac, mes_nac, anio_nac):
            return None, "Fecha inválida"
        
        fecha_nacimiento = datetime(anio_nac, mes_nac, dia_nac)
        
        # Verificar que no sea fecha futura
        if fecha_nacimiento > self.fecha_hoy:
            return None, "La fecha de nacimiento no puede ser en el futuro"
        
        # Calcular años
        anos = self.fecha_hoy.year - fecha_nacimiento.year
        
        # Calcular meses y días
        if (self.fecha_hoy.month, self.fecha_hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            anos -= 1
        
        # Calcular mes exacto
        mes_actual = self.fecha_hoy.month
        mes_nac_temp = fecha_nacimiento.month
        
        if mes_actual >= mes_nac_temp:
            meses = mes_actual - mes_nac_temp
        else:
            meses = 12 + mes_actual - mes_nac_temp
        
        # Calcular día exacto
        if self.fecha_hoy.day >= fecha_nacimiento.day:
            dias = self.fecha_hoy.day - fecha_nacimiento.day
        else:
            # Restar un mes
            meses -= 1
            if meses < 0:
                meses = 11
            
            # Obtener el número de días del mes anterior
            mes_anterior = self.fecha_hoy.month - 1
            if mes_anterior == 0:
                mes_anterior = 12
            
            if mes_anterior in [1, 3, 5, 7, 8, 10, 12]:
                dias_mes_anterior = 31
            elif mes_anterior in [4, 6, 9, 11]:
                dias_mes_anterior = 30
            else:  # Febrero
                if self.es_bisiesto(self.fecha_hoy.year):
                    dias_mes_anterior = 29
                else:
                    dias_mes_anterior = 28
            
            dias = dias_mes_anterior + self.fecha_hoy.day - fecha_nacimiento.day
        
        return (anos, meses, dias), None
    
    @staticmethod
    def es_bisiesto(anio):
        """Verifica si un año es bisiesto"""
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    def mostrar_edad(self, anos, meses, dias):
        """Muestra la edad de forma formateada"""
        print("\n╔═══════════════╗")
        print("║   RESULTADO   ║")
        print("╚═══════════════╝")
        print(f"Tu edad es: {anos} años, {meses} meses y {dias} días\n")


def main():
    """Función principal"""
    print("╔═══════════════════════════════════════╗")
    print("║  CALCULADORA DE EDAD - Versión Python ║")
    print("╚═══════════════════════════════════════╝\n")
    
    calculadora = CalculadoraEdad()
    
    try:
        print("Ingresa tu fecha de nacimiento:\n")
        dia = int(input("Día (1-31): "))
        mes = int(input("Mes (1-12): "))
        anio = int(input("Año (ej: 2000): "))
        
        edad, error = calculadora.calcular_edad(dia, mes, anio)
        
        if error:
            print(f"\n❌ Error: {error}")
        else:
            anos, meses, dias = edad
            calculadora.mostrar_edad(anos, meses, dias)
    
    except ValueError:
        print("\n❌ Error: Por favor, ingresa números válidos.")
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")


if __name__ == "__main__":
    main()
