from application import ScrapingData


if __name__ == '__main__':

    print("Scraping Data Prakerja Bukalapak............")
    run_data = ScrapingData()
    run_data.scrape_data()
    print("Scraping Completed")