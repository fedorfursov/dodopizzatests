from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from locators.menu_locators import MenuLocators

from pages.base_page import BasePage


class PizaMenuComponent(BasePage):

    def get_pizza_card(self, index=1):
        pizza_card_locator = (By.XPATH, MenuLocators.PIZZA_CARD.format(index=index))
        if self.is_element_visible_on_page(pizza_card_locator):
            return self.driver.find_element(*pizza_card_locator)
        return None

    def is_pizza_image_visible(self, pizza_card):
        pizza_image_locator = (By.XPATH, MenuLocators.PIZZA_IMAGE)
        return self.is_child_element_visible(pizza_card, pizza_image_locator)

    def is_pizza_name_visible(self, pizza_card):
        pizza_image_locator = (By.XPATH, MenuLocators.PIZZA_NAME)
        return self.is_child_element_visible(pizza_card, pizza_image_locator)

    def is_pizza_price_visible(self, pizza_card):
        pizza_image_locator = (By.XPATH, MenuLocators.PIZZA_PRICE)
        return self.is_child_element_visible(pizza_card, pizza_image_locator)

    def is_pizza_chose_button(self, pizza_card):
        pizza_image_locator = (By.XPATH, MenuLocators.PIZZA_CHOSE_BUTTON)
        return self.is_child_element_visible(pizza_card, pizza_image_locator)


