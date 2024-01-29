import re
import json, os, glob
import requests, pandas as pd #type: ignore
from . url import UrlData
from datetime import datetime


class ScrapingData:
    def scrape_data(self):
        UrlDataScrape = UrlData.url_bl(self)

        for index, ScrapeUrl in enumerate(UrlDataScrape):
            HtmlDoc = requests.get(ScrapeUrl).text
            DataScrape = re.search(r"window.INIT_DATA=(.*)}", HtmlDoc).group(1)
            DataDict = DataScrape + "}"
            DateData = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            with open(f"./output/{DateData}_{index+1}.json", "w", encoding='utf-8') as OutputFile:
                OutputFile.write(DataDict)

        DirData = './output'
        JsonPattern = os.path.join(DirData, '*.json')
        ListFile = glob.glob(JsonPattern)

        DataFrameList = []

        for FileData in ListFile:
            with open(FileData, encoding='utf-8') as f:
                JsonData = pd.json_normalize(json.loads(f.read()))
                JsonData['site'] = FileData.rsplit("/", 1)[-1]
            DataFrameList.append(JsonData)

        DataFrameFinal = pd.concat(DataFrameList)

        DataFrameClean = DataFrameFinal[["courseDetail.name",
                                         "courseDetail.deal.merchant.name",
                                         "courseDetail.sold",
                                         "courseDetail.rating.value",
                                         "courseDetail.discount.original_price"]]
        DataFrameClean = DataFrameClean.rename(columns={
                                    "courseDetail.name": "Course Name",
                                    "courseDetail.deal.merchant.name": "Merchant",
                                    "courseDetail.sold": "Sold",
                                    "courseDetail.rating.value": "Rating",
                                    "courseDetail.discount.original_price": "Price"})

        time = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        DataFrameClean.to_csv(f"./dataclean/data_bukalapak_{time}.csv")