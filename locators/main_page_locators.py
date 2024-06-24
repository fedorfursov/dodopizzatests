from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_LOGO = (By.XPATH, "//*[local-name()='svg' and @viewBox='0 0 532.32 97.95']") ##Bad locator
    MENU_NAVIGATION_PANEL = (By.XPATH, "(//nav)[1]")
    HEADER_LOGIN_BUTTON = (By.XPATH, "//button[@data-testid='header_login']")
    TOP_NAVIGATION_PANEL = (By.XPATH, "(//div/div/div)[1]")  ##Bad Locator, в идеале использовать testid
    CARD_BUTTON = (By.XPATH, "//button[@data-testid='navigation__cart']")
    STORIES_WIDGET = (By.XPATH, "//section[contains(@id, 'stories_widget')]")
    PROMOTIONS_SECTION = (By.XPATH, "//*[@data-testid='popular_title']/ancestor-or-self::section")
    MENU_CONTAINER = (By.XPATH, "(//main)[1]") ##Bad Locator, в идеале использовать testid
    FIRST_MENU_ITEM = (By.XPATH, "(//article[contains(@data-testid, 'menu__meta-product')])[1]")
    STORIES_IFRAME = (By.XPATH, "//iframe[contains(@id, 'iaswidget3')]")
    MAIN_PAGE_FOOTER = (By.XPATH, "(//div[contains(@class, 'footer')])[1]")
