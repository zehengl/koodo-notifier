from datetime import datetime
import os

import boto3
import rollbar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_my_acct = "https://www.koodomobile.com/my-account"


def test_toodo_notifier():

    username = os.getenv("username")
    password = os.getenv("password")
    access_key = os.getenv("access_key")
    secret_key = os.getenv("secret_key")
    rollbar_key = os.getenv("rollbar_key")

    wait_time = int(os.getenv("wait_time", 10))
    region_name = os.getenv("region_name", "us-east-1")

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)

        assert username
        assert password
        assert access_key
        assert secret_key
        assert rollbar_key

        rollbar.init(rollbar_key)

        driver.get(url_my_acct)

        _username = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "IDToken1"))
        )
        _password = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "IDToken2"))
        )
        _login = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lch-button "))
        )

        _username.clear()
        _password.clear()

        _username.send_keys(username)
        _password.send_keys(password)

        driver.execute_script("arguments[0].click()", _login)

        [phone_number, account_number] = [
            e.text
            for e in driver.find_elements_by_class_name(
                "overview-card-details-sub-title"
            )
        ]

        urls = driver.find_elements_by_class_name("overview-card-link")

        url_usage = urls[0].get_attribute("href")

        driver.get(url_usage)

        usage_cards = [
            e.text for e in driver.find_elements_by_class_name("usage-card-info")
        ]

        message = "\n".join([(" ").join(e.split("\n")[:3]) for e in usage_cards])

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{account_number}\n{message}\nAs of {now}"

        client = boto3.client(
            "sns",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name,
        )

        client.publish(PhoneNumber=f"+1{phone_number}", Message=message)

    except:
        rollbar.report_exc_info()
        assert False

    finally:
        driver.quit()
