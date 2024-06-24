from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.menu_locators import MenuLocators
from pages.base_page import BasePage


class PizzaModalComponent(BasePage):

    def open_modal_window(self, pizza_card):
        self.click(pizza_card)
        modal_locator = (By.XPATH, MenuLocators.MODAL_WINDOW)
        return self.is_element_visible_on_page(modal_locator)

    def select_pizza_size(self, size_label):
        size_input_locator = MenuLocators.get_size_locator(size_label)
        size_input_element = self.driver.find_element(*size_input_locator)
        self.click(size_input_element)

    def get_pizza_data_size(self, size_value):
        size_locator = (By.XPATH, f"//div[@data-size='{size_value}']")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(size_locator)
        )
        size_element = self.driver.find_element(*size_locator)
        return size_element.get_attribute("data-size")

    def get_pizza_diameter(self, diameter_value):
        diameter_locator = (By.XPATH, f"//span[contains(text(), '{diameter_value}')]")
        self.is_element_visible_on_page(diameter_locator)
        diameter_element = self.driver.find_element(*diameter_locator)
        full_text = diameter_element.text
        # Извлечение соответствующего фрагмента из текста
        diameter_text = diameter_value if diameter_value in full_text else None
        return diameter_value if diameter_text else None

    def select_pizza_crust(self, crust_label):
        pizza_crust_locator = (By.XPATH, MenuLocators.get_pizza_crust(crust_label))
        self.is_element_visible_on_page(pizza_crust_locator)
        crust_element = self.driver.find_element(*pizza_crust_locator)
        self.click(crust_element)

    def is_crust_option_selecteble(self, crust_label):
        pizza_crust_locator = MenuLocators.get_pizza_crust(crust_label)  # Возвращает корректный локатор
        try:
            self.is_element_visible_on_page(pizza_crust_locator)
            crust_element = self.driver.find_element(*pizza_crust_locator)

            is_disabled = crust_element.get_attribute("data-disabled") == "true"

            return not is_disabled
        except NoSuchElementException:
            return False

    def get_cart_button_price(self):
        card_button = (By.XPATH, MenuLocators.ADD_TO_CARD_BUTTON_PRICE)
        self.is_element_visible_on_page(card_button)
        price = self.driver.find_element(*card_button)
        return price.text

    def select_additional_ingredient(self, ingredient_name):
        ingredient_card = (By.XPATH, f"//button[@type='button' and .//picture[@alt='{ingredient_name}']]")
        self.is_element_visible_on_page(ingredient_card)
        ingredient_button = self.driver.find_element(*ingredient_card)
        self.click(ingredient_button)

    def is_ingredient_selected(self, ingredient_name):
        ingredient_card = (By.XPATH, f"//button[@type='button' and .//picture[@alt='{ingredient_name}']]")
        self.is_element_visible_on_page(ingredient_card)
        ingredient_button = self.driver.find_element(*ingredient_card)

        is_selected = ingredient_button.get_attribute("data-selected") == "true"
        if is_selected:
            return True
        else:
            return False
