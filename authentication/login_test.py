from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from authentication.test_data import admin_user, volunteer_user
from shared.authentication import single_authentication, cognito_token_verification
from shared.db_mongo import is_administrator
from shared.custom_exceptions.authentication_exceptions import CognitoTokenVeificationException


def selenium_app_logout(driver):
    #logout button click
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="root"]/header/nav/div/div[2]/div[2]/a[2]/button/span[1]')))\
    .click()

    #wait the email login field to be loaded 
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID ,'login-email')))
    return driver


@pytest.mark.functionals
def test_login_as_volunteer():
    
    #login and get the authentication token to go inside the app on the {host}/users section
    _, user_id = single_authentication(volunteer_user["email"], volunteer_user["password"], test_role="VOLUNTEER")

    try:
        # decide if is administrator or not
        if(is_administrator(user_id)):
            assert False
        else:
            assert True 
           
    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        assert False


@pytest.mark.functionals
def test_login_as_admin():

    #login and get the authentication token to go inside the app
    _, user_id = single_authentication(admin_user["email"], admin_user["password"], test_role="ADMINISTRATOR")

    # automation here:
    try:
        # decide if is volunteer or not
        if(is_administrator(user_id)):
            assert True
        else:
            assert False
           
    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        assert False


@pytest.mark.functionals
def test_logout_as_admin():

    #login and get the authentication token to go inside the app
    driver, user_id = single_authentication(admin_user["email"], admin_user["password"], test_role="ADMINISTRATOR")


    try:
        # decide if is volunteer or not
        if(is_administrator(user_id)):
            pass
        else:
            print("This user is not and admin ind the test is for an admin role")
            assert False

        driver = selenium_app_logout(driver)
        
        #check the local storage for verifying no cognito data saved
        if(cognito_token_verification(user_id) != None):
            assert False

    #catch when the cognito token is invalid that is what we want 
    #here as we have signed out of the app (the token need to turn invalid)
    except CognitoTokenVeificationException as e:
        assert True
           
    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        driver.close()
        assert False


@pytest.mark.functionals
def test_logout_as_volunteer():
    
    #login and get the authentication token to go inside the app
    driver, user_id = single_authentication(volunteer_user["email"], volunteer_user["password"], test_role="VOLUNTEER")

    try:
        # decide if is volunteer or not
        if(is_administrator(user_id)):
            assert False
        else:
            assert True 
           
        driver = selenium_app_logout(driver)
        
        #check the local storage for verifying no cognito data saved
        if(cognito_token_verification(user_id) != None):
            assert False

    #catch when the cognito token is invalid that is what we want 
    #here as we have signed out of the app (the token need to turn invalid)
    except CognitoTokenVeificationException as e:
        assert True

    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        driver.close()
        assert False





    

    






