from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://subsidies.qoldau.kz/ru/subsidies/herbicides/pub-apps?Year=2019')


def clic(count):

    for i in range(count):
        #
        driver.delete_all_cookies()
        xpath = '//*[@aria-label="Следующая страница"]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(4)
        html = driver.page_source
        parse_csv(html, i)


def parse_csv(html, i):
    ds = pd.read_html(html)
    df = ds[1]
    df.to_csv(f'data\data_frame{i}.csv', encoding='utf-8', index=False)
    driver.delete_all_cookies()


clic(5)