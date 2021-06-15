import pytest
from selenium import webdriver

driver = None


# -------------------------------------------------------------------------------
# Jenkins config = copy and paste project path in Advance->custom workspace->Add Path
# Parameterized-> select this project is paramiterized->choice Parameter->
# Enter Browser and in choices field->chrome,firefox,edge
# Build->Execute windows batch command if u are windows->
# cd TestCases
# py.test --browser_name %BrowserName% --html=$WORKSPACE\Reports\reports.html -v --junitxml="result.xml"
# -------------------------------------------------------------------------------


# run with different browser py.test --browser_name chrome/firefox/edge

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Drivers\\BrowserDriver\\Firefoxdriver\\geckodriver")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\Drivers\\BrowserDriver\\edgedriver_win64\\msedgedriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(6)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
