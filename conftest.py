import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from locators import TestLocators
from urls import TestUrl


# Фикстура для запуска Chrome
@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Фикстура для открытия сайта (для Chrome)
@pytest.fixture
def open_chrome_site(chrome_driver):
    def _open_site():
        chrome_driver.get(TestUrl.URL_STELLAR_BURGERS)
    yield _open_site


#функция для случайного выбора имени
@pytest.fixture
def random_name():
    names = ['Иван', "Maria", "123", "1"]
    name = random.choice(names)
    return name


# функция для генерации логинов имя_фамилия_номер когорты_любые 3 цифры@домен
@pytest.fixture
def random_login_generator():
    # Списки возможных имен и фамилий
    first_names = ["Maria", "Julia", "Andrey", "Petr", "Evgeny"]
    last_names = ["Klitschko", "Furkalo", "Brian", "Peterson"]

    # Случайный выбор имени и фамилии из списков
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Генерация номера когорты из двух случайных цифр
    cohort_number = ''.join(str(random.randint(0, 9)) for _ in range(2))

    # Генерация трех случайных цифр
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))

    # Домен почты
    domain = "@yandex.ru"

    # Формирование логина
    login = f"{first_name}{last_name}{cohort_number}{random_digits}{domain}"

    return login


# Функция для генерации случайного пароля
@pytest.fixture
def random_password_generator():
    random_password = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return random_password


# Функция ввода логина, пароля на странице "Вход" + кликанье кнопки "Войти"
@pytest.fixture
def filling_login_form(chrome_driver):
    def _filling_login_form():
        # заполняем поля и нажимаем кнопку "Войти"
        chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_EMAIL).send_keys(TestData.DATA_EMAIL)
        chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_PASSWORD).send_keys(TestData.DATA_PASSWORD)
        chrome_driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
    yield _filling_login_form
