import unittest

from appium import webdriver
from appium.webdriver.common.multi_action import  MultiAction
from appium.webdriver.common.touch_action import  TouchAction
from LoginPage import Feed, LoginPage, CreateAccountPage, More,MainMenuTab, JobOffer, Financialadvisers
from SeleniumMethods import  SeleniumMethods
from Environment import  my_environment
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class iplay(unittest.TestCase):

    def setUp(self):

        desired_caps=my_environment({}).set_my_environment("samsung galaxy j1","development version")
        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

        self.my_selenium_method = SeleniumMethods(self.driver)
        self.touch_action = TouchAction(self.driver)
        self.multi_action = MultiAction(self.driver)

        #actiony - dokumentacja w linku
        #https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/touch-actions.md
        #act = TouchAction(self.driver)
        #example
        #element = self.driver.find_element_by_id("login_edit_text")
        #act.tap(element).perform()

    def tearDown(self):
        self.driver.quit()

    def test_mock(self):
        self.assertEqual(1,1)

    # def test_single_player_mode(self):
    #
    #     log_in_via_email(self.my_selenium_method)
    #
    #     self.my_selenium_method.click(*Feed.handball_tab)
    #     self.my_selenium_method.click(*Feed.searching)
    #     self.my_selenium_method.click(*Feed.searching_form)
    #     self.my_selenium_method.type(*Feed.searching_type)
    #     self.my_selenium_method.click(*Feed.searching_element)
    #
    #     self.assertEqual('1','1')


    # def test_check_list_of_notifications(self):
    #     log_in_via_email(self.my_selenium_method)
    #     self.my_selenium_method.click(*Feed.notification_bell_list)
    #     notification_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
    #     notification_list[0].click()
    #     self.assertEqual('1', '1')

    # def test_create_remove_user(self):
    #     self.my_selenium_method.click(*LoginPage.tutorial_form)
    #     self.my_selenium_method.click(*CreateAccountPage.sign_in_via_email)
    #
    #     self.my_selenium_method.click(*CreateAccountPage.full_name_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_full_name_form)
    #
    #     self.my_selenium_method.click(*CreateAccountPage.email_address_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_email_address_form)
    #
    #     self.my_selenium_method.click(*CreateAccountPage.password_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_password_form)
    #
    #     self.my_selenium_method.click(*CreateAccountPage.register_button)

    # def test_crredential(self):
    #
    #     self.my_selenium_method.click(*LoginPage.tutorial_form)
    #     self.my_selenium_method.click(*CreateAccountPage.sign_in_via_email)
    #
    #     self.my_selenium_method.click(*CreateAccountPage.full_name_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_full_name_form)
    #     self.my_selenium_method.hide_keyboard()
    #
    #     self.my_selenium_method.click(*CreateAccountPage.email_address_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_email_address_form)
    #     self.my_selenium_method.hide_keyboard()
    #
    #     self.my_selenium_method.click(*CreateAccountPage.password_form)
    #     self.my_selenium_method.type(*CreateAccountPage.type_password_form)
    #     self.my_selenium_method.hide_keyboard()
    #
    #     self.my_selenium_method.click(*CreateAccountPage.register_button)
    #     self.my_selenium_method.click(*CreateAccountPage.popup_text_tutorial)
    #     self.my_selenium_method.click(*CreateAccountPage.handball_sport)
    #     self.my_selenium_method.click(*CreateAccountPage.bandy_sport)
    #     self.my_selenium_method.click(*CreateAccountPage.choose_interests_button)
    #
    #     self.my_selenium_method.is_displayed(*Feed.handball_tab)
    #     self.my_selenium_method.click(*Feed.handball_tab)
    #
    #     self.assertEqual(1,1)

    #def test_go_to_more(self):
        #log_in_via_email(self.my_selenium_method)
        #self.my_selenium_method.click(*Feed.handball_tab)
        # self.my_selenium_method.click(*Feed.searching)
        # self.my_selenium_method.click(*Feed.searching_form)
        # self.my_selenium_method.type(*Feed.searching_type_chuck_norris)
        # self.my_selenium_method.click(*Feed.searching_element)
        #
        # self.my_selenium_method.click(*More.edit_profile_action_settings)
        # self.my_selenium_method.click(*More.edit_profile_title)
        # self.my_selenium_method.click(*More.edit_profile_activity_profile_bg_edit)
        # self.my_selenium_method.click(*More.edit_profile_text1)
        #
        # self.driver.find_element(By.CLASS_NAME, "android.widget.LinearLayout").click()
        # self.driver.find_element(By.ID, "okay").click()
        # self.driver.find_element(By.ID, "action_save_profile").click()

        # self.driver.find_element(By.ID,"action_settings").click()
        # self.driver.find_element(By.ID,"title").click()
        # self.driver.find_element(By.ID,"activity_profile_bg_edit").click()
        # self.driver.find_element(By.ID,"text1").click()


    # def test_apply_job_offer(self):
    #     log_in_via_email(self.my_selenium_method)
    #
    #     self.my_selenium_method.click_list(*MainMenuTab.main_menu_tab_more)
    #     self.my_selenium_method.click_list(*JobOffer.job_offer_button)
    #     self.my_selenium_method.click(*JobOffer.choose_job_offer)
    #     self.my_selenium_method.click(*JobOffer.apply_job_offer)
    #     self.my_selenium_method.click_list(*JobOffer.phone_number_form)
    #     self.my_selenium_method.type_list_element(*JobOffer.type_english_phone_number)
    #
    #     start_date = self.driver.find_element(By.ID, "start_date")
    #     self.my_selenium_method.hide_keyboard()
    #     self.my_selenium_method.click(*JobOffer.start_date)
    #     self.my_selenium_method.click(*JobOffer.confirm_current_date)
    #     self.my_selenium_method.click(*JobOffer.monday)
        # self.my_selenium_method.click(*JobOffer.send_application)



    #     self.driver.find_element(By.ID, "start_date").click()
    #     self.driver.find_element(By.ID, "ok").click()
    #     self.driver.find_element(By.NAME, "M").click()
    #     self.driver.find_element(By.NAME, "Send application").click()

    # def test_scroll_feed(self):
    #     log_in_via_email(self.my_selenium_method)
    #     self.my_selenium_method.click_list(*MainMenuTab.main_menu_tab_feed)
    #     el = self.driver.find_elements(By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab")[0]
    #     atouch_action = TouchAction(self.driver)
        #atouch_action.press(el).perform()

    # def test_chat_conversation(self):
    #     log_in_via_email(self.my_selenium_method)
    #     self.my_selenium_method.click_list(*MainMenuTab.main_menu_tab_chat)
    #
    #
    # def test_apply_financial_advisers(self):
    #     log_in_via_email(self.my_selenium_method)
    #     self.my_selenium_method.click_list(*MainMenuTab.main_menu_tab_more)
    #     self.my_selenium_method.click_list(*Financialadvisers.financial_advisers)
    #     self.my_selenium_method.click(*Financialadvisers.choose_financial_advisers)
    #     self.my_selenium_method.click(*Financialadvisers.apply_contact_offer)
    #
    #     self.my_selenium_method.click_list(*Financialadvisers.phone_number_form)
    #     self.my_selenium_method.type_list_element(*Financialadvisers.type_english_phone_number)
    #     self.my_selenium_method.hide_keyboard()
    #     self.my_selenium_method.click(*Financialadvisers.send_application)


def log_in_via_email(my_selenium_method):
    my_selenium_method.click(*LoginPage.tutorial_form)
    my_selenium_method.click(*LoginPage.sign_in_button)
    my_selenium_method.click(*LoginPage.login_form)
    my_selenium_method.type(*LoginPage.type_login)
    my_selenium_method.click(*LoginPage.password_form)
    my_selenium_method.type(*LoginPage.type_password)
    my_selenium_method.click(*LoginPage.login_button)


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(iplay)
    unittest.TextTestRunner(verbosity=2).run(suite)