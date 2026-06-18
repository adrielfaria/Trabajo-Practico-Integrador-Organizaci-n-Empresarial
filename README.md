# Bot de Gestión de Vacaciones

Trabajo Práctico Integrador — Organización Empresarial  
Tecnicatura Universitaria en Programación (TUPaD) — UTN

---

## Descripción

Bot de consola desarrollado en Python que automatiza el proceso de gestión de vacaciones de una organización ficticia. Permite a los empleados consultar su saldo de días disponibles, solicitar vacaciones y cancelar solicitudes activas. Los datos se persisten en un archivo JSON que simula una base de datos.

---

## Estructura del proyecto

```
├── bot_gestion_vacaciones.py   # Código principal del bot (lógica completa)
├── empleados.json              # Base de datos simulada (empleados, saldos y vacaciones activas)
└── README.md                   # Este archivo
```

### Descripción de archivos

**`bot_gestion_vacaciones.py`**  
Contiene toda la lógica del bot: validación de legajo, menú de opciones, solicitud de vacaciones con validación de fechas y saldo, cancelación de vacaciones y persistencia de datos. Cada función tiene su responsabilidad definida y está comentada.

**`empleados.json`**  
Actúa como base de datos plana. Almacena el legajo, nombre, días disponibles y vacaciones activas de cada empleado. Se actualiza automáticamente cada vez que se confirma o cancela una solicitud.

---

## Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/adrielfaria/Trabajo-Practico-Integrador-Organizaci-n-Empresarial
cd Trabajo-Practico-Integrador-Organizaci-n-Empresarial
```

2. Verificar que `empleados.json` esté en la misma carpeta que el script.

3. Ejecutar el bot:

```bash
python bot_gestion_vacaciones.py
```

---

## Uso

Al iniciar, el bot solicita el **legajo** del empleado. Si es válido, presenta el menú principal:

| Opción | Acción | Descripción |
|--------|--------|-------------|
| `1` | Consultar saldo | Muestra los días disponibles. No modifica datos. |
| `2` | Solicitar vacaciones | Pide fechas, valida saldo y solicitudes previas, muestra resumen y pide confirmación. |
| `3` | Cancelar vacaciones | Elimina la solicitud activa y reintegra los días al saldo. |
| `4` | Salir | Cierra el bot. Los datos quedan guardados. |

### Formato de fechas

Las fechas deben ingresarse en formato `DD/MM/AAAA`. Ejemplo: `25/07/2026`.  
Cualquier otro formato es rechazado con un mensaje de error.

### Flujo de solicitud de vacaciones

1. El bot verifica que no haya una solicitud activa previa.
2. Solicita fecha de inicio y fecha de fin.
3. Valida que las fechas sean futuras y que el fin sea posterior al inicio.
4. Calcula los días solicitados y verifica el saldo disponible.
5. Muestra un resumen con el nuevo saldo resultante.
6. Pide confirmación (Sí / No) antes de guardar.

---

## Base de datos

El archivo `empleados.json` tiene la siguiente estructura:

```json
{
  "1001": {
    "nombre": "Juan Perez",
    "dias_disponibles": 10,
    "vacaciones_activas": null
  },
  "1002": {
    "nombre": "Maria Gomez",
    "dias_disponibles": 10,
    "vacaciones_activas": {
      "fecha_inicio": "2026-07-01",
      "fecha_fin": "2026-07-10",
      "dias_solicitados": 10
    }
  }
}
```

`vacaciones_activas` es `null` cuando no hay solicitud activa, o un objeto con `fecha_inicio`, `fecha_fin` y `dias_solicitados` cuando sí la hay.

---

## Empleados de prueba

| Legajo | Nombre | Días disponibles | Vacaciones activas |
|--------|--------|------------------|--------------------|
| 1001 | Juan Perez | 3 | Sí |
| 1002 | Maria Gomez | 10 | No |
| 1003 | Carlos Rodriguez | 20 | No |
| 1004 | Lucia Fernandez | 8 | No |
| 1005 | Sofia Martinez | 3 | No |

---

## Manejo de errores

El bot maneja los siguientes casos sin interrumpirse:

| Caso | Mensaje del bot |
|------|----------------|
| Legajo inexistente | "El legajo ingresado no existe." |
| Opción de menú inválida | El menú se repite sin interrumpirse |
| Formato de fecha incorrecto | "Ingrese una fecha valida." |
| Fecha en el pasado o fin anterior al inicio | "La fecha ingresada no es valida." |
| Saldo insuficiente | "Saldo de dias insuficiente." |
| Ya tiene vacaciones activas | "Ya tienes vacaciones solicitadas... debés cancelarlas primero." |
| Cancelar sin solicitud activa | "No tienes vacaciones activas para cancelar." |

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Persistencia:** archivo JSON (módulo estándar `json`)
- **Manejo de fechas:** módulo estándar `datetime`
- **Plataforma:** consola (simulación de chatbot)

---

