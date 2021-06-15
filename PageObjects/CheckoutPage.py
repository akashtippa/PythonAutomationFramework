from selenium.webdriver.common.by import By


class CheckoutPage:
    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    CheckoutItem = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    Checkout = (By.XPATH, "//button[normalize-space()='Checkout']")
    EnterCountry = (By.CSS_SELECTOR, "#country")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutItem(self):
        return self.driver.find_element(*CheckoutPage.CheckoutItem)

    def getCheckout(self):
        return self.driver.find_element(*CheckoutPage.Checkout)
