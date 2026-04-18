import pytest


@pytest.fixture(scope="session", autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")