import pandas as pd
from sklearn.preprocessing import LabelEncoder

from machine_learning.features.FeatureEngineering.stats import mean, standard_deviation
from machine_learning.features.FeatureEngineering.understanding import data


def normalize(ser):
    minimum = min(ser)
    maximum = max(ser)
    return [round((x - minimum) / (maximum - minimum), 3) for x in ser]


def standardize(ser):
    avg = mean(ser)
    std = standard_deviation(ser)
    return [round((x - avg) / std, 3) for x in ser]


def encode_class(df: pd.DataFrame, tar: str):
    encoder = LabelEncoder()
    encoder.fit(df[tar])
    df[tar] = encoder.transform(df[tar])
    return df


data: pd.DataFrame = encode_class(data, "class")
target: pd.Series = data["class"]
