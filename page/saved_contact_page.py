import allure

import page
from base.base_action import BaseAction


class SavedContactPage(BaseAction):
    # 获取大标题的名称
    @allure.step(title='获取大标题的名称')
    def get_contact_title_text(self):
        return self.find_element(page.contact_title_feature).text
