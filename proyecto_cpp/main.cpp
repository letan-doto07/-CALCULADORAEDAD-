#include <iostream>
#include <ctime>
#include <iomanip>

using namespace std;

// Estructura para almacenar la fecha
struct Fecha {
    int dia;
    int mes;
    int anio;
};

// Función para validar si una fecha es válida
bool esValidaFecha(int dia, int mes, int anio) {
    if (anio < 1900 || anio > 2100) return false;
    if (mes < 1 || mes > 12) return false;
    
    int diasPorMes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    // Verificar año bisiesto
    if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0)) {
        diasPorMes[1] = 29;
    }
    
    if (dia < 1 || dia > diasPorMes[mes - 1]) return false;
    return true;
}

// Función para calcular la edad
void calcularEdad(Fecha nacimiento, Fecha hoy) {
    int anos = hoy.anio - nacimiento.anio;
    int meses = hoy.mes - nacimiento.mes;
    int dias = hoy.dia - nacimiento.dia;
    
    // Ajustar si los días son negativos
    if (dias < 0) {
        meses--;
        // Obtener días del mes anterior
        int diasPorMes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((hoy.anio % 4 == 0 && hoy.anio % 100 != 0) || (hoy.anio % 400 == 0)) {
            diasPorMes[1] = 29;
        }
        dias += diasPorMes[hoy.mes - 2];
    }
    
    // Ajustar si los meses son negativos
    if (meses < 0) {
        anos--;
        meses += 12;
    }
    
    cout << "\n=== RESULTADO ===" << endl;
    cout << "Tu edad es: " << anos << " años, " << meses << " meses y " << dias << " días" << endl;
    cout << "================\n" << endl;
}

int main() {
    Fecha nacimiento, hoy;
    
    cout << "╔═══════════════════════════════════════╗" << endl;
    cout << "║   CALCULADORA DE EDAD - Versión C++   ║" << endl;
    cout << "╚═══════════════════════════════════════╝\n" << endl;
    
    // Obtener la fecha actual
    time_t t = time(0);
    struct tm* ahora = localtime(&t);
    hoy.dia = ahora->tm_mday;
    hoy.mes = ahora->tm_mon + 1;
    hoy.anio = ahora->tm_year + 1900;
    
    // Solicitar fecha de nacimiento
    cout << "Ingresa tu fecha de nacimiento:\n" << endl;
    
    cout << "Día (1-31): ";
    cin >> nacimiento.dia;
    
    cout << "Mes (1-12): ";
    cin >> nacimiento.mes;
    
    cout << "Año (ej: 2000): ";
    cin >> nacimiento.anio;
    
    // Validar fecha
    if (!esValidaFecha(nacimiento.dia, nacimiento.mes, nacimiento.anio)) {
        cout << "\n❌ Fecha inválida. Por favor, intenta nuevamente." << endl;
        return 1;
    }
    
    // Verificar que la fecha no sea futura
    if (nacimiento.anio > hoy.anio || 
        (nacimiento.anio == hoy.anio && nacimiento.mes > hoy.mes) ||
        (nacimiento.anio == hoy.anio && nacimiento.mes == hoy.mes && nacimiento.dia > hoy.dia)) {
        cout << "\n❌ La fecha de nacimiento no puede ser en el futuro." << endl;
        return 1;
    }
    
    // Calcular y mostrar edad
    calcularEdad(nacimiento, hoy);
    
    return 0;
}
