import time

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfimrationPage import Confirmation
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        logs = self.getLogger()
        homepage = HomePage(self.driver)

        homepage.shopItems().click()

        checkOutPage = CheckoutPage(self.driver)
        logs.info("getting the all cards Titles")
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            logs.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getCheckoutItem().click()
        time.sleep(2)
        checkOutPage.getCheckout().click()

        confirm = Confirmation(self.driver)
        logs.info("Entering country name as Ind")
        confirm.CountryName().send_keys("Ind")
        self.verifyLinkPresence("India")

        confirm.SelectCountry().click()
        confirm.purchase().click()
        time.sleep(3)
        SuccessMessage = confirm.verifySuccessmessage().text
        logs.info("Text recieved from application :" +SuccessMessage)
        assert "Success!" in SuccessMessage
        self.driver.get_screenshot_as_file("screenshot.png")
