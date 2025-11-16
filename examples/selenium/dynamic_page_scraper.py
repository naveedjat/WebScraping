from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
driver.get("https://quotes.toscrape.com/js/")  # JavaScript-rendered page

time.sleep(2)  # Wait for the page to load

quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

for q, a in zip(quotes, authors):
    print(f"{q.text} — {a.text}")

driver.quit()
