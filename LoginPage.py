
from selenium.webdriver.common.by import  By
import TestCredential
from SeleniumMethods import  SeleniumMethods
import  time


class LoginPage(object):
    tutorial_form = (By.NAME, "Skip tutorial")
    sign_in_button = (By.NAME,"Log in")
    login_form = (By.CLASS_NAME,"android.widget.EditText")
    type_login = (By.CLASS_NAME,"android.widget.EditText",TestCredential.test_fan[0])
    password_form = (By.ID,"password_edit_text")
    type_password = (By.ID,"password_edit_text",TestCredential.test_fan[1])
    login_button =  (By.ID,"login_button")


class CreateAccountPage(object):
    sign_in_via_email = (By.ID,"bt_sign_email")
    full_name_form = (By.ID,"full_name")
    email_address_form = (By.ID,"login")
    password_form = (By.ID,"password")

    type_full_name_form = (By.ID, "full_name", TestCredential.test_new_full_name)
    type_email_address_form = (By.ID,"login",TestCredential.test_new_email)
    type_password_form = (By.ID,"password","testqwerty")

    register_button = (By.ID, "sign_button")

    popup_text_tutorial = (By.ID,"popup_text")
    handball_sport = (By.ID, "handball_sport")
    bandy_sport = (By.ID, "bandy_sport")
    choose_interests_button = (By.ID,"bt_save_sport_interest")

#TestCredential.test_fan[0]
class Feed(object):
    handball_tab = (By.NAME, "Handball")
    searching = (By.ID,"action_search")
    searching_form = (By.ID,"et_search")
    searching_type = (By.ID,"et_search","ttt")
    searching_element = (By.ID,"tv_name")
    searching_type_chuck_norris = (By.ID,"et_search","chucknorris")
    notification_bell_list = (By.ID,"action_notifications")

class More(object):
    edit_profile_action_settings = (By.ID, "action_settings")
    edit_profile_title = (By.ID,"title")
    edit_profile_activity_profile_bg_edit = (By.ID, "activity_profile_bg_edit")
    edit_profile_text1 = (By.ID, "text1")

class JobOffer(object):
    job_offer_button = (By.ID,"more_name",2)
    choose_job_offer = (By.NAME,"Test jobb")
    apply_job_offer = (By.ID,"apply")
    phone_number_form = (By.CLASS_NAME,"android.widget.EditText",1)
    type_english_phone_number = (By.CLASS_NAME,"android.widget.EditText","20 7646 0000",1)
    start_date = (By.ID,"start_date")
    confirm_current_date = (By.ID,"ok")
    monday = (By.NAME,"M")
    send_application = (By.NAME,"Send application")

class Financialadvisers(object):
    financial_advisers = (By.NAME,"Financial advisers",3)
    choose_financial_advisers = (By.NAME,"No Country")
    apply_contact_offer = (By.NAME,"Contact")
    phone_number_form = (By.CLASS_NAME,"android.widget.EditText",1)
    type_english_phone_number = (By.CLASS_NAME, "android.widget.EditText", "20 7646 0000", 1)
    send_application = (By.NAME,"Send application")

class MainMenuTab(object):
    main_menu_tab_feed = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab", 0)
    main_menu_tab_chat = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab", 1)
    main_menu_tab_game_view = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab", 2)
    main_menu_tab_more = (By.CLASS_NAME,"android.support.v7.app.ActionBar$Tab",3)

class Games(object):
    searching_filter = (By.ID,"action_filter")
    all_games = (By.NAME,"All")
    football_games = (By.NAME,"Football")
    handball_games = (By.NAME, "Handball")
    bandy_games = (By.NAME, "Bandy")
    show_all_games = (By.ID,"bt_all_show")
    show_followed_only_games = (By.ID, "bt_followed_show")
    game_all_type = (By.ID, "bt_all_type")
    game_championship_type = (By.ID, "bt_champ_show")
    game_league_type = (By.ID, "bt_league_show")