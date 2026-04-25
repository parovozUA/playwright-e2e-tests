import pytest
import allure
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(autouse=True)
def enrich_report(browser):
    browser_version = browser.version

    allure.dynamic.parameter("browser_version", browser_version)


# allure screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"screenshot_{datetime.now().isoformat()}",
                attachment_type=allure.attachment_type.PNG
            )
