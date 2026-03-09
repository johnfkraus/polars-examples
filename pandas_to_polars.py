
import pandas as pd
import polars as pl

# Example Pandas DataFrame
pandas_df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.1, 2.2, 3.3]
})

# Convert to Polars DataFrame
polars_df = pl.from_pandas(pandas_df)

print(polars_df)