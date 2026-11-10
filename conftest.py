import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# scope="session" - браузер откроется 1 раз на все тесты
@pytest.fixture(scope="session")
def driver(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")  # Запуск в фоне без окна браузера
    options.add_argument("--disable-search-engine-choice-screen")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Из-за scope="session" драйвер лежит в другом месте
        driver = item.funcargs.get("driver", None)
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"\n[Allure] Не удалось сделать скриншот: {e}")