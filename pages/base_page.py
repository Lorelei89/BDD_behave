import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browser import Browser


class BasePage(Browser, unittest.TestCase):
    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
