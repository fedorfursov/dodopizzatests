from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage(object):

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def click(self, by_locator, wait=True):
        try:
            if wait:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
            else:
                self.driver.find_element(*by_locator).click()
        except TimeoutException:
            print(f"Element located by {by_locator} is not clickable after 10 seconds.")
            raise

    def is_element_visible_on_page(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def is_child_element_visible(self, parent_element, child_locator):
        try:
            child_element = parent_element.find_element(*child_locator)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(child_element)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def switch_to_frame(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(by_locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def go_to_page(self, url):
        self.driver.get(url)

    def is_title_matches(self, title):
        return title in self.driver.title

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)



