from behave import given, when, then, step
from utils.driver import get_driver
from pages.creai_page import CreaiPage
import time

@given('El usuario navega a la página de inicio de creai')
def open_homepage(context):
    context.driver = get_driver()
    context.creai_page = CreaiPage(context.driver)
    context.creai_page.open()

@then('La página debe cargarse correctamente')
def verify_homepage_load(context):
    status_code = context.creai_page.get_status_code()
    assert status_code == 200

@then('no debe haber errores visibles en consola')
def verify_no_console_errors(context):
    assert context.creai_page.console_errors()

@then('El logo de creai debe ser visible')
def verify_logo_visible(context):
    assert context.creai_page.logo_displayed()

@then('debe existir un botón de contacto')
def verify_cta_visible(context):
    assert context.creai_page.is_cta_visible()

@then("deben existir al menos tres secciones visibles en pantalla")
def step_sections_visible(context):
    count = context.creai_page.count_sections()
    assert count >= 3, f"Solo se encontraron {count} secciones visibles"

@when("hace clic en la opción About us del menu")
def step_click_about_us(context):
    context.creai_page.click_about_us()

@then("la URL debe ser la de la página About us")
def step_validate_about_url(context):
    assert context.creai_page.validate_about_us_url(), f" La URL no es la esperada ({context.driver.current_url})"
