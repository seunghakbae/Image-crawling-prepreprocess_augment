from Config import get_args
from Crawler import Crawler

def main():

    config = get_args()
    crawler = Crawler(config)
    crawler.crawl()

if __name__ =="__main__":
    main()
