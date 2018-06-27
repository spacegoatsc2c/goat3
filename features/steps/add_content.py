from selenium.webdriver.common.keys import Keys
import time

@given(u'I am on the home page')
def step_impl(context):
    context.browser.get(context.base_url)

@when(u'I add a youtube link "{video_link}"')
def step_impl(context, video_link):
    input_box = context.browser.find_element_by_id("id_upload")
    input_box.send_keys(f"{video_link}")
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)

@then(u'I will see a link to "{link_text}" on the home page')
def step_impl(context, link_text):
    assert f"{link_text}" in context.browser.page_source
