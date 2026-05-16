DROP TABLE IF EXISTS profesores_audit CASCADE;
DROP TABLE IF EXISTS alumnos_audit CASCADE;
DROP TABLE IF EXISTS asignaturas_audit CASCADE;

DROP TABLE IF EXISTS profesores CASCADE;
DROP TABLE IF EXISTS alumnos CASCADE;
DROP TABLE IF EXISTS asignaturas CASCADE;

CREATE TABLE profesores (
    profesor_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE alumnos (

    alumno_id SERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    dinero NUMERIC(10,2) DEFAULT 0

);

CREATE TABLE asignaturas (

    asignatura_id SERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    precio NUMERIC(10,2) NOT NULL,

    max_alumnos INT NOT NULL

);

CREATE TABLE matriculas (

    matricula_id SERIAL PRIMARY KEY,

    alumno_id INT REFERENCES alumnos(alumno_id),

    asignatura_id INT REFERENCES asignaturas(asignatura_id),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE profesores_audit (
    audit_id SERIAL PRIMARY KEY,
    operacion TEXT,
    profesor_id INT,
    nombre_old TEXT,
    nombre_new TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alumnos_audit (
    audit_id SERIAL PRIMARY KEY,
    operacion TEXT,
    alumno_id INT,
    nombre_old TEXT,
    nombre_new TEXT,
    email_old TEXT,
    email_new TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE asignaturas_audit (
    audit_id SERIAL PRIMARY KEY,
    operacion TEXT,
    asignatura_id INT,
    nombre_old TEXT,
    nombre_new TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION fn_audit_profesores()
RETURNS TRIGGER AS $$
BEGIN

    IF TG_OP = 'INSERT' THEN

        INSERT INTO profesores_audit(
            operacion,
            profesor_id,
            nombre_new
        )
        VALUES(
            'INSERT',
            NEW.profesor_id,
            NEW.nombre
        );

        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN

        INSERT INTO profesores_audit(
            operacion,
            profesor_id,
            nombre_old,
            nombre_new
        )
        VALUES(
            'UPDATE',
            OLD.profesor_id,
            OLD.nombre,
            NEW.nombre
        );

        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN

        INSERT INTO profesores_audit(
            operacion,
            profesor_id,
            nombre_old
        )
        VALUES(
            'DELETE',
            OLD.profesor_id,
            OLD.nombre
        );

        RETURN OLD;

    END IF;

    RETURN NULL;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_profesores
AFTER INSERT OR UPDATE OR DELETE
ON profesores
FOR EACH ROW
EXECUTE FUNCTION fn_audit_profesores();

CREATE OR REPLACE FUNCTION fn_audit_alumnos()
RETURNS TRIGGER AS $$
BEGIN

    IF TG_OP = 'INSERT' THEN

        INSERT INTO alumnos_audit(
            operacion,
            alumno_id,
            nombre_new,
            email_new
        )
        VALUES(
            'INSERT',
            NEW.alumno_id,
            NEW.nombre,
            NEW.email
        );

        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN

        INSERT INTO alumnos_audit(
            operacion,
            alumno_id,
            nombre_old,
            nombre_new,
            email_old,
            email_new
        )
        VALUES(
            'UPDATE',
            OLD.alumno_id,
            OLD.nombre,
            NEW.nombre,
            OLD.email,
            NEW.email
        );

        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN

        INSERT INTO alumnos_audit(
            operacion,
            alumno_id,
            nombre_old,
            email_old
        )
        VALUES(
            'DELETE',
            OLD.alumno_id,
            OLD.nombre,
            OLD.email
        );

        RETURN OLD;

    END IF;

    RETURN NULL;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_alumnos
AFTER INSERT OR UPDATE OR DELETE
ON alumnos
FOR EACH ROW
EXECUTE FUNCTION fn_audit_alumnos();

CREATE OR REPLACE FUNCTION fn_audit_asignaturas()
RETURNS TRIGGER AS $$
BEGIN

    IF TG_OP = 'INSERT' THEN

        INSERT INTO asignaturas_audit(
            operacion,
            asignatura_id,
            nombre_new
        )
        VALUES(
            'INSERT',
            NEW.asignatura_id,
            NEW.nombre
        );

        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN

        INSERT INTO asignaturas_audit(
            operacion,
            asignatura_id,
            nombre_old,
            nombre_new
        )
        VALUES(
            'UPDATE',
            OLD.asignatura_id,
            OLD.nombre,
            NEW.nombre
        );

        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN

        INSERT INTO asignaturas_audit(
            operacion,
            asignatura_id,
            nombre_old
        )
        VALUES(
            'DELETE',
            OLD.asignatura_id,
            OLD.nombre
        );

        RETURN OLD;

    END IF;

    RETURN NULL;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_asignaturas
AFTER INSERT OR UPDATE OR DELETE
ON asignaturas
FOR EACH ROW
EXECUTE FUNCTION fn_audit_asignaturas();