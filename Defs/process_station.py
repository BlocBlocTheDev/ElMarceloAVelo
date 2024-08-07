def process_station(idstation):
    driver = init_driver()
    urlstation = f"https://lemarcelavelo.ecovelo.mobi/#/station/stn_{idstation}"
    
    try:
        driver.get(urlstation)
        time.sleep(5)  # Réduit le délai d'attente initial

        accept_cookies(driver)
        time.sleep(5)  # Réduit le délai d'attente après avoir accepté les cookies

        NomStation, value, velo, places, place, bikes_data = get_station_data(driver)
        #print(f"NomStation: {NomStation}, Value: {value}, Velo: {velo}, Places: {places}, Place: {place}, Bikes Data: {bikes_data}")

        if NomStation:
            return NomStation, value, velo, place, places, bikes_data
        else:
            return None, 0, "", 0, "", {}
    finally:
        driver.quit()