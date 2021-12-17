import time
from selenium.webdriver.common.keys import Keys
from behave import *


@given('visit Armut')
def step(context):
    context.browser.get('https://armut.com/')
    time.sleep(2)
    context.browser.maximize_window()


@then('verify logo Armut')
def verify_logo(context):
    logo = context.browser.find_element_by_xpath("//*[@id='form1']/header/div/a")
    assert logo.is_displayed()


@then('it should have a title "Armut: Hizmet Piş, Ağzıma Düş. Ev Temizliği, Tadilat, Nakliyat"')
def home(context):
    assert context.browser.title == "[Armut: Hizmet Piş, Ağzıma Düş. Ev Temizliği, Tadilat, Nakliyat]"


@then('click on Kariyer')
def career(context):
    context.browser.find_element_by_partial_link_text("Kariyer").click()


@then('you found your QA Engineer')
def found(context):
    context.browser.find_element_by_partial_link_text("QA Engineer").click()
    assert context.browser.title == "QA Engineer - Armut Teknoloji AS - Career Page"
