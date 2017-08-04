from LoginPage import  LoginPage
from selenium.webdriver.common.keys import Keys
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestCredential
import random
import string
from Environment import my_environment
from RandomCredential import randomFullName,randomEmail

#print(TestCredential.test_fan[0])


#trytry = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
#print(trytry)
    #''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

# #rad = randomPassword(4,4)
# lista = [1,2,3]
# lista[0]
# print(lista[0])
# desired_caps={}
# #my_environment.desire_caps_device_environment(desired_caps,desired_caps,"samsung galaxy j1")
#
#
# d = my_environment.dasdasdas("samsung galaxy j1","samsung galaxy j1")
# for i in d:
#     print(i)