from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=1):
        """
        根据特征，找元素
        :param loc:
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
        return element

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, content):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(content)

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)



