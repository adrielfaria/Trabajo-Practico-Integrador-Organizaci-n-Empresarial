import json
from datetime import datetime, date

with open("empleados.json", "r", encoding="utf-8") as f:
    indice = json.load(f)

def consultar_saldo(legajo):
    print(f'Su saldo de dias disponible es de {indice[legajo]['dias_disponibles']}')

def pedir_legajo():
    legajo = input('Por favor ingrese su legajo: ')
    if legajo in indice:
        return legajo
    else:
        print('El legajo ingresado no existe.')
        return False

def resumen(inicio, fin, dias_solicitados, dias_restantes, legajo_validado):
    return (
        'Resumen\n'
        f'{indice[legajo_validado]["nombre"]}\n'
        f'Desde: {inicio}\n'
        f'Hasta: {fin}\n'
        f'Dias: {dias_solicitados}\n'
        f'Nuevo saldo de dias restantes: {dias_restantes}\n'
    )

def confirmar_vacaciones(legajo_validado, dias_solicitados, inicio, fin):
    indice[legajo_validado]['dias_disponibles'] -= dias_solicitados
    indice[legajo_validado]['vacaciones_activas'] = {
        'fecha_inicio': str(inicio),
        'fecha_fin': str(fin),
        'dias_solicitados': dias_solicitados
    }
    with open('empleados.json', 'w', encoding='utf-8') as f:
        json.dump(indice, f, ensure_ascii=False, indent=4)
    print('Vacaciones confirmadas y saldo actualizado.')

def cancelar_vacaciones(legajo_validado):
    vac = indice[legajo_validado]['vacaciones_activas']
    if vac is None:
        print('No tienes vacaciones activas para cancelar')
        return
    indice[legajo_validado]['dias_disponibles'] += vac["dias_solicitados"]
    indice[legajo_validado]['vacaciones_activas'] = None
    with open('empleados.json', 'w', encoding='utf-8') as f:
        json.dump(indice, f, ensure_ascii=False, indent=4)
    print('Vacaciones canceladas. Se reintegraron los días a tu saldo.')

def confirmacion(legajo_validado, dias_solicitados, inicio, fin):
    opciones = {
        '1': lambda: confirmar_vacaciones(legajo_validado, dias_solicitados, inicio, fin),
    }
    while True:
        print('\n1. SI')
        print('2. NO')
        opcion = input('Confirmas? ')
        if opcion == '2':
            break
        funcion = opciones.get(opcion)
        if funcion:
            funcion()
            break
            
def validar_fecha(legajo_validado, inicio, fin, dias_solicitados):
    dias_restantes = indice[legajo_validado]['dias_disponibles'] - dias_solicitados
    if dias_restantes < 0:
        print('Saldo de dias insuficiente')
        return False
    else:
        print(resumen(inicio, fin, dias_solicitados, dias_restantes, legajo_validado))
        return True
    

def solicitar_vacaciones(legajo_validado):
    if indice[legajo_validado]['vacaciones_activas'] is not None:
        vac = indice[legajo_validado]['vacaciones_activas']
        print(f'Ya tienes vacaciones solicitadas del {vac["fecha_inicio"]}al {vac["fecha_fin"]}.')
        print('Para solicitar nuevas vacaciones primero debés cancelar las actuales.')
        return

    fecha_inicio = input('Ingresa la fecha de inicio(DD/MM/AAAA) ')
    fecha_fin = input('Ingresa la fecha de fin(DD/MM/AAAA) ')
    try:
        inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y').date()
        fin = datetime.strptime(fecha_fin, '%d/%m/%Y').date()
        if date.today() < inicio < fin:        
            dias_solicitados = (fin - inicio).days + 1
            if validar_fecha(legajo_validado, inicio, fin, dias_solicitados):
                confirmacion(legajo_validado, dias_solicitados, inicio, fin)
        else:
            print('La fecha ingresdaa no es valida.')

    except ValueError:
        print('Ingrese una fecha valida.')
    except Exception as e:
        print(f'Error: {e}')


def main():
    print('👋 Bienvenido al Bot de Vacaciones')
    legajo_validado = pedir_legajo()
    if legajo_validado == False:
        return
    opciones = {
        '1': lambda: consultar_saldo(legajo_validado),
        '2': lambda: solicitar_vacaciones(legajo_validado),
        '3': lambda: cancelar_vacaciones(legajo_validado),
    }

    while True:
        print('\n1. Consultar saldo')
        print('2. Solicitar vacaciones')
        print('3. Cancelar vacaciones')
        print('4. Salir')

        opcion = input('Escoga una opcion: ')

        if opcion == '4':
            print('Terminando la ejecucion del programa')
            break

        funcion = opciones.get(opcion)

        if funcion:
            funcion()
            
    
if __name__ == '__main__':
    main()