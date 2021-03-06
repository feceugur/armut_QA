import time
from selenium.webdriver.common.keys import Keys
from behave import *

"""
@given('we visit Armut')
def step(context):
    context.browser.get('https://armut.com/')
    time.sleep(2)
    context.browser.maximize_window()


@then('verify logo')
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


@when('you select service')
def select_service(context):
    #sservice = str(str('//*[@id="form1"]/header/div/ul/li[') + service + str(']/a'))
    services = context.browser.find_element_by_xpath('//*[@id="form1"]/header/div/ul/li[1]/a')
    services.click()


@then('select from popular')
def select_pop(context):
    context.browser.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_rpPopularServicePods_ucServicePods_0_pnlServicePods_0"]').click()
    time.sleep(3)
    #pop_title = context.browser.find_element_by_xpath("/html/body/ngb-modal-window/div/div/div/service-questions-component/modal-header/div/custom-progressbar/div/h1")
    assert context.failed is False

@then('select plus')
def select_plus(context):
    context.browser.find_element_by_xpath('//*[@id="dynamic-form-component-element"]/div/div/button[2]/i').click()
    time.sleep(3)

@when('you search Temizlik')
def search(context):
    item = context.browser.find_element_by_xpath('//*[@id="form1"]/section[1]/div[2]/app-root-wizard/routing/search-form/div/form/div/div[2]/input')
    kkey = 'Temizlik'
    item.send_keys(kkey)
    item.send_keys(Keys.ENTER)
    time.sleep(2)


@then('you should see title')
def s_title(context):
    title = context.browser.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div/service-questions-component/modal-header/div/faq-button/button')
    time.sleep(2)
    assert title.is_displayed()
"""