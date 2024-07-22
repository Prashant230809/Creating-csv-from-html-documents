from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = "laptop"
fileNo = 0

driver = webdriver.Chrome()
for i in range(1, 3):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=LXE7BB7APIB9&qid=1721557412&sprefix=laptop%2Caps%2C1337&ref=sr_pg_2")

    elems = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    print(f"{len(elems)} items found")

    for elem in elems:
        # print(elem.text)
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{fileNo}.html", "w", encoding="utf-8") as f:
            f.write(d)
            fileNo += 1
    time.sleep(2)

driver.close()