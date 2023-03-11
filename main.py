import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException 



class tinderbot():
    URL = 'https://tinder.onelink.me/9K8a/3d4abb81'

    def __init__(self):
        # 1. Navigate to tinder web app
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.URL)
        # driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login(self):
        # 2. Login to account
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]').click()

        # 2.1 Verify user
        try:
            self.driver.implicitly_wait(10)
            # verify = driver.find_element(By.CLASS_NAME, 'sc-bdnxRM')
            # verify = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button')
            verify = self.driver.find_element(By.ID, 'home_children_button')
            print(verify.text)
        except NoSuchElementException:
            print('ERROR: Element not found')
        finally:
            print('End script')

    def quit():
        print('~~~~~ Script complete ~~~~~')
        self.driver.quit()



if __name__ == '__main__':
    bot = tinderbot()
    bot.login()

