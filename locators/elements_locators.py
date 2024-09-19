from selenium.webdriver.common.by import By


class ElementsPageLocators:
    filter_category_locator = (By.CSS_SELECTOR, "div.ant-select")
    element_category_locator = (By.CSS_SELECTOR, "div[title='strategy']")
    game_page_locator = (By.CSS_SELECTOR, "div._title_vlg32_45")
    button_locator = (By.CLASS_NAME, "ant-btn")
    navigation_locator = (By.CLASS_NAME, "ant-pagination-item-2")
