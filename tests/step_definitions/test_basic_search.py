import pytest
import time
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, scenario, given, when, then
from MethodsPage import Methods
from LocatorsPage import Locators

scenarios ("../features/basic_search.feature")
locator = Locators
method = Methods

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
  
method.go_to_page
@given ("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def go_to_page(page):
    page.goto(locator.main_url)    
    page.click(locator.accept)
    

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
def departure_airport(page):
    page.fill(locator.arrival_airport,'MAD')
    page.click(locator.madrid)

@when("Set the departure time 1 week in the future starting current date") 
def departure_time(page):
    page.click(locator.outbound_date)
    time.sleep(2)
    # Calculate the date one week from today
    
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
    page.click(locator.set_dates)
    time.sleep(1)
    page.click(locator.check_accomodation)  


@when("Click the search button") 
def departure_time(page):
    page.click(locator.search_button)
    time.sleep(1)

@then("I am redirected to search results page") 
def redirected_to_result_page(page):
    page.click(locator.price_alerts)
    ### I clicked on the button for price alerts and that is validation that redirection was success!
    time.sleep(2)

    
    
