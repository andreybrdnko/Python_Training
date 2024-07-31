import unittest

from websiteProject.ebayProject.Pages.ebayHomePage import ebayHomePage
from websiteProject.ebayProject.Tests.BaseSelenium import baseSelenium
from websiteProject.ebayProject.Tests.Globals import url

class ebay_test(unittest.TestCase):

    def test_price_value(self):
        base = baseSelenium()
        driver = base.selenium_start(url)

        ebay_home = ebayHomePage(driver)

        ebay_home.select_first_item()
        ebay_home.get_first_price()
        ebay_home.return_to_home_page()
        ebay_home.select_second_item()
        ebay_home.get_second_price()

        base.selenium_end(driver)
