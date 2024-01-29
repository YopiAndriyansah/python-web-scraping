import pandas as pd #type: ignore

class UrlData:

    def url_bl(self):

        DataFrame       = pd.read_csv("./listurl/url_bl_new.csv")

        DataFrameList = DataFrame.values.tolist()

        DataFrameList = [i[0] for i in DataFrameList]

        return DataFrameList
