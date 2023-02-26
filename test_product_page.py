import pytest

from .pages.product_page import ProductPage

@pytest.mark.parametrize('num', ["0","1","2","3","4","5","6",
                                 pytest.param("7", marks=pytest.mark.xfail),
                                 "8","9"])
def test_guest_can_add_product_to_cart(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_in_basket()