import pytest
from selenium import webdriver

# список поддерживаемых браузеров
browsers_list = ['chrome', 'firefox']
# список поддерживаемых языков
langs_list = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi',
              'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru',
              'sk', 'uk', 'zh-cn']

# браузер и язык по умолчанию
default_browser, default_lang = 'chrome', 'ru'


# передачa параметров через командную строку
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=default_browser,
                     help=f'Choose correct browser: {browsers_list}')
    parser.addoption('--language', action='store', default=default_lang,
                     help=f'Choose corret language: {langs_list}')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_lang = request.config.getoption('language')

    # создание исключения при неверном вводе языка
    if browser_lang not in langs_list:
        raise Exception('Wrong language! List languages: ', *langs_list)

    # создание исключения при неверном вводе браузера
    if browser_name not in browsers_list:
        raise Exception('Wrong browser! List browsers: ', *browsers_list)

    print(f'\nStart {browser_name} browser..')

    # выбор и запуск браузера
    if browser_name == 'chrome':
        lng_opt = webdriver.chrome.options.Options()
        lng_opt.add_experimental_option(
            'prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=lng_opt)
    elif browser_name == 'firefox':
        lng_opt = webdriver.FirefoxProfile()
        lng_opt.set_preference("intl.accept_languages", browser_lang)
        browser = webdriver.Firefox(firefox_profile=lng_opt)

    yield browser
    print('\nQuit browser..')
    browser.quit()
