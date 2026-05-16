import psycopg

conninfo = (
    "host=localhost "
    "port=5434 "
    "dbname=auditoria_db "
    "user=postgres "
    "password=1234"
)

def get_conn():
    return psycopg.connect(conninfo)