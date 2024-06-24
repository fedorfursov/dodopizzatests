from pages.components.menu_component import MenuComponent
from pages.components.pizza_menu_component import PizaMenuComponent
import config
from pages.components.pizza_modal_component import PizzaModalComponent
import utils


# Тесты для взаимодействия с меню

def test_pizza_card_visibility(driver):
    menu_component = MenuComponent(driver)
    menu_component.go_to_page(config.HOME_PAGE_URL)
    pizza_menu_component = PizaMenuComponent(driver)
    pizza_card = pizza_menu_component.get_pizza_card(index=1)
    assert pizza_card is not None, "The pizza card should be present on the page."
    assert pizza_menu_component.is_pizza_image_visible(pizza_card), "The pizza image should be visible on the card."
    assert pizza_menu_component.is_pizza_name_visible(pizza_card), "The pizza name should be visible on the card."
    assert pizza_menu_component.is_pizza_price_visible(pizza_card), "The pizza price should be visible on the card."
    assert pizza_menu_component.is_pizza_chose_button(
        pizza_card), "The pizza chose button should be visible on the card."


def test_is_modal_window_visible(driver):
    menu_component = MenuComponent(driver)
    menu_component.go_to_page(config.HOME_PAGE_URL)

    pizza_menu_component = PizaMenuComponent(driver)
    pizza_card = pizza_menu_component.get_pizza_card(index=1)

    pizza_modal_component = PizzaModalComponent(driver)
    modal_opened = pizza_modal_component.open_modal_window(pizza_card)

    assert modal_opened, "The modal window should be visible after clicking the pizza card."


def test_pizza_size_changes_in_modal_window(driver):
    menu_component = MenuComponent(driver)
    menu_component.go_to_page(config.HOME_PAGE_URL)
    pizza_menu_component = PizaMenuComponent(driver)
    pizza_card = pizza_menu_component.get_pizza_card(index=1)
    pizza_modal_component = PizzaModalComponent(driver)
    pizza_modal_component.open_modal_window(pizza_card)

    size_attributes_mapping = {
        "Маленькая": {"data-size": "1", "diameter": "25 см"},
        "Средняя": {"data-size": "2", "diameter": "30 см"},
        "Большая": {"data-size": "3", "diameter": "35 см"}
    }

    for size_name, attributes in size_attributes_mapping.items():
        data_size = attributes["data-size"]
        diameter_value = attributes["diameter"]

        pizza_modal_component.select_pizza_size(size_name)

        actual_data_size = pizza_modal_component.get_pizza_data_size(data_size)
        assert actual_data_size == data_size, "The data-size attribute did not match the selected size."

        actual_pizza_diameter = pizza_modal_component.get_pizza_diameter(diameter_value)
        assert actual_pizza_diameter == diameter_value, "The diameter value did not match the selected size."


def test_pizza_crust_selection_availability(driver):
    menu_component = MenuComponent(driver)
    menu_component.go_to_page(config.HOME_PAGE_URL)
    pizza_menu_component = PizaMenuComponent(driver)
    pizza_card = pizza_menu_component.get_pizza_card(index=1)
    pizza_modal_component = PizzaModalComponent(driver)
    pizza_modal_component.open_modal_window(pizza_card)

    size_crust_mapping = {
        "Маленькая": {"thin_crust_available": False},
        "Средняя": {"thin_crust_available": True},
        "Большая": {"thin_crust_available": True}
    }

    for size_name, crust_info in size_crust_mapping.items():
        pizza_modal_component.select_pizza_size(size_name)

        if crust_info["thin_crust_available"]:
            assert pizza_modal_component.is_crust_option_selecteble('Тонкое'), \
                f"Thin crust should be selectable for size {size_name}"
        else:
            assert not pizza_modal_component.is_crust_option_selecteble('Тонкое'), \
                f"Thin crust should not be selectable for size {size_name}"


def test_add_additional_ingridient(driver):
    menu_component = MenuComponent(driver)
    menu_component.go_to_page(config.HOME_PAGE_URL)
    pizza_menu_component = PizaMenuComponent(driver)
    pizza_card = pizza_menu_component.get_pizza_card(index=1)
    pizza_modal_component = PizzaModalComponent(driver)
    pizza_modal_component.open_modal_window(pizza_card)

    initial_price = utils.parse_price(pizza_modal_component.get_cart_button_price())

    additional_ingredient = "Креветки"
    pizza_modal_component.select_additional_ingredient(additional_ingredient)

    assert pizza_modal_component.is_ingredient_selected(additional_ingredient), \
        f"Ingredient {additional_ingredient} should be selected after clicking."

    updated_price = utils.parse_price(pizza_modal_component.get_cart_button_price())
    assert updated_price > initial_price, \
        "The price should increase after adding an additional ingredient."
