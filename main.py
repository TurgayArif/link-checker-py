import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


broken_status_codes = [404, 500, 502, 503, 504]
BASE_URL = 'DESTINATION_URL'


# Create a new instance of the Chrome driver
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.timeouts.implicit_wait = 10
    return driver


def open_url(url):
    driver = init_driver()
    driver.get(url)
    return driver


def get_anchors(driver, url):
    driver.get(url)
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    print(f'Found {len(anchors)} anchor tags on the page.')
    return anchors


def check_for_duplicates(anchors):
    anchor_list = []
    for anchor in anchors:
        if anchor.get_attribute('href') not in anchor_list and anchor.get_attribute('href') is not None:
            anchor_list.append(anchor.get_attribute('href'))
        else:
            print(f'Duplicate link found: {anchor.get_attribute("href")}')
    return anchor_list


def get_response_code(url):
    response = requests.get(url)
    print(f'Response code for {url} is {response.status_code} ')
    return response.status_code


def visit_url(url):
    open_url(url)
    print(f'Visiting: {url}...')


def get_page_source(driver):
    return driver.page_source


def tear_down(driver):
    driver.quit()


def main():
    driver = init_driver()
    anchors = get_anchors(driver, BASE_URL)
    anchors = check_for_duplicates(anchors)
    print(f'Found {len(anchors)} unique anchor tags on the page.')
    i = 1
    broken_links = []
    for anchor in anchors:
        print(f'{i}.Visiting: {anchor}...')
        i += 1
        visit_url(anchor)
        time.sleep(2)
        page_source = get_page_source(driver)
        assert page_source is not None
        response_code = get_response_code(anchor)
        if response_code in broken_status_codes:
            broken_links.append(anchor)
            print(f'Page {anchor} is broken. Status code is: {response_code}')
        if response_code == 403:
            broken_links.append(anchor)
            print(f'Page {anchor} is forbidden. Status code is: {response_code}')
        if response_code == 200:
            print(f'Page {anchor} is live.')

    print(f'Found {len(broken_links)} broken links.')
    if len(broken_links) > 0:
        print('Broken links:')
        for link in broken_links:
            print(link)
    tear_down(driver)


if __name__ == '__main__':
    main()
