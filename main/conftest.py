import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge"
        # default browser is set as chrome,the --browser_name should be same with the --browser_nam in cmd
    )
    parser.addoption(
        "--username", action="store", default="saheli.mondal0398@gmail.com"
    )

    parser.addoption(
        "--pass", action="store", default="Lokenathbaba@03"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(chrome_options=option, executable_path=r"C:\Users\Saheli "
                                                                     r"Mondal\Downloads\chromedriver_win32 ("
                                                                     r"2)\chromedriver.exe")
    driver.get('https://www.facebook.com')
    driver.maximize_window()

    request.cls.driver = driver


@pytest.fixture(scope="class")
def get_username(request):
    username = request.config.getoption("username")
    print(get_username)
    return username


@pytest.fixture(scope="class")
def get_password(request):
    password = request.config.getoption("pass")
    print(get_password)
    return password
