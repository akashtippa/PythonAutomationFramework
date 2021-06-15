import time

import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomepageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        logs.info("first name is :" + getData["firstname"])
        homepage.enterName().send_keys(getData["firstname"])
        logs.info("email is :" + getData["email"])
        homepage.enterEmail().send_keys(getData["email"])
        logs.info("Password is :" + getData["password"])
        homepage.enterPassword().send_keys(getData["password"])
        homepage.checkBox().click()
        logs.info("Gender is :" + getData["gender"])
        self.selecOptionbytext(homepage.gender(), getData["gender"])

        homepage.dob().send_keys("03042022")
        homepage.submit().click()
        time.sleep(3)
        alertText = homepage.successMessage().text
        logs.info("Succes Recieved from Application: " + alertText)
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
