from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Set up the Chrome WebDriver service
DRIVER_PATH = r'C:\Users\Sarah\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
CHROME_PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

class Info:
    def __init__(self):
        self.service = Service(executable_path=DRIVER_PATH)

        # Chrome options
        self.options = Options()
        self.options.binary_location = CHROME_PATH

        # Chrome WebDriver
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        # Find the search bar element by name
        search_box = self.driver.find_element(By.NAME, "search")

        # Enter the query and submit the form
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        element = self.driver.find_element(By.ID, "mw-content-text")
        paragraph = element.find_elements(By.XPATH, '//p')
        print(paragraph[1].text)
        print(paragraph[2].text)
        

