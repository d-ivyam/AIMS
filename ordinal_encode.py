import pandas as pd
import numpy as np

class OrdinalEncoder:
    def __init__(self, df, columns):
        self.columns = columns
        self.df = df

    def startEncode(self):
        
        uniqueVals = dict()
        for col in self.columns:
            temp = []
            for i,j in enumerate(self.df[col].unique()):
                temp.append([j, (i+1)])
            uniqueVals[col] = temp

        for i in uniqueVals.keys():
            for j in uniqueVals[i]:
                val = j[0]
                newVal = j[1]
                for count in range(self.df.shape[0]):
                    if self.df.loc[count,i] == val:
                        self.df.loc[count, i] = newVal
                    else:
                        pass

        return self.df              
            

if __name__ == '__main__':
    df = pd.read_csv('basicData.csv')
    ordinal = df.select_dtypes('object')
    instance = OrdinalEncoder(df, ordinal.columns)
    df = OrdinalEncoder.startEncode(instance)
    print(df)
