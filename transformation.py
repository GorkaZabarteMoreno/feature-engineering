import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from understanding import data


def encode_class(df: pd.DataFrame, tar: str):
    encoder = LabelEncoder()
    encoder.fit(df[tar])
    df[tar] = encoder.transform(df[tar])
    return df
    

data: pd.DataFrame = encode_class(data, "class")
target: pd.Series = data["class"]
