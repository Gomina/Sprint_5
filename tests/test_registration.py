from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    #Успешная регистрация:
    def test_registration(self, chrome_driver, open_chrome_site, random_name, random_login_generator, random_password_generator):
            # открыть сайт, дождаться загрузки
            open_chrome_site()
            # клик кнопку "Личный кабинет"
            chrome_driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
            # клик на "Зарегисттрироваться"
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a").click()
            # ввод рандомного имени в поле имя
            random_name_here=random_name
            chrome_driver.find_element(By.XPATH, "//*[@id='root']//input[@name='name']").send_keys(random_name_here)
            # ввод рандомного логина в поле Email
            random_login_generator_here=random_login_generator
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(
                random_login_generator_here)
            # ввод рандомного пароля в поле "Пароль"
            random_password_generator_here = random_password_generator
            chrome_driver.find_element(By.XPATH, "//*[@id='root']//input[@name='Пароль']").send_keys(random_password_generator_here)
            # клик кнопки "Зарегистироваться"
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()
            # заходим в личный кабинет
            WebDriverWait(chrome_driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Войти')]"))
            )
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(random_login_generator_here)
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(random_password_generator_here)
            chrome_driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
            # проверяем что в личном кабинете отражено верное имя
            # клик на "Личный кабинет"
            chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()
            # Ожидание, пока поле станет доступным для чтения
            WebDriverWait(chrome_driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#root>div>main>div>div>div>ul>li:nth-child(1)>div>div>input")))
            # Нахождение элемента с именем пользователя
            name_field = chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[1]/div/div/input")
            # Проверка, что в поле отображается правильное имя
            assert name_field.get_attribute('value') == random_name_here
            # выход из браузера
            chrome_driver.quit()

    #Регистрация с неверным паролем
    def test_registration_bad_password(self, chrome_driver,open_chrome_site, random_name, random_login_generator):
        # открыть сайт, дождаться загрузки
        open_chrome_site()
        # клик кнопку "Личный кабинет"
        chrome_driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        # клик на "Зарегисттрироваться"
        chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a").click()
        # ввод рандомного имени в поле имя
        chrome_driver.find_element(By.XPATH, "//*[@id='root']//input[@name='name']").send_keys(random_name)
        # ввод рандомного логина в поле Email
        chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(
            random_login_generator)
        # ввод рандомного пароля в поле "Пароль"
        chrome_driver.find_element(By.XPATH, "//*[@id='root']//input[@name='Пароль']").send_keys("FRD")
        # клик кнопки "Зарегистироваться"
        chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()
        # ожидание появления ошибки
        WebDriverWait(chrome_driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"))
        )
        # нахождение элемента с сообщением об ошибке
        error_message = chrome_driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p")
        # проверка, что текст ошибки соответствует ожидаемому
        assert error_message.text == "Некорректный пароль"
        # выход из браузера
        chrome_driver.quit()