import pytest
from authentication.test_data import admin_user, volunteer_user
from shared.authentication import single_authentication
from shared.db_mongo import is_administrator


@pytest.mark.parametrize("smoke_url",[
    "profile",
    "users",
    "incidents",
    "incidents/6345e23d422943523e8960e0",
    "trainings",
    "events",
    "NonCorrectUrl"
])
@pytest.mark.admin_smoke
def test_smoke_admin(smoke_url):
    
    #login and get the authentication token to go inside the app on the {host}/users section
    _, user_id = single_authentication(admin_user["email"], admin_user["password"], test_role="ADMINISTRATOR", test_url=smoke_url)

    try:
        # decide if is administrator or not
        if(is_administrator(user_id)):
            assert True
        else:
            assert False 
           
    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        assert False


@pytest.mark.parametrize("smoke_url",[
    "profile",
    "users",
    "incidents",
    "incidents/6345e23d422943523e8960e0",
    #"trainings", wtf this need t be corrected xdxdxd
    "events",
    "NonCorrectUrl"
])
@pytest.mark.volunteer_smoke
def test_smoke_volunteer(smoke_url):
    
    #login and get the authentication token to go inside the app on the {host}/users section
    _, user_id = single_authentication(volunteer_user["email"], volunteer_user["password"], test_role="VOLUNTEER", test_url=smoke_url)

    try:
        # decide if is administrator or not
        if(is_administrator(user_id)):
            assert False
        else:
            assert True 
           
    except Exception as e:
        print(f'ERROR: Test failed due: {e} ')
        assert False