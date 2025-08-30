import narwhals as nw
from narwhals.typing import IntoFrameT
import pandas as pd
import polars as pl

def func(df: IntoFrameT) -> IntoFrameT:
    return(
        nw.from_native(df)
        .select(a_sum=nw.col("a").sum(),
                a_mean=nw.col("a").mean(),
                a_std=nw.col("a").std(),
                
                ).to_native()
    )

# df = pd.DataFrame({"a":[1,1,2]})
# print('pandas:')
# print(func(df))

# df = pl.DataFrame({"a":[1,1,2]})
# print('polars:')
# print(func(df))

## groupby & mean

def func1(df:IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df).group_by("a").agg(nw.col("b").mean()).sort("a").to_native()
    )


df_pd = pd.DataFrame({"a": [1, 1, 2], "b": [4, 5, 6]})
# print('pandas:')
# print(func1(df_pd))

df_pl = pl.LazyFrame({"a": [1, 1, 2], "b": [4, 5, 6]})
# print('polars lazy:')
# print(func1(df_pl).collect())

## horizontal sum

def func2(df: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df)
        .with_columns(a_plus_b=nw.sum_horizontal("a", "b"))
        .to_native()
    )

print('pandas')
print(func2(df_pd))

print('lazy polars')
print(func2(df_pl).collect())



