import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless") # Раскомментируйте при необходимости запуска без GUI
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    # Выставление неявного ожидания в ноль (согласно требованиям)
    driver.implicitly_wait(0)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return "https://parabank.parasoft.com/parabank/register.htm"


@pytest.fixture(scope="function", autouse=True)
def attach_failure_artifacts(request, driver):
    yield
    # Проверка, упал ли тест
    if request.node.rep_call.failed:
        # 1. Скриншот
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )
        
        # 2. Логи браузера (доступны для Chrome)
        try:
            browser_logs = driver.get_log("browser")
            logs_text = "\n".join([str(log) for log in browser_logs])
            allure.attach(
                logs_text,
                name="browser_console_logs",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass

        # 3. Сетевые запросы (Performance Logs, если поддерживается)
        try:
            perf_logs = driver.get_log("performance")
            perf_text = "\n".join([str(log) for log in perf_logs])
            allure.attach(
                perf_text,
                name="network_requests",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)