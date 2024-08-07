from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ebayHomePage():
    def __init__(self, driver):
        self.driver = driver
        self.luxury = "h3[class='vl-popular-destinations-evo__name']"
        self.balenciaga = "a[class='b-textlink b-textlink--parent']"
        self.first_item_in_list = "a[class='s-item__link']"
        self.first_price = "x-price-primary"
        self.logo = "gh-logo"
        self.search_box = "gh-ac"
        self.first_item_on_the_list = "a[class='s-item__link']"
        self.second_price = "x-price-primary"

    def select_first_item(self):
        luxury_select = self.driver.find_element(By.CSS_SELECTOR, self.luxury)
        luxury_select.click()
        balenciaga_select = self.driver.find_elements(By.CSS_SELECTOR, self.balenciaga)
        balenciaga_select[1].click()
        first_item_in_list_select = self.driver.find_element(By.CSS_SELECTOR, self.first_item_in_list)
        url_updated = first_item_in_list_select.get_attribute("href")
        self.driver.get(url_updated)

    def get_first_price(self):
        get_price_of_first_item = self.driver.find_element(By.CLASS_NAME, self.first_price)
        price_of_first_item = get_price_of_first_item.text
        index1 = price_of_first_item.index(" ")
        index2 = price_of_first_item.index(".")
        price_temp = price_of_first_item[index1:index2]
        first_price_as_int = int(price_temp)
        print(first_price_as_int)

        assert first_price_as_int > 20, 'The price of the product is cheaper than the provided value'

    def return_to_home_page(self):
        logo_click = self.driver.find_element(By.ID, self.logo)
        logo_click.click()

    def select_second_item(self):
        search_box_select = self.driver.find_element(By.ID, self.search_box)
        search_box_select.click()
        search_box_select.send_keys("shoes")
        search_box_select.send_keys(Keys.ENTER)
        select_first_item_in_list = self.driver.find_elements(By.CSS_SELECTOR, self.first_item_on_the_list)
        new_url_window = select_first_item_in_list[2].get_attribute("href")
        self.driver.get(new_url_window)

    def get_second_price(self):
        get_price_of_second_item = self.driver.find_element(By.CLASS_NAME, self.second_price)
        price_of_second_item = get_price_of_second_item.text
        index_one = price_of_second_item.index(" ")
        index_two = price_of_second_item.index(".")
        temp_price = price_of_second_item[index_one:index_two]
        second_price_as_int = int(temp_price)
        print(second_price_as_int)

        assert second_price_as_int < 250, 'The price of the product is too expensive'
