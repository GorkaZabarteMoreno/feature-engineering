import pandas as pd

cols: list = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym",
              "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]

data: pd.DataFrame = pd.read_csv(filepath_or_buffer="../../data/magic04.data", names=cols)


def get_columns(df: pd.DataFrame):
    counter = 1
    for col in df.columns:
        # print("Column", counter, "is", col)
        counter += 1


def get_unique_values(column: str):
    unique_values = data[column].unique()
    return unique_values


get_columns(data)
