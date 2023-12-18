import numpy as np
import pandas as pd


def SimpleImputer(data, strategy="mean", fill_value=None):
    # first checking if it is a pandas dataframe, if not convert it into dataframe
    if isinstance(data, pd.DataFrame):
        df = data
    else:
        try:
            df = pd.DataFrame(data)
        except Exception as e:
            raise ValueError(e)

    # imputation process
    imputed_df = df.copy()
    for column in df.columns:
        if strategy == "mean":
            imputed_df[column] = df[column].fillna(df[column].mean())
        elif strategy == "median":
            imputed_df[column] = df[column].fillna(df[column].median())
        elif strategy in ["mode", "most_frequent"]:
            imputed_df[column] = df[column].fillna(
                df[column].mode().iloc[0]
            )  # iloc[0] for getting first value of mode if many vals
        elif strategy == "constant":
            imputed_df[column] = df[column].fillna(fill_value)
        else:
            raise ValueError("Invalid Imputation Strategy")
    return imputed_df


# example testing
data = np.array([[1, 2, np.nan], [33, 4, 11], [np.nan, np.nan, 22]])
for strategy in ["mean", "mode", "median", "constant"]:
    if strategy == "constant":
        imputed_data = SimpleImputer(data, strategy=strategy, fill_value=10)
    else:
        imputed_data = SimpleImputer(data, strategy=strategy)

    print("Imputed Data(mean):\n")
    print(imputed_data)