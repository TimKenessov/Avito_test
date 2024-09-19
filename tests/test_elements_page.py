from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.feature("UI Tests")
class TestElementsPage:

    @pytest.mark.filter_by_category_test
    @allure.title("Фильтр по категории — показывает релевантные результаты")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filter_by_category(self, driver):

        with allure.step("Шаг 1. Открыть главную страницу сайта"):
            elements_page = ElementsPage(
                driver,
                "https://makarovartem.github.io/frontend-avito-tech-test-assignment/",
            )
            elements_page.open()

        with allure.step('Шаг 2. Выбрать категорию, например, "strategy"'):
            elements_page.filter_by_category()

        with allure.step(
            '''Шаг 3. Проверить, что выбранный элемент отображается'''
            ):
            element_locator = elements_page.locators.element_category_locator
            selector = element_locator[1]
            expected_title = "strategy"
            assert expected_title in selector

    @pytest.mark.back_to_main_test
    @allure.title(
        """Кнопка «Back to main» — должна перенаправлять на домашнюю страницу
        и отображать основной контент"""
    )
    @allure.severity(allure.severity_level.MINOR)
    def test_return_to_the_main_page(self, driver):

        with allure.step("Шаг 1. Открыть главную страницу сайта"):
            elements_page = ElementsPage(
                driver,
                "https://makarovartem.github.io/frontend-avito-tech-test-assignment/",
            )
            elements_page.open()

        with allure.step('Шаг 2. Выбрать категорию, например, "strategy"'):
            elements_page.filter_by_category()

        with allure.step("Шаг 3. Возвратиться на главную страницу"):
            elements_page.return_to_the_main_page()

        with allure.step("Шаг 4. Проверить, что основной контент отображается"):
            main_content_element = elements_page.element_is_present(
                (By.CLASS_NAME, "ant-divider-inner-text")
            )
            element_text = main_content_element.text
        assert element_text == "Games List Below"

    @pytest.mark.navigate_by_pagination_test
    @allure.title(
        "Пагинация — должна правильно перемещаться по страницам результатов поиска"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_using_pagination(self, driver):

        with allure.step("Шаг 1. Открыть главную страницу сайта"):
            elements_page = ElementsPage(
                driver,
                "https://makarovartem.github.io/frontend-avito-tech-test-assignment/",
            )
            elements_page.open()

        with allure.step('Шаг 2. Выбрать категорию, например, "strategy"'):
            elements_page.filter_by_category()

        with allure.step("Шаг 3. Перейти на следующую страницу с помощью пагинации"):
            elements_page.navigate_using_pagination()

        with allure.step("Шаг 4. Проверить, что номер страницы изменился"):
            element_locator = elements_page.locators.navigation_locator
            selector = element_locator[1]
            expected_page_number = "2"
            assert expected_page_number in selector
