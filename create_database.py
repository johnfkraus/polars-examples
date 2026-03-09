import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine  # for read database (not read_database_uri)

DB_NAME = "polars"

# 1. Connect to an existing database (NOT the one you're creating)
conn = psycopg2.connect(
    dbname="postgres",   # or "template1"
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

# 2. Allow CREATE DATABASE outside a transaction
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# 3. Create the new database safely
# DB_NAME = "polars"
with conn.cursor() as cur:
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
    if not cur.fetchone():
        print(f"Creating database {DB_NAME}...")
        cur.execute(f"CREATE DATABASE \"{DB_NAME}\"")
    else:
        print(f"Database {DB_NAME} already exists.")

    # cur.execute(
    #     sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME))
    # )

conn.close()
