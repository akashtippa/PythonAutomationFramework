from selenium.webdriver.common.by import By


class Confirmation:
    EnterCountryName = (By.XPATH, "//input[@id='country']")
    Selectcountry = (By.LINK_TEXT, "India")
    Purchase = (By.XPATH, "//input[@value='Purchase']")
    VerifySuccessMessage = (By.CLASS_NAME,"alert-success")

    def __init__(self, driver):
        self.driver = driver

    def CountryName(self):
        return self.driver.find_element(*Confirmation.EnterCountryName)

    def SelectCountry(self):
        return self.driver.find_element(*Confirmation.Selectcountry)

    def purchase(self):
        return self.driver.find_element(*Confirmation.Purchase)

    def verifySuccessmessage(self):
        return self.driver.find_element(*Confirmation.VerifySuccessMessage)