import json

with open("empleados.json", "r", encoding="utf-8") as f:
    indice = json.load(f)


print(indice)

print('👋 Bienvenido al Bot de Vacaciones')
print('Por favor ingrese su legajo')
legajo = input()

def consultar_saldo(legajo):
    print(f'Su saldo de dias disponible es de {indice[legajo]['dias_disponibles']}')


consultar_saldo(legajo)