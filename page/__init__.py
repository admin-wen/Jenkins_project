"""以下为页面配置信息"""

from selenium.webdriver.common.by import By
# 添加联系人
add_contact_button = By.ID, "com.android.contacts:id/floating_action_button"
# 点击本地保存
locality = By.XPATH, "//*[@text='本地保存']"
# 姓名输入框
name_edit_text = By.XPATH, "//*[@text='姓名']"
# 电话输入框
phone_edit_text = By.XPATH, "//*[@text='电话']"
# 保存后的大标题
contact_title_feature = By.ID, "com.android.contacts:id/large_title"

