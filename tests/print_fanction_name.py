# Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
def print_name_function(function_name, *args):
    name_func = function_name.__name__.title().replace("_", " ")
    print("=" * 10, "Start", "=" * 10)
    print(name_func)
    for arg in args:
        print(arg.title())
    print("=" * 10, "End", "=" * 10)

def open_browser(browser_name):
    print_name_function(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_name_function(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_name_function(find_registration_button_on_login_page, page_url, button_text)

open_browser("chrome")
go_to_companyname_homepage("url")
find_registration_button_on_login_page("url", "button")