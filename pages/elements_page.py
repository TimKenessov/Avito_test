from pages.base_page import BasePage
from locators.elements_locators import ElementsPageLocators


class ElementsPage(BasePage):
    locators = ElementsPageLocators()

    def filter_by_category(self):
        # Метод, который вызывает отображение раскрывающегося списка
        elements = self.elements_are_present(
            self.locators.filter_category_locator
            )

        # Метод, выбирающий второй элемент(список)
        second_element = elements[1]
        second_element.click()

        """Метод, выбирающий элемент из списка(для выбора других элементов
        списка, поменяйте название категории, перейдя в
        elements_locators.py и измените значение title в локаторе
        element_category_locator)"""
        self.element_is_clickable(
            self.locators.element_category_locator
            ).click()

    def return_to_the_main_page(self):
        # Метод открывающий страницу с игрой
        elements = self.elements_are_present(
            self.locators.game_page_locator
            )

        ''' Выбор элемента на страницу с индексом 1 (для выбора других игр
        можно поменять индекс)'''
        first_element = elements[0]
        first_element.click()

        # Возврат на главную страницу по нажатию кнопки Back to main
        self.element_is_clickable(self.locators.button_locator).click()

    def navigate_using_pagination(self):
        """Переход по страницам результата поиска с помощью пагинации
        (для выбора других страниц поменяйте значение в 'ant-pagination-item'
        локатора navigation_locator)"""
        self.element_is_clickable(self.locators.navigation_locator).click()
