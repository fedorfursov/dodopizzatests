from selenium.webdriver.common.by import By


class MenuLocators:
    PIZZA_CARD = "(//article[contains(@data-testid, 'menu__meta-product')])[{index}]"
    PIZZA_IMAGE = ".//img"
    PIZZA_NAME = "//div[@data-gtm-id='product-title']"
    PIZZA_PRICE = "//div[@class='product-control-price']"
    PIZZA_CHOSE_BUTTON ="//button[@data-testid='product__button']"
    MODAL_WINDOW = "//div[contains(@data-testid, 'product__card')]"
    ADD_TO_CARD_BUTTON_PRICE = "//button[@data-testid='button_add_to_cart']//span[@class='money__value']"

    def get_size_locator(size_label):
        return (By.XPATH, f"//label[@data-testid='menu__pizza_size_{size_label}']")

    def get_pizza_crust(crust_label):
        return (By.XPATH, f"//label[contains(text(), '{crust_label}')]")

