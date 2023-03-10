import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException 



# 1. Navigate to tinder web app
URL = 'https://tinder.onelink.me/9K8a/3d4abb81'

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(URL)
# driver.maximize_window()
time.sleep(5)

# 2. Login to account
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]').click()
time.sleep(5)

# 2.1 Verify user
try:
    verify = driver.find_element(By.CLASS_NAME, 'sc-bdnxRM')
    print(verify.text)
except NoSuchElementException:
    print('x Element not found')
finally:
    print('End script')

# if driver.find_element(By.CLASS_NAME, 'sc-bdnxRM kkVpCJ sc-kEqXSa'):
#     # verify = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button/svg')
#     # verify = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button')
#     # verify = driver.find_element(By.XPATH, '//*[@id="home_children_button"]')
#     verify = driver.find_element(By.CLASS_NAME, 'sc-bdnxRM kkVpCJ sc-kEqXSa')
#     print(verify.text)
#     verify.click()
#     print('3. Clicked verify button')
# else:
#     print('Element not found!')


print('~~~~~ Script complete ~~~~~')
# Close webdriver
driver.quit()
