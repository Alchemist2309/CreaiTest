from behave import given, when, then
from utils.driver import get_driver
from pages.creai_page import CreaiPage

@given('El usuario navega a la página de inicio de creai')
def open_homepage(context):
    context.driver = get_driver()
    context.creai_page = CreaiPage(context.driver)
    context.creai_page.open()

@then('La página debe cargarse correctamente')
def verify_homepage_load(context):
    status_code = context.creai_page.get_status_code()
    assert status_code == 200