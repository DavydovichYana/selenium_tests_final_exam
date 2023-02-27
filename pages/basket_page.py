from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_SELECTOR), "Busket isn't empty, but should be"

    def should_basket_be_empty_text(self):
        empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT_SELECTOR).text
        assert "empty" in empty_text, "Text about empty busket is not presented, but should be"