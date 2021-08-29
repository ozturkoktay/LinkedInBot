from driver_config import DriverOptions
from configuration import *
from typing import List
from log_manager import LogManager
from selenium.common.exceptions import TimeoutException
import random
import time


class ViewUserProfiles:

    def __init__(self):
        self.login_sleep_time = random.uniform(20, 30)
        self.linkedin_login_url = "https://linkedin.com/uas/login"
        self.config = DriverOptions()
        self.browser = self.config.set_browser()
        self.logger = LogManager("LinkedinViewLogger",
                                 "./logs/linkedin_view.log")
        self.login_linkedin(EMAIL, PASS)

    def split_position_name(self, titles: list) -> List[str]:
        """
        Split given position names by space.

        :param titles: given position name
        :type titles: list
        :return: list of words that are splitted
        :rtype: List[str]
        """
        return random.choice(titles).split()

    def sleep_in_minute(self, time_in_sec: int) -> int:
        """
        Convert float number to minutes.

        :param time_in_sec: float number to convert
        :type time_in_sec: int
        :return: converted number to minutes
        :rtype: int
        """
        return int(time_in_sec / 60)

    def login_linkedin(self, username: str, password: str) -> None:
        """
        Login linkedin.

        :param username: email adress for login to linkedin
        :type username: str
        :param password: password for login to linkedin
        :type password: str
        """
        try:
            self.logger.info("Logining to Linkedin account...")
            self.browser.get(self.linkedin_login_url)
            email_element = self.browser.find_element_by_id("username")
            pass_element = self.browser.find_element_by_id("password")
            email_element.send_keys(EMAIL)
            pass_element.send_keys(PASS)
            pass_element.submit()
            self.logger.info(
                f"Going sleep for {self.login_sleep_time} seconds.")
            time.sleep(self.login_sleep_time)
        except TimeoutException as e:
            self.logger.exception("Failed to login, REASON: ", e)

    def find_profiles(self) -> List[str]:
        """
        Find linkedin profiles parsing html.

        :return: unique profile links
        :rtype: list
        """
        elems = self.browser.find_elements_by_xpath(
            "//*[@class='app-aware-link']")
        links = [elem.get_attribute("href") for elem in elems]
        return list(set(links))

    def parse_position_title(self, titles: list) -> str:
        """
        Parse position title.

        :param titles: list of position titles
        :type titles: list
        :return: parsed position title
        :rtype: str
        """
        title = random.choice(titles).split()
        if len(title) > 0:
            return "%20".join(title)
        return random.choice(titles)

    def select_country(self, country: dict) -> int:
        """
        Select country.

        :param country: country to select
        :type country: dict
        :return: selected country
        :rtype: int
        """
        return random.choice(list(country.values()))

    def view_profiles(self) -> None:
        """View profiles."""
        index = 0
        for i in range(1, MAX_PAGE):
            page = f'https://www.linkedin.com/search/results/people/?geoUrn=%5B"{self.select_country(COUNTRIES)}"%5D' \
                   f'&keywords={self.parse_position_title(TITLES)}&page={i}&profileLanguage=%5B"en"%5D '
            self.browser.get(page)
            for idx, profile in enumerate(self.find_profiles()):
                quick_sleep_time = random.uniform(5, 10)
                iteration_sleep_time = random.uniform(500, 900)
                self.browser.get(profile)
                index += 1
                time.sleep(quick_sleep_time)
                self.logger.info(
                    f"VISITED PROFILE: {self.browser.current_url}")
                self.browser.get(page)
                self.logger.info(
                    f"Going sleep for {quick_sleep_time} seconds.")
                time.sleep(quick_sleep_time)
                if index % 20 == 0:
                    self.logger.info(
                        f"{index} profile viewed. Going next page.")
                    self.logger.info(
                        f"Going sleep for {self.sleep_in_minute(iteration_sleep_time)} minutes."
                    )
                    time.sleep(iteration_sleep_time)


instance = ViewUserProfiles()
instance.view_profiles()
