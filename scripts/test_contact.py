from time import sleep
import pytest
import allure
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("contact_data.yaml", "test_contact"))
    def test_contact(self, args):
        name = args["name"]
        phone = args["phone"]
        self.page.contact_list.click_add_contact()
        # self.page.new_contact.click_locality()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)
        self.page.new_contact.press_back()
        # 断言：
        assert name == self.page.saved_contact.get_contact_title_text()



