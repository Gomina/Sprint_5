import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestData

class TestAccount:

    # Вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_account_button_login_in_account(self, chrome_driver, open_chrome_site, filling_login_form, ):
        open_chrome_site()
        # ожидание загрузки главной страницы
        WebDriverWait(chrome_driver, 20).until(
            EC.visibility_of_element_located(TestLocators.LOCATOR_ACCOUNT_LOGIN_BUTTON)
        )
        # открыть окно "Вход", кликая на кнопку "Войти в аккаунт"
        chrome_driver.find_element(*TestLocators.LOCATOR_ACCOUNT_LOGIN_BUTTON).click()
        # заполнить поля и нажать кнопку "Войти"
        filling_login_form()
        # проверка, что в поле Имя, указано имя "Евгения"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # Дождаться появления элемента
        WebDriverWait(chrome_driver, 20).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_FIELD_NAME)
        )
        name_field = chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_NAME)
        # Проверяем, что значение поля "Имя" равно "Евгения"
        assert name_field.get_attribute('value') == TestData.DATA_NAME


    # Вход через кнопку «Личный кабинет»
    def test_login_account_button_personal_account(self, chrome_driver, open_chrome_site, filling_login_form):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик на кнопку "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # заполнение полей и клик кнопку "Войти"
        filling_login_form()
        # проверка, что в поле Имя, указано имя "Евгения"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # Ожидание, пока поле станет доступным для чтения
        WebDriverWait(chrome_driver, 20).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_FIELD_NAME))
        name_field = chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_NAME)
        # Проверяем, что значение поля "Имя" равно "Евгения"
        assert name_field.get_attribute('value') == TestData.DATA_NAME


    # Вход через кнопку в форме регистрации
    def test_login_account_registration_form(self, chrome_driver, open_chrome_site, random_name,random_login_generator, random_password_generator):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопку "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # клик на "Зарегистрироваться"
        chrome_driver.find_element(*TestLocators.LOCATOR_REGISTER).click()
        # ввод рандомного имени в поле имя
        random_name_here = random_name
        chrome_driver.find_element(*TestLocators.LOCATOR_NAME_REGISTRATION).send_keys(random_name_here)
        # ввод рандомного логина в поле Email
        random_login_generator_here = random_login_generator
        chrome_driver.find_element(*TestLocators.LOCATOR_EMAIL_REGISTRATION).send_keys(
            random_login_generator_here)
        # ввод рандомного пароля в поле "Пароль"
        random_password_generator_here = random_password_generator
        chrome_driver.find_element(*TestLocators.LOCATOR_PASSWORD_REGISTRATION).send_keys(
            random_password_generator_here)
        # клик кнопки "Зарегистироваться"
        chrome_driver.find_element(*TestLocators.LOCATOR_REGISTRATION_BUTTON).click()
        # заходим в личный кабинет
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_LOGIN_BUTTON)
        )
        chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_EMAIL).send_keys(
            random_login_generator_here)
        chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_PASSWORD).send_keys(
            random_password_generator_here)
        chrome_driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
        # проверяем что в личном кабинете отражено верное имя
        # клик на "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # ожидание, пока поле станет доступным для чтения
        WebDriverWait(chrome_driver, 30).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_FIELD_NAME)
        )
        # нахождение элемента с именем пользователя
        name_field = chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_NAME)
        # проверка, что в поле отображается правильное имя
        assert name_field.get_attribute('value') == random_name_here


        # Вход через кнопку в форме восстановления пароля
    def test_login_account_password_recovery(self, chrome_driver, open_chrome_site, filling_login_form):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # клик "Восстановить пароль"
        chrome_driver.find_element(*TestLocators.LOCATOR_PASSWORD_RECOVERY).click()
        # в поле Email ввод адреса почты
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_EMAIL_PASSWORD_RECOVERY)
        ).send_keys(TestData.DATA_EMAIL)
        # клик кнопки "Восстановить"
        chrome_driver.find_element(*TestLocators. LOCATOR_RECOVER_BUTTON).click()
        # проверка, что открылось окно "Восстановление пароля" - URL "...reset-password"
        WebDriverWait(chrome_driver, 5).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/reset-password")
        )
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/reset-password"
        assert current_url == expected_url


    #Переход в личный кабинет
    def test_go_to_personal_account(self, chrome_driver, open_chrome_site, filling_login_form):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # заполнение полей и нажатие кнопки "Войти"
        filling_login_form()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # Ожидание, пока поле станет доступным для чтения
        WebDriverWait(chrome_driver, 30).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_FIELD_NAME)
        )
        name_field = chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_NAME)
        # Проверяем, что значение поля "Имя" равно "Евгения"
        assert name_field.get_attribute('value') == TestData.DATA_NAME


    # Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_from_personal_account_button_constructor(self, chrome_driver, open_chrome_site, filling_login_form):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # заполнение полей и нажатие кнопки "Войти"
        filling_login_form()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # переход в конструктор по клику на "Конструктор"
        chrome_driver.find_element(*TestLocators.LOCATOR_CONSTRUCTOR).click()
        # проверка, что открылась главная страница
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url


    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_from_personal_account_Stellar_Burgers_logo(self, chrome_driver, open_chrome_site, filling_login_form):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # заполнение полей и клик кнопки "Войти"
        filling_login_form()
        # клик кнопки "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # переход в конструктор по клику на логотип Stellar Burgers
        chrome_driver.find_element(*TestLocators.LOCATOR_STELLAR_BURGERS_LOGO).click()
        # проверка, что открылась главная страница
        current_url = chrome_driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url


    # Выход по кнопке «Выйти» в личном кабинете.
    def test_exit_from_personal_account(self, chrome_driver, open_chrome_site, filling_login_form):
            # открыть сайт
            open_chrome_site()
            # клик кнопки "Личный кабинет"
            chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
            # заполнение полей и клик кнопки "Войти"
            filling_login_form()
            # клик кнопки "Личный кабинет"
            chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
            # ожидание загрузки и клик кнопки "Выход"
            WebDriverWait(chrome_driver, 10).until(
                EC.presence_of_element_located(TestLocators.LOCATOR_EXIT_BUTTON)
            ).click()
            WebDriverWait(chrome_driver, 5).until(
                EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
            )
            current_url = chrome_driver.current_url
            expected_url = "https://stellarburgers.nomoreparties.site/login"
            assert current_url == expected_url
