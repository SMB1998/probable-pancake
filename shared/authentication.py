from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from chromedriver.driver_config import driver_config
from chromedriver.chrome_local_storage import LocalStorage
import re
import json
from shared.context_vars import cvar_admin, cvar_volunteer
from shared.custom_exceptions.authentication_exceptions import CognitoTokenVeificationException
import boto3


PAGE_URL = 'https://d3glcfa4f3sllf.cloudfront.net/'
driver = driver_config()
ADMINISTRADOR = "ADMINISTRATOR"

client = boto3.client('cognito-idp')


def cognito_token_verification(AccesKey):
    try: ## Used fot vertify connection with cognito and if fails return a json to the client
        cliente= dict(client.get_user(AccessToken = AccesKey))
        print(cliente)
        return cliente
    except:
        raise CognitoTokenVeificationException("---- ERROR:","---- invalid acces token")


def get_page_user_local_storage(driver, data_to_get:str = "userData", test_role:str = None) -> (dict) :

    #excecute some js scritps
    storage = driver.execute_script("return window.localStorage;")
    user_data = ""
    for value in storage:
            data = re.search(f"^CognitoIdentityServiceProvider.*{data_to_get}$", value) 
            if(data != None):
                user_data = storage[value]
    
    if(test_role == ADMINISTRADOR):
        localStorage_data = cvar_admin.set(storage)
    elif(test_role == "VOLUNTEER"):
        localStorage_data = cvar_volunteer.set(storage)
    else:
        print(localStorage_data)
        raise
    
        
    return json.loads(user_data)

def login(email:str, password:str, test_role:str = None):  

    # Go to the page url
    driver.get(PAGE_URL)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID ,'login-email')))\
        .send_keys(email)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID ,'login-password')))\
        .send_keys(password)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="root"]/section/div/div/div[2]/form/div[3]/button')))\
        .click()
    # by clicking into users section we are sure we are into the app and
    # cognito auth system saves some data into the local storage
    WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="navbar-nav"]/a[1]')))
    
    # get the local storage
    storage = LocalStorage(driver)

    # set an item
    storage.set("mykey2", 5678)
    user_id = get_page_user_local_storage(driver, test_role= test_role)
    return driver, user_id


def single_authentication(email:str, password:str, test_role:str = None, test_url:str = "users"):
    data_to_get = "userData"
    if(test_role == ADMINISTRADOR):
        if(cvar_admin.get() == False):
            return login(email, password, test_role)
        localStorage_data = cvar_admin.get()

    elif(test_role == "VOLUNTEER"):
        if(cvar_volunteer.get() == False):
            return login(email, password, test_role)
        localStorage_data = cvar_volunteer.get()
    else:
        raise 

    if(localStorage_data == False):
        return login(email, password, test_role)
    else:
        # get the local storage
        storages = LocalStorage(driver)

        #excecute some js scritps
        storage = localStorage_data
        user_id = ""
        for value in storage:
                storages.set(value, storage[value])
                data = re.search(f"^CognitoIdentityServiceProvider.*{data_to_get}$", value)
                
                if(data != None):
                    user_id = storage[value]
        
        driver.get(PAGE_URL+test_url)
        return driver, json.loads(user_id)