from selenium.webdriver.common.by import By


class HomePage:

    EnterName = (By.CSS_SELECTOR, "input[name='name']")
    EnterEmail = (By.XPATH, "//input[@name='email']")
    EnterPassword = (By.ID, "exampleInputPassword1")
    Checkbox = (By.ID, "exampleCheck1")
    Gender = (By.ID, "exampleFormControlSelect1")
    Dob = (By.CSS_SELECTOR, "input[name='bday']")
    Submit = (By.CSS_SELECTOR, "input[value='Submit']")
    SuccessMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def enterName(self):
        return self.driver.find_element(*HomePage.EnterName)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.EnterEmail)

    def enterPassword(self):
        return self.driver.find_element(*HomePage.EnterPassword)

    def enterName(self):
        return self.driver.find_element(*HomePage.EnterName)

    def checkBox(self):
        return self.driver.find_element(*HomePage.Checkbox)

    def gender(self):
        return self.driver.find_element(*HomePage.Gender)

    def dob(self):
        return self.driver.find_element(*HomePage.Dob)

    def submit(self):
        return self.driver.find_element(*HomePage.Submit)

    def successMessage(self):
        return self.driver.find_element(*HomePage.SuccessMessage)

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)



