from configuration import HEADLESS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverOptions:
    """Options for web browser."""

    CHROME_DRIVER_PATH = 'drivers/chromedriver'

    def __init__(self):
        self.options = Options()

    def all_options(self) -> dict:
        """Set selenium browser options."""
        if HEADLESS:
            self.options.headless = True
        self.options.add_argument('disable-infobars')
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--disable-logging')
        self.options.add_argument("--remote-debugging-port=9222")
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument(
            "--disable-blink-features=AutomationControlled")
        # options.add_argument('--proxy-server=socks5://localhost:9050')
        return self.options

    def set_browser(self):
        """Set browser."""
        return webdriver.Chrome(executable_path=self.CHROME_DRIVER_PATH, options=self.all_options())
