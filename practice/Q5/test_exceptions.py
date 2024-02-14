from time import sleep
import logging
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
fh = logging.FileHandler("Q5/except_log.log")
frmt = logging.Formatter("%(asctime)s : %(name)s : %(message)s")
fh.setFormatter(frmt)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

@pytest.fixture
def browser():
    # Initialize WebDriver instance (replace 'chrome' with your desired browser)
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Close the browser after the test
    driver.quit()


def test_selenium_search(browser):
    try:
        # Navigate to the webpage
        browser.get("https://www.google.com")
        sleep(5)
        logger.info("opening url....")
        # Find the search input element
        search_input = browser.find_element(By.NAME, "q")

        # Type the search query
        logger.info("entering text in search bar....")
        search_input.send_keys("pytest")
        search_input.send_keys(Keys.ENTER)

        # Find and click the search button
        # search_button = browser.find_element(By.NAME, "btnK")
        # search_button.click()
        sleep(5)

        # Verify search results page
        logger.info("testing the browser title....")
        assert "pytest" in browser.title
    except TimeoutException as e:
        # Handle timeout exception
        pytest.fail(f"Timeout: Search page did not load within 10 seconds: {e}")
    except NoSuchElementException as e:
        # Handle element not found exception
        pytest.fail(f"Search input or button not found: {e}")
    except Exception as e:
        # Handle any other exceptions
        pytest.fail(f"An unexpected error occurred: {str(e)}")