import pandas as pd
import numpy as np

class OneHotEncoder:
    def __init__(self, df, columns):
        self.columns = columns
        self.df = df

    def startEncode(self):
        
        uniqueVals = dict()
        for col in self.columns:
            uniqueVals[col] = self.df[col].unique()

        for i in uniqueVals.keys():
            for j in uniqueVals[i]:
                for count in range(self.df.shape[0]):
                    if self.df.loc[count, i] == j:
                        self.df.loc[count, j] = 1
                    else:
                        self.df.loc[count, j] = 0
            self.df = self.df.drop([i], axis=1)

        self.df = self.df.drop(np.nan, axis = 1)
        return self.df
    

if __name__ == '__main__':
    df = pd.read_csv('basicData.csv')
    oneHot = df.select_dtypes('object')
    instance = OneHotEncoder(df, oneHot.columns)
    df = OneHotEncoder.startEncode(instance)
    print(df)
