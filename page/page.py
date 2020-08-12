from page.contact_list_page import ContactListPage
from page.new_contact_page import NewContactPage
from page.saved_contact_page import SavedContactPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def contact_list(self):
        return ContactListPage(self.driver)

    @property
    def new_contact(self):
        return NewContactPage(self.driver)

    @property
    def saved_contact(self):
        return SavedContactPage(self.driver)
