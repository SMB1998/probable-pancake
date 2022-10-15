from selenium import webdriver


def driver_config(mode:str=None):
    options =  webdriver.ChromeOptions()
    if mode != None:
        options.add_argument(mode)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--allow-insecure-localhost")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("acceptInsecureCerts")
    #prefs = {"profile.default_content_setting_values.notifications" : 2}
    #options.add_experimental_option("prefs",prefs)
    #options.add_argument('--start-maximized')
    driver_path = 'chromedriver\\chromedriver_exe\\chromedriver.exe'
    driver = webdriver.Chrome(driver_path, options=options)
    return driver