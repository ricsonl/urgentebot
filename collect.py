from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import json

def get_news():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://g1.globo.com/"
    driver.get(url)

    print('Coletando manchetes...')
    try:
        for i in range(0, 500):
                time.sleep(0.3)
                xpath = (By.XPATH,'//*[@id="feed-placeholder"]/div/div/div[3]/a')
                driver.execute_script("arguments[0].click();window.scrollTo(0, document.body.scrollHeight);",
                                    WebDriverWait(driver, 30,
                                                    ignored_exceptions=(NoSuchElementException,
                                                                        StaleElementReferenceException,)
                                                    ).until(EC.element_to_be_clickable(xpath)))
    except TimeoutException:
        raise TimeoutError("timeout")

    news = []
    newsElem = driver.find_elements_by_xpath('//*/div/div[2]/div/a')

    for n in newsElem:
        txt = n.text
        if(txt != ''):
            news.append(txt)
    print(f"{len(news)} manchetes obtidas (raw_news.json)")
    return news

def main():
    news = get_news()
    with open('raw_news.json', 'w', encoding='utf8') as outfile:
        json.dump(news, outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()