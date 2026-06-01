import json
from datetime import datetime

with open("empleados.json", "r", encoding="utf-8") as f:
    indice = json.load(f)


print(indice)


def consultar_saldo(legajo):
    print(f'Su saldo de dias disponible es de {indice[legajo]['dias_disponibles']}')


def solicitar_vaciones(legajo):
    fecha_inicio = input('Ingresa la fecha de inicio(DD/MM/AAAA) ')
    fecha_fin = input('Ingresa la fecha de fin(DD/MM/AAAA) ')
    try:
        inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        fin = datetime.strptime(fecha_fin, '%d/%m/%Y')
        dias_solicitados = (fin - inicio).days + 1
        print('Resumen')
        print(indice[legajo]['nombre'])
        print(f'Desde: {inicio}')
        print(f'Hasta: {fin}')
        print(f'Dias: {dias_solicitados}')
        confirmacion = input('Confirmas? Escribe SI o NO: ')
    except Exception as e:
        print(f'Error: {e}')

def salir():
    return False

def main():
    print('👋 Bienvenido al Bot de Vacaciones')
    legajo = input('Por favor ingrese su legajo: ')
    opciones = {
        '1': consultar_saldo,
        '2': solicitar_vaciones,
        '3': salir
    }

    while True:
        print('\n1. Consultar saldo')
        print('2. Solicitar vacaciones')
        print('3. Salir')

        opcion = input('Escoga una opcion: ')

        funcion = opciones.get(opcion)

        if funcion:
            resultado = funcion(legajo)
            if resultado is False:
                break
    
if __name__ == '__main__':
    main()