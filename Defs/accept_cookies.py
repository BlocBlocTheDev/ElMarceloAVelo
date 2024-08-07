def accept_cookies(driver):
    try:
        accept_cookies_button_xpath = '/html/body/app-root/ion-app/ion-modal/div[2]/app-cookie/ion-footer/ion-grid/ion-row/ion-col[2]/ion-button'
        accept_cookies_button = driver.find_element(By.XPATH, accept_cookies_button_xpath)
        accept_cookies_button.click()
    except Exception:
        pass  # Si le bouton n'est pas trouvé, on continue sans lancer d'exception