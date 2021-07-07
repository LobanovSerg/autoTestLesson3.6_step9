# import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# проверка наличия кнопки добавления товара на странице
def test_page_contains_add_to_cart_button(browser):
    browser.get(link)
    # time.sleep(30)
    button = browser.find_elements_by_css_selector(
        '.btn-primary.btn-add-to-basket')
    assert len(button) == 1, 'Button not found or not unique!'
