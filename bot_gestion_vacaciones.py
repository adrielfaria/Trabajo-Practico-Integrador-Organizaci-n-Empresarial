import json
from datetime import datetime

with open("empleados.json", "r", encoding="utf-8") as f:
    indice = json.load(f)

def consultar_saldo(legajo):
    print(f'Su saldo de dias disponible es de {indice[legajo]['dias_disponibles']}')

def legajo():
    legajo = input('Por favor ingrese su legajo: ')
    if legajo in indice:
        print('legajo existe')
        return legajo
    else:
        print('El legajo ingresado no existe.')

def resumen(inicio, fin, dias_solicitados, dias_restantes, legajo_validado):
    return (
        'Resumen\n'
        f'{indice[legajo_validado]["nombre"]}\n'
        f'Desde: {inicio}\n'
        f'Hasta: {fin}\n'
        f'Dias: {dias_solicitados}\n'
        f'Nuevo saldo de dias restantes: {dias_restantes}\n'
    )

def confirmar_vacaciones():
    return print('Vacaciones confirmadas')

def confirmacion():
    opciones = {
        '1': confirmar_vacaciones,
        '2': salir
    }
    while True:
        print('\n1. SI')
        print('2. NO')
        opcion = input('Confirmas?')
        funcion = opciones.get(opcion)
        if funcion:
            resultado = funcion()
            if resultado is False:
                break
            

def solicitar_vaciones(legajo_validado):
    fecha_inicio = input('Ingresa la fecha de inicio(DD/MM/AAAA) ')
    fecha_fin = input('Ingresa la fecha de fin(DD/MM/AAAA) ')
    try:
        inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        fin = datetime.strptime(fecha_fin, '%d/%m/%Y')
        dias_solicitados = (fin - inicio).days + 1
        dias_restantes = indice[legajo_validado]['dias_disponibles'] - dias_solicitados
        print(resumen(inicio, fin, dias_solicitados, dias_restantes, legajo_validado))
        confirmacion()
        # confirmacion = input('Confirmas? Escribe SI o NO: ')
        # if confirmacion == 'SI':
        #     indice[legajo]['dias_disponibles'] = dias_restantes

    except ValueError:
        print('Ingrese una fecha valida.')
    except Exception as e:
        print(f'Error: {e}')

def salir():
    return False

def main():
    print('👋 Bienvenido al Bot de Vacaciones')
    legajo_validado = legajo()
    opciones = {
        '1': lambda: consultar_saldo(legajo_validado),
        '2': lambda: solicitar_vaciones(legajo_validado),
        '3': salir
    }

    while True:
        print('\n1. Consultar saldo')
        print('2. Solicitar vacaciones')
        print('3. Salir')

        opcion = input('Escoga una opcion: ')

        funcion = opciones.get(opcion)

        if funcion:
            resultado = funcion()
            if resultado is False:
                break
    
if __name__ == '__main__':
    main()