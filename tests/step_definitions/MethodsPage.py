import pytest
import time
from LocatorsPage import Locators
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, scenario, given, when, then
scenarios ("../features/basic_search.feature")
locator = Locators

class Methods:
    @pytest.fixture(scope="session")
    def browser():
      with sync_playwright() as p:
        browser =p.chromium.launch(headless=False,channel='chrome')
        yield browser
        browser.close()

    @pytest.fixture(scope="function")
    def page(browser):
     page = browser.new_page()
     yield page 
     page.close()
     ###test
     ###test
   


    @given ("As an not logged user navigate to homepage https://www.kiwi.com/en/")
    def go_to_page(page):
     page.goto("https://www.kiwi.com/en/")    
     page.click('//*[@id="cookies_accept"]' )

    @when("I select one-way trip type") 
    def one_way(page):  
      page.click(locator.return_btn) 
      time.sleep(1)
      page.click(locator.one_way) 
      ### my city is Belgrade and when I start app Belgrade is selected, I need to delete that and import RTM, I believe that locator is good for deletion your city
      page.click(locator.belgrade)
    

    @when("Set as departure airport RTM") 
    def departure_airport(page):
       page.fill(locator.departure_airport,'RTM')
       page.click(locator.roterdam)
    

    @when("Set the arrival Airport MAD") 
    def arival_airport(page):
       page.fill(locator.arrival_airport,'MAD')
       page.click(locator.madrid)

    @when("Set the departure time 1 week in the future starting current date") 
    def departure_time(page):
       xpath = "//input[@name='search-outboundDate']"
       page.click(xpath)
       time.sleep(5)
       # Calculate the date one week from today
       today ="(//*[contains(text(), 'Today')])"
       div_buttons = page.locator('div[role="button"][data-test ="CalendarDay"]').element_handles()
       div_buttons_list = [div for div in div_buttons]
       print("number of elements with role='button':", len(div_buttons_list))
    
       counter=0 
       for div in div_buttons_list:
        if (counter ==7):
            div.click()
        counter =counter +1    
    
       time.sleep(1)

    @when("Uncheck the `Check accommodation with booking.com` option") 
    def uncheck_accomodation(page):
       xpath = "//div[contains(text(), 'Set dates')]"
       page.click(xpath)
       time.sleep(1)
       # Calculate the date one week from today
       check_accomodation="//div[@data-test='bookingCheckbox']//*[name()='svg'][contains(@class, 'orbit-icon')]"
       page.click(check_accomodation)  


    @when("Click the search button") 
    def search(page):
       search_button = "(//div[contains(text(), 'Search')])[1]"
       page.click(search_button)
       time.sleep(1)

    @then("I am redirected to search results page") 
    def redirected_to_result_page(page):
       price_alerts = "//div[contains(@class, 'duration-fast')]/div[contains(@class, 'bg-white-normal')]/*[name()='svg'][contains(@class, 'orbit-icon')]"
       page.click(price_alerts)
       ### I clicked on the button for price alerts and that is validation that redirection was success!
    
       time.sleep(5)

    
    
