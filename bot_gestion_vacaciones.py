import json

with open("empleados.json", "r", encoding="utf-8") as f:
    indice = json.load(f)


print(indice)

print('👋 Bienvenido al Bot de Vacaciones')
legajo = input('Por favor ingrese su legajo: ')

def consultar_saldo(legajo):
    print(f'Su saldo de dias disponible es de {indice[legajo]['dias_disponibles']}')


def solicitar_vaciones(legajo):
    inicio = input('Ingresa la fecha de inicio(DD/MM/AAAA) ')
    fin = input('Ingresa la fecha de fin(DD/MM/AAAA) ')
    print('Resumen')
    print(indice[legajo]['nombre'])
    print(f'Desde: {inicio}')
    print(f'Hasta: {fin}')
    confirmacion = input('Confirmas? Escribe SI o NO: ')
    

solicitar_vaciones(legajo)