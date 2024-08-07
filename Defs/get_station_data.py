def get_station_data(driver):
    try:
        name_xpath = '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-card/ion-card-header/ion-card-title/ion-label'
        element_xpath = '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-card/ion-card-content/ion-row/ion-col/ion-text[1]'
        places_xpath = '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-card/ion-card-content/ion-row/ion-col/ion-text[2]'

        name = driver.find_element(By.XPATH, name_xpath).text
        value = int(driver.find_element(By.XPATH, element_xpath).text)
        places = int(driver.find_element(By.XPATH, places_xpath).text)

        bikedatanumbers = value
        endresearch = bikedatanumbers + 1

        bikes_data = {}

        currentbike = 1

        while currentbike != endresearch:
            IDBike_Xpath = f"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-list/ion-item[{currentbike}]/ion-label/h2/ion-text"
            BATBike_Xpath = f"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-list/ion-item[{currentbike}]/ion-label/p/span[1]"
            KMBike_Xpath = f"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-list/ion-item[{currentbike}]/ion-label/p/span[2]"
            button_xpath = f"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-station/ion-content/ion-list/ion-item[{currentbike}]/ion-button"

            BikeIsBlock = None
            try:
                IDBike = driver.find_element(By.XPATH, IDBike_Xpath).text
                BATBike = driver.find_element(By.XPATH, BATBike_Xpath).text
                KMBike = driver.find_element(By.XPATH, KMBike_Xpath).text
                button_element = driver.find_element(By.XPATH, button_xpath)

# Vérifier l'attribut aria-disabled
                aria_disabled = button_element.get_attribute("aria-disabled")

# Déterminer si le vélo est bloqué en fonction de la valeur de aria-disabled
                if aria_disabled == "true":
                    BikeIsBlock = True
                else:
                    BikeIsBlock = False

                bikes_data[IDBike] = {
                    'BATBike': BATBike,
                    'KMBike': KMBike,
                    'Bloked' : BikeIsBlock
                }
                #print(BikeIsBlock)
            except Exception as e:
                print(f"Erreur en récupérant les données du vélo {currentbike} à la Station {name}: {e}")

            currentbike += 1

        velo = "vélo" if value == 1 else "vélos"
        place = "place" if places == 1 else "places"
        return name, value, velo, places, place, bikes_data

    except Exception as e:
        print(f"Une erreur est survenue pour obtenir les données pour {AllStationsID} : {e}")
        return "", 0, "", 0, "", {}