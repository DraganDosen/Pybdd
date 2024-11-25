class Locators:
    main_url= "https://www.kiwi.com/en/"
    accept ='//*[@id="cookies_accept"]' 
    return_btn ='//*[contains(text(), "Return")]'
    one_way ='//*[contains(text(), "One-way")]'
    belgrade = '//*[@id="react-view"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[1]/div'
    departure_airport= "//div[@data-test='PlacePickerInput-origin']/input[@data-test='SearchField-input']"
    roterdam = '//*[contains(text(), "Rotterdam, Netherlands")]'
    arrival_airport = "//div[@class='absolute overflow-hidden whitespace-nowrap w-full']/input[@data-test='SearchField-input']"
    madrid = '//*[contains(text(), "Madrid, Spain")]'
    search_button = "(//div[contains(text(), 'Search')])[1]"
    price_alerts = "//div[contains(@class, 'duration-fast')]/div[contains(@class, 'bg-white-normal')]/*[name()='svg'][contains(@class, 'orbit-icon')]"
    check_accomodation="//div[@data-test='bookingCheckbox']//*[name()='svg'][contains(@class, 'orbit-icon')]"
    set_dates = "//div[contains(text(), 'Set dates')]"
    outbound_date = "//input[@name='search-outboundDate']"