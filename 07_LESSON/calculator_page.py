from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        # Ждём, пока в результате исчезнет знак + (вычисление завершится)
        self.wait.until(lambda driver: "+" not in self.driver.find_element(By.CSS_SELECTOR, ".screen").text)
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text