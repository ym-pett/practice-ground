from typing import Self
import narwhals as nw
from narwhals.typing import IntoDataFrameT
import pandas as pd
import polars as pl

class StandardScaler:
    def fit(self, df: IntoDataFrameT) -> Self:
        df_nw = nw.from_native(df, eager_only=True)
        self._means = {col: df_nw[col].mean() for col in df_nw.columns}
        self._std_devs = {col: df_nw[col].std() for col in df_nw.columns}
        self._columns = df_nw.columns
        return self
    
    def transform(self, df: IntoDataFrameT) -> IntoDataFrameT:
        df_nw = nw.from_native(df)
        return df_nw.with_columns(
            (nw.col(col) - self._means[col])/ self._std_devs[col]
            for col in self._columns
        ).to_native()
    
df_train = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 7]})
df_test = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 7]})
scaler = StandardScaler()
scaler.fit(df_test)
print(scaler.transform(df_test))

# polars
df_train_pl = nw.from_native(df_test).to_polars()
df_test_pl = nw.from_native(df_test, eager_only=False).to_native()
scaler.fit(df_train_pl)
print(scaler.transform(df_test_pl))