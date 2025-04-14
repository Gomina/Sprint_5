import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://stellarburgers.nomoreparties.site/"

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
        chrome_driver.get(URL)
        WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/header/nav/a/p"))
        )
    yield _open_site


# Фикстура для запуска Firefox
@pytest.fixture()
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
# Фикстура для открытия сайта (для Firefox)
@pytest.fixture
def open_firefox_site(firefox_driver):
    def _open_site():
        firefox_driver.get(URL)
        WebDriverWait(firefox_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/header/nav/a/p"))
        )
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
        chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(
            "EvgenyFurkalo65893@yandex.ru")
        chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys("465109")
        chrome_driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
    yield _filling_login_form
