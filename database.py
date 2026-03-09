
import polars as pl

from sqlalchemy import create_engine  # for read database (not read_database_uri)

# read from database
# When using pl.read_database_uri, you can specify one of two engines to read from the database:
# ConnectorX and
# ADBC
# https://docs.pola.rs/user-guide/io/database/#engines
# pip install connectorx pyarrow
uri = "postgresql://postgres:postgres@localhost:5432/northwind"
query = "SELECT * FROM public.products"

df_nw_products = pl.read_database_uri(query=query, uri=uri)
print(df_nw_products.head())


# requires sqlalchemy:
# requires psycopg2 pandas
conn = create_engine(uri)  # f"sqlite:///test.db")

query = "SELECT * FROM public.products"

df_products = pl.read_database(query=query, connection=conn.connect())
print(f"25, {df_products=}")


# SQLAlchemy
# With the default engine SQLAlchemy you can write to any database supported by SQLAlchemy. To use this engine you need to install SQLAlchemy and Pandas

# pip install SQLAlchemy pandas
# write database

uri = "postgresql://postgres:postgres@localhost:5432/polars"
# uri = "postgresql://username:password@server:port/database"
df = pl.DataFrame({"foo": [1, 2, 3]})

df.write_database(table_name="examples.records",  connection=uri)


