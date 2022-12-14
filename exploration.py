import pandas as pd
import matplotlib.pyplot as plt

from machine_learning.features.FeatureEngineering.transformation import data


def get_histograms(df: pd.DataFrame, tar: str):
    cols = df.columns
    for col in cols[:-1]:
        plt.hist(df[df[tar] == 1][col], color="red", label="hadron", alpha=0.7, density=True)
        plt.hist(df[df[tar] == 0][col], color="blue", label="gamma", alpha=0.7, density=True)
        plt.title(col)
        plt.ylabel("Probability")
        plt.xlabel(col)
        plt.show()


get_histograms(df=data, tar="class")
