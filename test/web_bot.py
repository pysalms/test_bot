import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mozilla.org/"
#url = "https://www.mozilla.org/en-US/firefox/accounts/"
title = "Internet for people"


@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = wait(driver, 10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    # always quit driver
    driver.quit()


def test_web_link(webFix):
    webFix.find_element("link text", "Learn more").click()
    title = webFix.title
    assert 'Firefox' in title


def test_web_links(webFix):
    links = webFix.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        #print(href)
        # assert 'cnbc.com' in href or 'bbc.com' in href or 'mozilla' in href or 'firefox' in href or 'buzzfeed' in href or 'getpocket' in href or 'thenextweb' in href
        assert 'mozilla' in href or 'firefox' in href or 'getpocket' in href or 'spotify' in href or 'youtu.be' in href
def test_account_form(webFix):
    webFix.find_element(By.ID, "fxa-learn-secondary").click()


    text_input = webFix.find_element(By.ID, "fxa-email-field")
    text_input.send_keys('pytest.auto@gmail.com')
    #webFix.find_element(By.ID, 'privacy').click()
    webFix.find_element(By.ID, 'fxa-email-form-submit').click()
    prefill_email = 'none'
    try:
        element = wait(webFix, 3).until(EC.title_contains('Set your password'))
        prefill_email= webFix.find_elements(By.ID, 'prefillEmail') [0].get_attribute("textContent")
    except Exception as ex:
        print(ex)
    assert 'pytest.auto@gmail.com' in prefill_email