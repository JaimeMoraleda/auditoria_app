<<<<<<< HEAD
# Auditoria App — Flask + PostgreSQL

Aplicación web desarrollada con Flask y PostgreSQL para la gestión académica de:
=======
# Auditoria App — PostgreSQL + Flask + PostGIS

Sistema académico desarrollado con arquitectura MVC utilizando Flask y PostgreSQL.  
Incluye funcionalidades avanzadas de bases de datos como auditoría, transacciones, JSONB multiidioma, consultas SQL avanzadas y soporte GIS mediante PostGIS.

---

# 1. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Backend |
| Flask | Framework web MVC |
| PostgreSQL | Base de datos relacional |
| PostGIS | Extensión GIS |
| JSONB | Soporte multiidioma |
| Leaflet.js | Visualización de mapas |
| OpenStreetMap | Mapas GIS |
| Git + GitHub | Control de versiones |

---

# 2. Funcionalidades implementadas

## Gestión académica


- Profesores
- Alumnos
- Asignaturas
- Matrículas

<<<<<<< HEAD
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

````

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


```text
=======
---

## CRUD completo

El sistema permite:

### Profesores
- Crear
- Modificar
- Eliminar

### Alumnos
- Crear
- Modificar
- Eliminar

### Asignaturas
- Crear
- Modificar
- Eliminar

---

## Matrículas transaccionales

La matrícula de alumnos incluye:

- Validación de saldo disponible
- Validación de plazas máximas
- Uso de transacciones SQL
- Rollback automático en caso de error

---

## Auditoría

Se implementan tablas de auditoría para:

- profesores
- alumnos
- asignaturas

Registrando operaciones:

- INSERT
- UPDATE
- DELETE

---

## JSONB Multiidioma

Las asignaturas almacenan nombres en varios idiomas utilizando JSONB.

Ejemplo:

```json
>>>>>>> 3bf4a6f (Añadido soporte GIS, PostGIS y mapa interactivo)
{
  "es": "Bases de Datos",
  "en": "Databases",
  "fr": "Bases de données"
}
<<<<<<< HEAD
````
Índices implementados
---
Se utilizan índices para optimizar búsquedas:

Índices GIN sobre JSONB
Índices trigram (pg_trgm)
Índices sobre relaciones y matrículas

---
Requisitos
---
Python 3.11+
PostgreSQL 15+
pgAdmin (opcional)
=======
```

Características:

- búsquedas por idioma
- consultas usando `->>`
- búsquedas `ILIKE`
- índices GIN

---

## GIS + PostGIS

El sistema incluye funcionalidades geográficas:

### Alumnos
Se representan mediante:

```sql
POINT
```

### Asignaturas
Se representan mediante:

```sql
POLYGON
```

### Funcionalidades GIS

- Geolocalización de alumnos
- Áreas geográficas de asignaturas
- Movimiento de alumnos ("viajar")
- Consultas espaciales
- `ST_Contains`
- Visualización en mapas

---

## Mapa interactivo

Se implementa un mapa GIS utilizando:

- Leaflet.js
- OpenStreetMap
- PostgreSQL + PostGIS

Visualizando:

- alumnos como marcadores
- asignaturas como polígonos

Ruta:

```text
/mapa
```

---

## Consultas SQL avanzadas

El proyecto incluye consultas utilizando:

- ROW_NUMBER
- GROUPING SETS
- ROLLUP
- FILTER

---

# 3. Estructura del proyecto

```text
auditoria_app/
│
├── app.py
├── requirements.txt
├── schema.sql
├── seed.sql
├── consultas_avanzadas.sql
├── gis_postgis.sql
│
├── routes/
│   ├── alumnos.py
│   ├── profesores.py
│   ├── asignaturas.py
│   ├── matriculas.py
│   └── mapa.py
│
├── templates/
│   ├── index.html
│   ├── mapa.html
│   ├── alumnos.html
│   ├── profesores.html
│   ├── asignaturas.html
│   └── matriculas.html
│
├── static/
│
└── database.ini
```

---

# 4. Instalación del proyecto

## Clonar repositorio

```bash
git clone https://github.com/JaimeMoraleda/auditoria_app
cd auditoria_app
```

---

## Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 5. Configuración PostgreSQL

Crear una base de datos:

```sql
CREATE DATABASE auditoria_db;
```

---

## Activar PostGIS

```sql
CREATE EXTENSION postgis;
```

---

# 6. Crear esquema

Ejecutar:

```bash
schema.sql
```

Esto crea:

- tablas principales
- claves foráneas
- auditoría
- índices
- columnas JSONB
- columnas GIS

---

# 7. Insertar datos iniciales

Ejecutar:

```bash
seed.sql
```

Esto inserta:

- profesores
- alumnos
- asignaturas
- matrículas

---

# 8. Configuración conexión PostgreSQL

Editar credenciales dentro de:

```text
app.py
```

Ejemplo:

```python
conninfo = "host=localhost dbname=auditoria_db user=postgres password=TU_PASSWORD"
```

---

# 9. Ejecutar aplicación

```bash
python app.py
```

---

# 10. Acceder a la aplicación

Abrir navegador:

```text
http://127.0.0.1:5000
```

---

# 11. Rutas disponibles

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/alumnos` | Gestión de alumnos |
| `/profesores` | Gestión de profesores |
| `/asignaturas` | Gestión de asignaturas |
| `/matriculas` | Gestión de matrículas |
| `/mapa` | Visualización GIS |
| `/vista` | Vista SQL relacional |

---

# 12. Funcionalidades GIS

## Ver posiciones de alumnos

```sql
SELECT
    alumno_id,
    nombre,
    ST_AsText(ubicacion)
FROM alumnos;
```

---

## Ver polígonos de asignaturas

```sql
SELECT
    asignatura_id,
    ST_AsText(aula)
FROM asignaturas;
```

---

## Verificar si un alumno está dentro de un aula

```sql
SELECT
    ST_Contains(aula, ubicacion)
FROM asignaturas, alumnos;
```

---

# 13. Ejemplos JSONB

## Obtener nombre en inglés

```sql
SELECT nombres ->> 'en'
FROM asignaturas;
```

---

## Búsqueda por idioma

```sql
SELECT *
FROM asignaturas
WHERE nombres ->> 'fr'
ILIKE '%base%';
```

---

# 14. Índices implementados

## Índice GIN JSONB

```sql
CREATE INDEX idx_asignaturas_nombres
ON asignaturas
USING GIN (nombres);
```

---

## Índices relacionales

- alumnos(email)
- matriculas(alumno_id)
- matriculas(asignatura_id)

---

# 15. Autor

Proyecto desarrollado para la asignatura de Bases de Datos Avanzadas.

Tecnologías principales:
- PostgreSQL
- Flask
- PostGIS
- JSONB
- GIS
- SQL avanzado
>>>>>>> 3bf4a6f (Añadido soporte GIS, PostGIS y mapa interactivo)
