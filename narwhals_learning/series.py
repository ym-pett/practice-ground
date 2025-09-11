import narwhals as nw
from narwhals.typing import IntoFrameT, FrameT, IntoDataFrameT
import pandas as pd
import polars as pl
from typing import reveal_type

def my_func(df: IntoFrameT) -> IntoFrameT:
    return nw.from_native(df).filter(nw.col("a") > 0).to_native()

df = pd.DataFrame({"a": [-1,1,3], "b": [3,5,-3]})
print(my_func(df))

# if I want to filter on multiple columns, TODO: investigate way of targetting all columns without naming them: 
print(nw.from_native(df).filter(nw.col("a")> 0, nw.col("b")> 0).to_native())

def my_func1(df: IntoFrameT) -> IntoFrameT:
    return nw.from_native(df).with_columns(nw.col("a")*2).to_native()

# # eager
# df_pl = nw.from_native(df, eager_only=True).to_polars()
# print(my_func1(df_pl))

# eager without using pd dataframe:
df_pl = pl.DataFrame({"a": [-1, 1, 3], "b": [3, 5, -3]})
print(my_func1(df_pl))

# lazy
df_lazy = pl.LazyFrame({"a": [-1, 1, 3], "b": [3, 5, -3]})
print(my_func1(df_lazy).collect())

# to make a new column:
@nw.narwhalify # TODO: why do we need it? 
def my_func2(df: FrameT) -> FrameT:
    return nw.from_native(df).with_columns((nw.col("a")*2).alias("double_a"))

print(my_func2(df))

# finding the mean of a column as a scalar
# does this need to be `IntoDataFrameT`? Could it also works with `IntoFrameT`?

def my_func3(df: IntoDataFrameT) -> float | None:
    return nw.from_native(df, eager_only=True)["a"].mean()

print(my_func3(df))

















