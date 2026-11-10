import pytest
import allure
from pages.bmi_calculator_page import BmiCalculatorPage

@pytest.fixture(scope="session")
def bmi_page(driver):
    page = BmiCalculatorPage(driver)
    page.open()
    page.select_metric_units()
    return page

@allure.title("Корректный расчет BMI: возраст {age}, вес {weight}кг, рост {height}см")
@pytest.mark.parametrize("age, height, weight, expected_bmi, category", [
    (25, 180, 50, "15.4", "Severe thinness"),
    (30, 175, 68, "22.2", "Normal"),
    (40, 170, 80, "27.7", "Overweight"),
    (35, 165, 90, "33.1", "Obese Class I"),
    (50, 160, 110, "43", "Obese Class III"),
])
def test_bmi_valid_calculation(bmi_page, age, height, weight, expected_bmi, category):
    bmi_page.enter_age(age)\
            .enter_height(height)\
            .enter_weight(weight)\
            .click_calculate()

    result = bmi_page.get_bmi_result()
    assert expected_bmi in result
    assert category in result

@allure.title("Проверка граничных значений возраста: {border_age} лет")
@pytest.mark.parametrize("border_age", [2, 120])
def test_bmi_boundary_values(bmi_page, border_age):
    bmi_page.enter_age(border_age)\
            .enter_height(170)\
            .enter_weight(65)\
            .click_calculate()

    result = bmi_page.get_bmi_result()
    assert "BMI =" in result

@allure.title("Обработка неверного ввода возраста: '{invalid_age}'")
@pytest.mark.parametrize("invalid_age, height, weight", [
    ("abc", 170, 70),
    (-5, 170, 70),
    (150, 170, 70),
])
def test_bmi_invalid_input(bmi_page, invalid_age, height, weight):
    bmi_page.enter_age(invalid_age)\
            .enter_height(height)\
            .enter_weight(weight)\
            .click_calculate()

    error = bmi_page.get_error_message()
    assert len(error) > 0

@allure.title("Сброс формы по кнопке Clear")
def test_clear_button(bmi_page):
    bmi_page.enter_age(45)\
            .enter_height(180)\
            .enter_weight(80)\
            .click_clear()

    current_val = bmi_page.get_age_value()
    assert current_val == "" or current_val != "45"