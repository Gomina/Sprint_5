import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestRegistration:
    #Успешная регистрация:
    def test_registration(self, chrome_driver, open_chrome_site, random_name, random_login_generator, random_password_generator):
            # открыть сайт, дождаться загрузки
            open_chrome_site()
            # клик кнопку "Личный кабинет"
            chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
            # клик на "Зарегисттрироваться"
            chrome_driver.find_element(*TestLocators.LOCATOR_REGISTER).click()
            # ввод рандомного имени в поле имя
            random_name_here=random_name
            chrome_driver.find_element(*TestLocators.LOCATOR_NAME_REGISTRATION).send_keys(random_name_here)
            # ввод рандомного логина в поле Email
            random_login_generator_here=random_login_generator
            chrome_driver.find_element(*TestLocators.LOCATOR_EMAIL_REGISTRATION).send_keys(
                random_login_generator_here)
            # ввод рандомного пароля в поле "Пароль"
            random_password_generator_here = random_password_generator
            chrome_driver.find_element(*TestLocators.LOCATOR_PASSWORD_REGISTRATION).send_keys(random_password_generator_here)
            # клик кнопки "Зарегистироваться"
            chrome_driver.find_element(*TestLocators.LOCATOR_REGISTRATION_BUTTON).click()
            # заходим в личный кабинет
            WebDriverWait(chrome_driver, 10).until(
                EC.presence_of_element_located(TestLocators.LOCATOR_LOGIN_BUTTON)
            )
            chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_EMAIL).send_keys(random_login_generator_here)
            chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_PASSWORD).send_keys(random_password_generator_here)
            chrome_driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
            # проверяем что в личном кабинете отражено верное имя
            # клик на "Личный кабинет"
            chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
            # Ожидание, пока поле станет доступным для чтения
            WebDriverWait(chrome_driver, 30).until(
                EC.presence_of_element_located(TestLocators.LOCATOR_FIELD_NAME))
            # Нахождение элемента с именем пользователя
            name_field = chrome_driver.find_element(*TestLocators.LOCATOR_FIELD_NAME)
            # Проверка, что в поле отображается правильное имя
            assert name_field.get_attribute('value') == random_name_here


    #Регистрация с некорректным паролем
    def test_registration_bad_password(self, chrome_driver,open_chrome_site, random_name, random_login_generator):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопку "Личный кабинет"
        chrome_driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT_BUTTON).click()
        # клик на "Зарегисттрироваться"
        chrome_driver.find_element(*TestLocators.LOCATOR_REGISTER).click()
        # ввод рандомного имени в поле имя
        chrome_driver.find_element(*TestLocators.LOCATOR_NAME_REGISTRATION).send_keys(random_name)
        # ввод рандомного логина в поле Email
        chrome_driver.find_element(*TestLocators.LOCATOR_EMAIL_REGISTRATION).send_keys(
            random_login_generator)
        # ввод пароля в поле "Пароль"
        chrome_driver.find_element(*TestLocators.LOCATOR_PASSWORD_REGISTRATION).send_keys("FRD")
        # клик кнопки "Зарегистироваться"
        chrome_driver.find_element(*TestLocators.LOCATOR_REGISTRATION_BUTTON).click()
        # ожидание появления ошибки
        WebDriverWait(chrome_driver, 60).until(
            EC.presence_of_element_located(TestLocators.LOCATOR_INCORRECT_PASSWORD)
        )
        # нахождение элемента с сообщением об ошибке
        error_message = chrome_driver.find_element(*TestLocators.LOCATOR_INCORRECT_PASSWORD)
        # проверка, что текст ошибки соответствует ожидаемому
        assert error_message.text == "Некорректный пароль"
