from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators(object):
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")