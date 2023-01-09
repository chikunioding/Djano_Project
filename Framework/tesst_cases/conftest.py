from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Django_Project001\driver\chromedriver.exe")
    return driver

