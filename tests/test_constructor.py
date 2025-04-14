
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


class TestConstructor:

    # переход к разделу "Булки" осуществляется
    def test_go_to_section_buns(self, chrome_driver, open_chrome_site):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # кликнуть на раздел "Соусы"
        chrome_driver.find_element(*TestLocators.LOCATOR_SECTION_SAUCES).click()
        # кликнуть на раздел "Булки"
        chrome_driver.find_element(*TestLocators.LOCATOR_BUN_SECTION).click()
        # проверяем, что элемент "Флюоресцентная булка" виден на странице
        element_visible = WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located(TestLocators.LOCATOR_FLUORESCENT_BUN)
        )
        # утверждение, что элемент найден и виден
        assert element_visible
        # выход из браузера
        chrome_driver.quit()

    # переход к разделу «Соусы» осуществляется
    def test_go_to_section_sauces(self, chrome_driver, open_chrome_site):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # кликнуть на раздел "Соусы"
        chrome_driver.find_element(*TestLocators.LOCATOR_SECTION_SAUCES).click()
        # проверяем, что элемент "Соус Spicy-X" виден на странице
        element_visible = WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located(TestLocators.LOCATOR_SPICY_X)
        )
        # утверждение, что элемент найден и виден
        assert element_visible
        # выход из браузера
        chrome_driver.quit()

    # переход к разделу «Начинки» осуществляется
    def test_go_to_section_fillings(self, chrome_driver, open_chrome_site):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # кликнуть на раздел "Начинки"
        chrome_driver.find_element(*TestLocators.LOCATOR_FILLING_SECTION).click()
        # проверяем, что элемент "Говяжий метеорит(отбивная)" виден на странице
        element_visible = WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located(TestLocators.LOCATOR_BEEF_METEORITE)
        )
        # утверждение, что элемент найден и виден
        assert element_visible
        # выход из браузера
        chrome_driver.quit()