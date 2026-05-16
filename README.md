# Auditoria App — Flask + PostgreSQL

Aplicación web desarrollada con Flask y PostgreSQL para la gestión académica de:

- Profesores
- Alumnos
- Asignaturas
- Matrículas

El proyecto incluye:

- Arquitectura MVC
- CRUD completo
- Auditoría de cambios
- Transacciones
- Control de matrículas
- JSONB multiidioma
- Índices PostgreSQL
- GitHub colaborativo

---

# Tecnologías utilizadas

- Python 3
- Flask
- PostgreSQL
- Psycopg
- HTML / CSS
- Git + GitHub

---

# Estructura del proyecto

```text
auditoria_app/
│
├── app.py
├── schema.sql
├── seed.sql
├── requirements.txt
├── database.ini.example
├── .gitignore
│
├── routes/
│   ├── profesores.py
│   ├── alumnos.py
│   └── asignaturas.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── profesores.html
│   ├── alumnos.html
│   ├── asignaturas.html
│   └── matriculas.html
│
├── static/
│   └── style.css
│
└── audit/

Funcionalidades implementadas
Gestión de profesores
Crear profesores
Modificar profesores
Eliminar profesores
Auditoría de cambios
Gestión de alumnos
Crear alumnos
Modificar alumnos
Eliminar alumnos
Gestión de email
Gestión de dinero disponible
Auditoría
Gestión de asignaturas
Crear asignaturas
Modificar asignaturas
Eliminar asignaturas
Precio de asignaturas
Límite máximo de alumnos
Soporte multiidioma con JSONB
Matrículas
Matrícula visual
Control transaccional
Rollback automático
Validación de dinero
Validación de plazas disponibles
Multiidioma JSONB

Las asignaturas soportan múltiples idiomas mediante PostgreSQL JSONB.

Ejemplo:

{
  "es": "Bases de Datos",
  "en": "Databases",
  "fr": "Bases de données"
}

Consultas usando:

nombres ->> 'es'
Índices implementados

Se utilizan índices para optimizar búsquedas:

Índices GIN sobre JSONB
Índices trigram (pg_trgm)
Índices sobre relaciones y matrículas
Requisitos
Python 3.11+
PostgreSQL 15+
pgAdmin (opcional)
