from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge browser")
    return driver



def pytest_addoption(parser):         #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the Browser value to setup method
    return request.config.getoption("--browser")

# It is hook for  adding environment info to html report

def pytest_configure(config):
    config._metadata["Project Name"] = "nop commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester Name"] = "savitha"

# It is hook for  removing/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)