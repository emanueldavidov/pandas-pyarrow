from typing import Tuple

from pandas_pyarrow import convert_to_pyarrow
from pandas_pyarrow.mappers import datetime_mapper
from tests.unit.property_based.pb_sts import single_column_df_st

import hypothesis as hp
import pandas as pd


@hp.given(pair=single_column_df_st(gen_type="datetime64[ns]", pair_mapping=datetime_mapper()))
def test_datetime_pb_ns(pair: Tuple[pd.DataFrame, str]):
    df, target_dtype = pair
    adf = convert_to_pyarrow(df)
    assert list(adf.dtypes)[0] == target_dtype
