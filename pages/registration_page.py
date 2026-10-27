import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    # Локаторы элементов страницы регистрации ParaBank
    FIRST_NAME_INPUT = (By.ID, "customer.firstName")
    LAST_NAME_INPUT = (By.ID, "customer.lastName")  # <--- Исправлено здесь
    ADDRESS_INPUT = (By.ID, "customer.address.street")
    CITY_INPUT = (By.ID, "customer.address.city")
    STATE_INPUT = (By.ID, "customer.address.state")
    ZIP_INPUT = (By.ID, "customer.address.zipCode")
    PHONE_INPUT = (By.ID, "customer.phoneNumber")
    SSN_INPUT = (By.ID, "customer.ssn")
    USERNAME_INPUT = (By.ID, "customer.username")
    PASSWORD_INPUT = (By.ID, "customer.password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")
    
    # Ошибки валидации полей
    FIRST_NAME_ERROR = (By.ID, "customer.firstName.errors")
    LAST_NAME_ERROR = (By.ID, "customer.lastName.errors")  # <--- И исправлено здесь
    ADDRESS_ERROR = (By.ID, "customer.address.street.errors")
    CITY_ERROR = (By.ID, "customer.address.city.errors")
    STATE_ERROR = (By.ID, "customer.address.state.errors")
    ZIP_ERROR = (By.ID, "customer.address.zipCode.errors")
    SSN_ERROR = (By.ID, "customer.ssn.errors")
    USERNAME_ERROR = (By.ID, "customer.username.errors")
    PASSWORD_ERROR = (By.ID, "customer.password.errors")
    CONFIRM_PASSWORD_ERROR = (By.ID, "repeatedPassword.errors")
    
    SUCCESS_REGISTRATION_MESSAGE = (By.XPATH, "//div[@id='rightPanel']/p")

    @allure.step("Заполнить имя: {first_name}")
    def set_first_name(self, first_name):
        return self.fill(self.FIRST_NAME_INPUT, first_name)

    @allure.step("Заполнить фамилию: {last_name}")
    def set_last_name(self, last_name):
        return self.fill(self.LAST_NAME_INPUT, last_name)

    @allure.step("Заполнить адрес: {address}")
    def set_address(self, address):
        return self.fill(self.ADDRESS_INPUT, address)

    @allure.step("Заполнить город: {city}")
    def set_city(self, city):
        return self.fill(self.CITY_INPUT, city)

    @allure.step("Заполнить штат: {state}")
    def set_state(self, state):
        return self.fill(self.STATE_INPUT, state)

    @allure.step("Заполнить почтовый индекс: {zip_code}")
    def set_zip_code(self, zip_code):
        return self.fill(self.ZIP_INPUT, zip_code)

    @allure.step("Заполнить телефон: {phone}")
    def set_phone(self, phone):
        return self.fill(self.PHONE_INPUT, phone)

    @allure.step("Заполнить SSN: {ssn}")
    def set_ssn(self, ssn):
        return self.fill(self.SSN_INPUT, ssn)

    @allure.step("Заполнить имя пользователя: {username}")
    def set_username(self, username):
        return self.fill(self.USERNAME_INPUT, username)

    @allure.step("Заполнить пароль: {password}")
    def set_password(self, password):
        return self.fill(self.PASSWORD_INPUT, password)

    @allure.step("Подтвердить пароль: {confirm_password}")
    def set_confirm_password(self, confirm_password):
        return self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    @allure.step("Нажать кнопку 'Register'")
    def click_register(self):
        self.click(self.REGISTER_BUTTON)
        return self

    @allure.step("Получить текст успешной регистрации")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_REGISTRATION_MESSAGE)

    @allure.step("Получить текст ошибки для поля Имя")
    def get_first_name_error(self):
        return self.get_text(self.FIRST_NAME_ERROR)

    @allure.step("Получить текст ошибки для поля Фамилия")
    def get_last_name_error(self):
        return self.get_text(self.LAST_NAME_ERROR)

    @allure.step("Получить текст ошибки для поля Пароль")
    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)

    @allure.step("Получить текст ошибки для поля Подтверждение пароля")
    def get_confirm_password_error(self):
        return self.get_text(self.CONFIRM_PASSWORD_ERROR)

    @allure.step("Получить текст ошибки для поля Username")
    def get_username_error(self):
        return self.get_text(self.USERNAME_ERROR)