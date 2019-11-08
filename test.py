from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import login_config

user_name = login_config.username
password = login_config.password
executable_path = '/home/sharang/PycharmProjects/test'

os.environ["PATH"] += os.pathsep + executable_path

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/login")
element = driver.find_element_by_id("username")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
#element.close()

wait = WebDriverWait(driver, 10)


#driver.get('https://www.linkedin.com/voyager/api/messaging/peripheral/messagingSearchHistory?q=type')
driver.get('https://www.linkedin.com/messaging/thread/6594995304859348993/')
driver.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fmessaging%2Fthread%2F6594995304859348993%2F&fromSignIn=true&trk=uno-reg-join-sign-in')
element = driver.find_element_by_id("username")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)

driver.find_elements_by_css_selector(".msg-form__contenteditable")[0].send_keys('anoother test')
driver.find_elements_by_css_selector(".js-msg-close").click()
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js-msg-close")))
