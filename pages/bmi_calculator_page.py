import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BmiCalculatorPage(BasePage):
    URL = "https://www.calculator.net/bmi-calculator.html"

    TAB_METRIC = (By.XPATH, "//a[contains(text(), 'Metric Units')]")
    AGE_INPUT = (By.ID, "cage")
    HEIGHT_INPUT = (By.ID, "cheightmeter")
    WEIGHT_INPUT = (By.ID, "ckg")
    CALCULATE_BTN = (By.XPATH, "//input[@value='Calculate']")
    CLEAR_BTN = (By.XPATH, "//input[@value='Clear']")
    RESULT_TEXT = (By.CSS_SELECTOR, "div.bigtext")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "font[color='red']")

    @allure.step("Открыть страницу калькулятора BMI")
    def open(self):
        self.open_url(self.URL)
        return self

    @allure.step("Выбрать метрическую систему (Metric Units)")
    def select_metric_units(self):
        self.click(self.TAB_METRIC)
        return self

    @allure.step("Ввести возраст: {age}")
    def enter_age(self, age):
        self.type_text(self.AGE_INPUT, age)
        return self

    @allure.step("Ввести рост: {height}")
    def enter_height(self, height):
        self.type_text(self.HEIGHT_INPUT, height)
        return self

    @allure.step("Ввести вес: {weight}")
    def enter_weight(self, weight):
        self.type_text(self.WEIGHT_INPUT, weight)
        return self

    @allure.step("Нажать кнопку 'Calculate'")
    def click_calculate(self):
        self.click(self.CALCULATE_BTN)
        return self

    @allure.step("Нажать кнопку 'Clear'")
    def click_clear(self):
        self.click(self.CLEAR_BTN)
        return self

    @allure.step("Получить результат BMI")
    def get_bmi_result(self) -> str:
        return self.get_text(self.RESULT_TEXT)

    @allure.step("Получить текст ошибки")
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_CONTAINER)

    @allure.step("Получить текущее значение поля возраста")
    def get_age_value(self) -> str:
        return self.find(self.AGE_INPUT).get_attribute("value")