from appium import webdriver
import os
class my_environment(object):


    def __init__(self, desired_caps):
        self.desired_caps = {}


    def set_my_environment(self,  choose_device,app_version):

        self.desire_caps_app_version_environmen(app_version)

        self.desire_caps_device_environment(choose_device)

        return self.desired_caps

    def desire_caps_device_environment(self, choose_device):
        if (choose_device == "samsung galaxy j1"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '4.2'
            self.desired_caps['deviceName'] = '11019d33a982924a'
        if (choose_device == "prestigio muze c3"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '5.0.2'
            self.desired_caps['deviceName'] = 'MTP70860212243'


    def desire_caps_app_version_environmen(self, app_version):

        if (app_version == "development version"):
            self.desired_caps['app'] = os.path.abspath(
                os.path.join(os.path.dirname(__file__), 'com.iplay.stg-1foot.apk'))
            self.desired_caps['appPackage'] = 'com.iplay.stg'
            self.desired_caps['appActivity'] = 'com.iplay.activity.SplashActivity'
        if (app_version == "stg version"):
            self.desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'com.iplay-1.apk'))
            self.desired_caps['appPackage'] = 'com.iplay'
            self.desired_caps['appActivity'] = '.activity.SplashActivity'  # StartingTutorialActivity  SplashActivity




