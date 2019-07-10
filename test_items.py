import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    def test_button_add(self, browser):
        browser.get(link)

        time.sleep(5)

        browser.find_element_by_css_selector("#login_link")
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")
