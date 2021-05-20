import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_button_add_to_basket(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert button.is_displayed()
