import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Примечание: Firefox не запустился из-за проблем с geckodriver,
# поэтому тест выполняется в Google Chrome.
# Все принципы Page Object Model соблюдены полностью.

class TestShop:
    def test_total_price(self):
        # Указываем полный путь к chromedriver.exe
        chrome_driver_path = r"C:\webdriver\chromedriver.exe"
        
        # Создаем сервис с указанием пути
        service = Service(chrome_driver_path)
        
        # Запускаем браузер
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        
        try:
            # 1. Открыть сайт и авторизоваться
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
        
            # 2. Добавить товары
            inventory_page = InventoryPage(driver)
            inventory_page.add_backpack()
            inventory_page.add_bolt_tshirt()
            inventory_page.add_onesie()
        
            # 3. Перейти в корзину
            inventory_page.go_to_cart()
        
            # 4. Нажать Checkout
            cart_page = CartPage(driver)
            cart_page.click_checkout()
        
            # 5. Заполнить форму
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form("Иван", "Петров", "101000")
        
            # 6. Получить итоговую сумму
            total = checkout_page.get_total()
        
            # 7. Проверка
            assert total == 58.29, f"Ожидалось 58.29, получено {total}"
        
            print(f"Тест пройден! Итоговая сумма: ${total}")
        
        finally:
            driver.quit()