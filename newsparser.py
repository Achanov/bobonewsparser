from siteconfig import site_presets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time
import datetime
import re
import sqlite3
conn = sqlite3.connect('news.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE,
    text TEXT NOT NULL,
    source TEXT NOT NULL,
    date TEXT NOT NULL
);
""")

def initialize_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-minimized")
    options.add_argument("--enable-javascript")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver

def clean_text(text):
    cleaned_text = re.sub(r'[\n\t\xa0]|[^\w\s\d\.,%;:!?\-"\'’‘’“”]', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def navigate_and_parse_site(driver, url, navigation_steps, data_extraction_pattern, source, scroll_depth=None, filter_pattern=None):
    driver.get(url)
    WebDriverWait(driver, random.randint(10,  14)).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    if scroll_depth is not None:
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(scroll_depth):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(random.uniform(0.5,  1.33))
        time.sleep(1)

    href_and_text = {}
    if 'links' in data_extraction_pattern:
        link_elements = driver.find_elements(By.CSS_SELECTOR, data_extraction_pattern['links']['selector'])
        for link_element in link_elements:
            href = link_element.get_attribute('href')
            inner_text = link_element.get_attribute('innerText')
            if href is not None:
                cleaned_text = clean_text(inner_text)
                if filter_pattern is not None and re.match(filter_pattern, href):
                    if cleaned_text and len(cleaned_text) >=   4:
                        if href not in href_and_text:
                            href_and_text[href] = {
                                'url': href,
                                'text': cleaned_text,
                                'source': source,
                                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                            }
                        else:
                            href_and_text[href]['text'] += ' ' + cleaned_text
                    else:
                        continue

    href_and_text_list = list(href_and_text.values())
    return href_and_text_list

def main():
    driver = initialize_webdriver()
    for preset in site_presets:
        href_and_text = navigate_and_parse_site(driver, preset['url'], preset['navigation_steps'], preset['data_extraction_pattern'], preset['source'], preset.get('scroll_depth'), preset.get('filter_pattern'))
        for news_item in href_and_text:
            cursor.execute("""
            INSERT OR IGNORE INTO news (url, text, source, date) VALUES (?, ?, ?, ?)
            """, (news_item['url'], news_item['text'], news_item['source'], news_item['date']))

    conn.commit()
    conn.close()
    driver.quit()

if __name__ == "__main__":
    main()