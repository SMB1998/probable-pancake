
------------------------------------- TO INSTALL A VIRTUAL ENV AND REPO PACKAGES ----------------------------------- 

#Fist we need to install python 3.8.8 from the official web site 


        https://www.python.org/downloads/windows/

        (also if you are windows user and have a x64 procesor you can use)

        https://www.python.org/ftp/python/3.8.8/python-3.8.8-amd64.exe

#We can chen the python version = 3.8.8 using using the flag --verson, type the following into the Command Promt (cmd)

        $ python --version
        sould appear:  Python 3.8.8


#Now we can install virtualenv typing the following on the terminal(you should see a new folder "venv" on the main directory of the project)

        $ pip install vitualenv

#Then to create the virtualenv and activate it using

        $ python -m venv ./venv  (create)
        $ source venv/Scripts/activate (activate)
        sould appear: (venv)

#Now we can install our repo packages inside the virtualenv by using the requeriments.txt file with the following command

        $ pip install requeriments.txt (this file contains our packages and its versions)

------------------------------------- TO INSTALL CHROMEDRIVER ------------------------------------  

#Download chromedriver from https://chromedriver.chromium.org/downloads and ensure that the chromdriver version matches your 
#Google Chrome version (if chromedriver and Google Chrome versions don't match compiler will raise an error regarding this)


#afther  downloading the chromedriver move manually the chromedriver.exe to the v911-regressions/chromedriver/chromedriver_exe/ folder and 
#replace the one that is there (or maybe try with this, this chromedriver is for Google Chrome 106.X ) 
#Or you can use this command on the cmd into the main directory of the project (v911-regressions)

        $ move <source_chromedriver.exe_path> v911-regressions/chromedriver/chromedriver_exe/

------------------------------------- TO SET UP THE AWS CREDENCIALS ------------------------------

#Request to the devops team mate the acces keys ad set up them with the guide in the link below


        [AWS Programmatic credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
        

------------------------------------- TO RUN THE TESTS LOCALLY -----------------------------------        

#Run functonals/smoke tests showing prints, exceptions, and kind of logs we can see in temrinal when running python locally (with the STDOUT )

        $ pytest -s -v -m functionals (for fuctionals)
        $ pytest -s -v -m smoke (for smoke tests)

#Run functonals/smoke tests just with testing results (without the STDOUT )

        $ pytest -v -m functionals  (for fuctionals)
        $ pytest -v -m smoke (for smoke tests)
