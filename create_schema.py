import psycopg2
from psycopg2 import sql

DB_NAME = "polars"
SCHEMA_NAME = "examples"

conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",          # adjust
    password="postgres", # adjust
    host="127.0.0.1",
    port="5432",
)

conn.autocommit = True  # or use an explicit transaction

with conn.cursor() as cur:
    cur.execute(
        sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(
            sql.Identifier(SCHEMA_NAME)
        )
    )

conn.close()
print(f"Schema {SCHEMA_NAME} ensured in database {DB_NAME}.")
