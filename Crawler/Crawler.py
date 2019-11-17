from selenium import webdriver
import json
import os
import urllib.request

class Crawler():

    def __init__(self, config):
        self.search_term = config.image_name
        self.chrome_driver = config.chrome_driver_path

    def crawl(self):

        # 찾고자 하는 검색어를 url로 만들어 준다.
        url = "https://www.google.com/search?q=" + self.search_term + "&source=lnms&tbm=isch"

        # chrom webdriver 사용하여 브라우저를 가져온다.
        browser = webdriver.Chrome(self.chrome_driver)
        browser.get(url)

        header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

        counter = 0
        succounter = 0

        if not os.path.exists(self.search_term):
            os.mkdir(self.search_term)

        for _ in range(10000):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
            browser.execute_script("window.scrollBy(0,10000)")

        # div태그에서 class name이 rg_meta인 것을 찾아온다
        for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
            print(counter)
            counter = counter + 1
            print("Total Count:", counter)
            print("Succsessful Count:", succounter)
            print("URL:", json.loads(x.get_attribute('innerHTML'))["ou"])

            # 이미지 url
            img = json.loads(x.get_attribute('innerHTML'))["ou"]

            # 이미지 확장자
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]

            # 구글 이미지를 읽고 저장한다.
            try:
                req = urllib.request.Request(img, headers=header)
                response = urllib.request.urlopen(img)
                raw_img = response.read()
                File = open(os.path.join(self.search_term, str(succounter) + "." + "jpg"), "wb")
                File.write(raw_img)
                File.close()
                succounter = succounter + 1
            except:
                print("can't get img")

        print(succounter, "succesfully downloaded")
        browser.close()