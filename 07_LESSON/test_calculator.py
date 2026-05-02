from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage

class TestCalculator:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.page = CalculatorPage(self.driver)
        self.driver.implicitly_wait(10)

    def test_slow_calculator(self):
        self.page.open()
        self.page.set_delay("45")
        self.page.click_button("7")
        self.page.click_button("+")
        self.page.click_button("8")
        self.page.click_button("=")
        result = self.page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()