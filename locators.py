from selenium.webdriver.common.by import By

class TestLocators:

# Раздел "Личный кабинет". Главная страница
    LOCATOR_PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"

# Кнопка "Войти в аккаунт". Главная страница
    LOCATOR_ACCOUNT_LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"

# Поле "Email". Страница "Вход"
    LOCATOR_FIELD_EMAIL = By.XPATH, "//input[contains(@class,'textfield') and @name='name']"

# "Зарегистрироваться". Страница "Вход"
    LOCATOR_REGISTER = By.XPATH, "//a[@href='/register']"

# Поле "Пароль". Страница "Вход"
    LOCATOR_FIELD_PASSWORD = By.XPATH, "//input[contains(@class,'input__textfield') and @type='password']"

# Кнопка "Войти" Страница "Вход"
    LOCATOR_LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"

# "Восстановить пароль". Страница "Вход"
    LOCATOR_PASSWORD_RECOVERY = By.XPATH, "//a[text()='Восстановить пароль']"

# Поле "Имя". Страница "Регистрация"
    LOCATOR_NAME_REGISTRATION = By.XPATH, "//input[@type='text' and @name='name']"

# Поле "Email". Страница "Регистрация"
    LOCATOR_EMAIL_REGISTRATION = By.XPATH, "(//input[@name='name'])[2]"

# Поле "Пароль". Страница "Регистрация"
    LOCATOR_PASSWORD_REGISTRATION = By.XPATH, "//input[@type='password']"

# Кнопка "Зарегистрироваться". Страница "Регистрация"
    LOCATOR_REGISTRATION_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"

# Сообщение об ошибки "Некорректный пароль". Страница "Регистрация"
    LOCATOR_INCORRECT_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']"

# Поле "Email". Страница "Восстановление пароля"
    LOCATOR_EMAIL_PASSWORD_RECOVERY = By.XPATH, "//input[@type='text' and @name='name']"

# Кнопка "Восстановить". Страница "Восстановление пароля"
    LOCATOR_RECOVER_BUTTON = By.XPATH, "//button[text()='Восстановить']"

# Раздел "Конструктор" в шапке сайта.
    LOCATOR_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"

# Логотип Stellar Burgers в шапке сайта
    LOCATOR_STELLAR_BURGERS_LOGO = By.XPATH, "//*[local-name()='svg']//*[local-name()='path'][1]"

# Кнопка "Выход". Страница "Профиль"
    LOCATOR_EXIT_BUTTON = By.XPATH, "//button[text()='Выход']"

# Поле "Имя". Страница "Профиль"
    LOCATOR_FIELD_NAME = By.XPATH, "//input[@name='Name']"

# Поле Логин. Страница "Профиль"
    LOCATOR_FIELD_LOGIN = By.XPATH, "(//input[contains(@class, 'input__textfield')])[2]"

#Поле Пароль. Страница "Профиль"
    LOCATOR_FIELD_PASSWORD_PROFILE = By.XPATH, By.XPATH, "(//input[contains(@class, 'input__textfield')])[3]"

# Раздел "Булки"
    LOCATOR_BUN_SECTION = By.XPATH, "//span[.='Булки']"

# Флюоресцентная булка
    LOCATOR_FLUORESCENT_BUN = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"

# Раздел "Соусы"
    LOCATOR_SECTION_SAUCES = By.XPATH, "//span[.='Соусы']"

# Соус Spicy-X
    LOCATOR_SPICY_X = By.XPATH, "//a[contains(., 'Соус Spicy-X')]"

# Раздел "Начинки"
    LOCATOR_FILLING_SECTION = By.XPATH, "//span[text()='Начинки']"

#"Говяжий метеорит(отбивная)"
    LOCATOR_BEEF_METEORITE = By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']"

