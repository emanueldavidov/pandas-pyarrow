



# SchemArrow
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SchemArrow)](https://pypi.org/project/SchemArrow/)
[![version](https://img.shields.io/pypi/v/SchemArrow)](https://img.shields.io/pypi/v/SchemArrow)
[![License](https://img.shields.io/:license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![OS](https://img.shields.io/badge/ubuntu-blue?logo=ubuntu)
![OS](https://img.shields.io/badge/win-blue?logo=windows)
![OS](https://img.shields.io/badge/mac-blue?logo=apple)
[![Code Checks](https://github.com/DanielAvdar/SchemArrow/actions/workflows/code-checks.yml/badge.svg)](https://github.com/DanielAvdar/SchemArrow/actions/workflows/code-checks.yml)
[![Tests](https://github.com/DanielAvdar/SchemArrow/actions/workflows/ci.yml/badge.svg)](https://github.com/DanielAvdar/SchemArrow/actions/workflows/ci.yml)
[![Codecov](https://codecov.io/gh/DanielAvdar/SchemArrow/branch/master/graph/badge.svg)](https://codecov.io/gh/DanielAvdar/SchemArrow)


`SchemArrow` simplifies the conversion between pandas and Arrow DataFrames, allowing seamlessly switch to pyarrow pandas backend.

## Get started:
### Installation
To install the package use pip:

```bash
pip install schemarrow
```
### Usage

```python
import pandas as pd

from schemarrow import SchemArrow

# Create a pandas DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.1, 2.2, 3.3],
    'D': [True, False, True]
})

# Instantiate a SchemArrow object
arrow_schema = SchemArrow()

# Convert the pandas DataFrame dtypes to arrow dtypes
df_pa: pd.DataFrame = arrow_schema(df)

print(df_pa.dtypes)
```
outputs:
```
A     int64[pyarrow]
B    string[pyarrow]
C    double[pyarrow]
D      bool[pyarrow]
dtype: object
```


Furthermore, it's possible to add mappings or override existing ones:

```python
import pandas as pd

from schemarrow import SchemArrow

# Create a pandas DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.1, 2.2, 3.3],
    'D': [True, False, True]
})

# Instantiate a SchemArrow object
arrow_schema = SchemArrow(custom_mapper={'int64': 'int32[pyarrow]', 'float64': 'float32[pyarrow]'})

# Convert the pandas DataFrame dtypes to arrow dtypes
df_pa: pd.DataFrame = arrow_schema(df)

print(df_pa.dtypes)
```
