import random
import string
import allure
from pages.registration_page import RegistrationPage


def generate_random_username():
    return "user_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


@allure.feature("Регистрация пользователя")
class TestRegistration:

    @allure.story("Позитивный тест регистрации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self, driver, base_url):
        page = RegistrationPage(driver)
        username = generate_random_username()

        page.open(base_url) \
            .set_first_name("Иван") \
            .set_last_name("Иванов") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username(username) \
            .set_password("Password123") \
            .set_confirm_password("Password123") \
            .click_register()

        success_text = page.get_success_message()
        assert "Your account was created successfully" in success_text

    @allure.story("Негативный тест: Пустое поле Имя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_first_name(self, driver, base_url):
        page = RegistrationPage(driver)
        username = generate_random_username()

        page.open(base_url) \
            .set_first_name("") \
            .set_last_name("Иванов") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username(username) \
            .set_password("Password123") \
            .set_confirm_password("Password123") \
            .click_register()

        error_text = page.get_first_name_error()
        assert "First name is required." in error_text

    @allure.story("Негативный тест: Пустое поле Фамилия")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_last_name(self, driver, base_url):
        page = RegistrationPage(driver)
        username = generate_random_username()

        page.open(base_url) \
            .set_first_name("Иван") \
            .set_last_name("") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username(username) \
            .set_password("Password123") \
            .set_confirm_password("Password123") \
            .click_register()

        error_text = page.get_last_name_error()
        assert "Last name is required." in error_text

    @allure.story("Негативный тест: Пароли не совпадают")
    @allure.severity(allure.severity_level.NORMAL)
    def test_passwords_do_not_match(self, driver, base_url):
        page = RegistrationPage(driver)
        username = generate_random_username()

        page.open(base_url) \
            .set_first_name("Иван") \
            .set_last_name("Иванов") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username(username) \
            .set_password("Password123") \
            .set_confirm_password("DifferentPassword") \
            .click_register()

        error_text = page.get_confirm_password_error()
        assert "Passwords did not match." in error_text

    @allure.story("Негативный тест: Пустое поле Пароль")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_password(self, driver, base_url):
        page = RegistrationPage(driver)
        username = generate_random_username()

        page.open(base_url) \
            .set_first_name("Иван") \
            .set_last_name("Иванов") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username(username) \
            .set_password("") \
            .set_confirm_password("Password123") \
            .click_register()

        error_text = page.get_password_error()
        assert "Password is required." in error_text

    @allure.story("Негативный тест: Пустое поле Username")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_username(self, driver, base_url):
        page = RegistrationPage(driver)

        page.open(base_url) \
            .set_first_name("Иван") \
            .set_last_name("Иванов") \
            .set_address("Ленина 1") \
            .set_city("Москва") \
            .set_state("Московская") \
            .set_zip_code("123456") \
            .set_phone("89001234567") \
            .set_ssn("111-22-333") \
            .set_username("") \
            .set_password("Password123") \
            .set_confirm_password("Password123") \
            .click_register()

        error_text = page.get_username_error()
        assert "Username is required." in error_text