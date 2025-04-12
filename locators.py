from selenium.webdriver.common.by import By

class TestLocators:

# Раздел "Личный кабинет". Главная страница
    LOCATOR_PERSONAL_ACCOUNT_BUTTON_1 = By.XPATH, "//*[@id='root']/div/header/nav/a/p"
    LOCATOR_PERSONAL_ACCOUNT_BUTTON_2 = By.XPATH, "//p[contains(text(), 'Личный Кабинет'"

# Кнопка "Войти в аккаунт". Главная страница
    LOCATOR_ACCOUNT_LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"

# Поле "Email". Страница "Вход"
    LOCATOR_FIELD_EMAIL = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"

# "Зарегистрироваться". Страница "Вход"
    LOCATOR_REGISTER =By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a"

# Поле "Пароль". Страница "Вход"
    LOCATOR_PASSWORD_FIELD = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"

# Кнопка "Войти" Страница "Вход"
    LOCATOR_LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"

# "Восстановить пароль". Страница "Вход"
    LOCATOR_PASSWORD_RECOVERY = By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a"

# Поле "Имя". Страница "Регистрация"
    LOCATOR_NAME_REGISTRATION = By.XPATH, "//*[@id='root']//input[@name='name']"

# Поле "Email". Страница "Регистрация"
    LOCATOR_EMAIL_REGISTRATION = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"

# Поле "Пароль". Страница "Регистрация"
    LOCATOR_PASSWORD_REGISTRATION = By.XPATH, "//*[@id='root']//input[@name='Пароль']"

# Кнопка "Зарегистрироваться". Страница "Регистрация"
    LOCATOR_REGISTRATION_BUTTON = By.XPATH, "//*[@id='root']/div/main/div/form/button"

# Сообщение об ошибки "Некорректный пароль". Страница "Регистрация"
    LOCATOR_INCORRECT_PASSWORD = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"

# Поле "Email". Страница "Восстановление пароля"
    LOCATOR_EMAIL_PASSWORD_RECOVERY = By.XPATH, "//*[@id='root']/div/main/div/form/fieldset/div/div/input"

# Кнопка "Восстановить". Страница "Восстановление пароля"
    LOCATOR_RECOVER_BUTTON = By.XPATH, "//*[@id='root']/div/main/div/form/button"

# Раздел "Конструктор" в шапке сайта.
    LOCATOR_CONSTRUCTOR = By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p"

# Логотип Stellar Burgers в шапке сайта
    LOCATOR_STELLAR_BURGERS_LOGO = By.CSS_SELECTOR, "#root header nav div a svg"

# Кнопка "Выход". Страница "Профиль"
    LOCATOR_EXIT_BUTTON = By.XPATH, "//*[@id='root']//main//nav//ul//li[3]//button"
# Окно "Имя". Страница "Профиль"
    LOCATOR_FIELD_NAME = By.CSS_SELECTOR,"#root>div>main>div>div>div>ul>li:nth-child(1)>div>div>input"

# Раздел "Булки"
    LOCATOR_BUN_SECTION = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span"

# Флюоресцентная булка
    LOCATOR_FLUORESCENT_BUN = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/img"

# Раздел "Соусы"
    LOCATOR_SECTION_SAUCES = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]"

# Соус Spicy-X
    LOCATOR_SPICY_X = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]"

# Раздел "Начинки"
    LOCATOR_FILLING_SECTION =By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span"

#"Говяжий метеорит(отбивная)"
LOCATOR_BEEF_METEORITE_ = By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[3]/a[2]/img"

