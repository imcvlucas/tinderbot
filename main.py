import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC



class tinderbot():
    # URL = 'https://tinder.onelink.me/9K8a/3d4abb81'
    URL = 'https://tinder.com/'

    def __init__(self):
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def close_cookie_option(self):
        # time.sleep(3)
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button')))
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()

    def login(self):
        self.close_cookie_option()

        # Click login button
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

        # Click login with phone
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button')))
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button').click()

        # Verify user
        try:
            WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/button')))
            # verify = driver.find_element(By.CLASS_NAME, 'sc-bdnxRM')
            # verify = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button')
            # verify = self.driver.find_element(By.ID, 'home_children_button')
            # print(verify.text)
        except NoSuchElementException:
            print('ERROR: Element not found')

    def quit():
        print('~~~~~ Script complete ~~~~~')
        self.driver.quit()



if __name__ == '__main__':
    bot = tinderbot()
    bot.login()
