import allure

import page
from base.base_action import BaseAction


class ContactListPage(BaseAction):
    # 点击添加联系人
    @allure.step(title='点击添加联系人')
    def click_add_contact(self):
        self.click(page.add_contact_button)
