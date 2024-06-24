from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import config


# Тесты доступности главной страницы

def test_main_page_is_accessible(driver):
    main_page = MainPage(driver)
    main_page.go_to_page(config.HOME_PAGE_URL)
    assert main_page.is_title_matches(main_page.MAIN_PAGE_TITLE), "Main page title doesnt match. "


def test_key_elements_are_visible(driver):
    main_page = MainPage(driver)
    main_page.go_to_page(config.HOME_PAGE_URL)
    assert main_page.is_element_visible_on_page(MainPageLocators.HEADER_LOGO), "Header logo is not visible"
    assert main_page.is_element_visible_on_page(
        MainPageLocators.TOP_NAVIGATION_PANEL), "Top navigation panel is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.STORIES_WIDGET), "Stories widget is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.HEADER_LOGIN_BUTTON), "Login button is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.CARD_BUTTON), "Card button is not visible"
    assert main_page.is_element_visible_on_page(
        MainPageLocators.MENU_NAVIGATION_PANEL), "Navigation menu panel is not visible"
    assert main_page.is_element_visible_on_page(
        MainPageLocators.PROMOTIONS_SECTION), "Promotions section is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.MENU_CONTAINER), "Menu container is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.FIRST_MENU_ITEM), "First menu item is not visible"
    assert main_page.is_element_visible_on_page(MainPageLocators.MAIN_PAGE_FOOTER), "Footer is not visible"
