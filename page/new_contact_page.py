import allure

import page
from base.base_action import BaseAction


class NewContactPage(BaseAction):
    # 点击本地保存
    def click_locality(self):
        self.click(page.locality)

    # 输入联系人姓名
    @allure.step(title='输入联系人姓名')
    def input_name(self, content):
        self.input(page.name_edit_text, content)

    # 输入联系人电话
    @allure.step(title='输入联系人电话')
    def input_phone(self, content):
        self.input(page.phone_edit_text, content)



