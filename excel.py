
import polars as pl

df = pl.read_excel("output.xlsx")
print(f"{df=}")


df = pl.read_excel("output2.xlsx")
print(f"9, {df=}")

# requires pip install xlsxwriter
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_excel("polars_write_excel.xlsx")


df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_excel("sheet_name.xlsx", worksheet="Sales")


uri = "postgresql://postgres:postgres@localhost:5432/northwind"
query = "SELECT * FROM public.products"

df_nw_products = pl.read_database_uri(query=query, uri=uri)
print(df_nw_products.head())

df_nw_products.write_excel("northwind.xlsx", worksheet="Products")

df_nw_products_read = pl.read_excel("northwind2.xlsx")
print(f"{df_nw_products_read=}")
