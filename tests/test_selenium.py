
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_factorial_webpage():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://127.0.0.1:5000")

        number = driver.find_element(By.ID, "number")
        number.send_keys("5")

        driver.find_element(By.ID, "calculate").click()

        time.sleep(1)

        result = driver.find_element(By.ID, "result")

        assert "120" in result.text

        print("Selenium test passed!")

    finally:
        driver.quit()

