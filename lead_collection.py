import sys
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
chrome_options = Options()
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/?hl=en")
time.sleep(10)
driver.refresh()
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Laptop shop near Mirpur")
search_box.send_keys(Keys.RETURN)
time.sleep(30)
driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div[1]/div[1]/div/div[2]/a').click()
time.sleep(30)
select_place = driver.find_element(By.CLASS_NAME,'Ntshyc')
action = ActionChains(driver)
action.move_to_element(select_place).click().perform()
scroll_div = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
height = driver.execute_script('return arguments[0].scrollHeight',scroll_div)
for i in range(0,height+1500,30):
    driver.execute_script("arguments[0].scrollTop = arguments[1]", scroll_div, i)
    time.sleep(0.2)
get_add_leads = driver.find_elements(By.CLASS_NAME,'UaQhfb')
store_phone_number = []
for i in get_add_leads:
    match_pattern = re.findall("\d{5}-\d{6}", i.text)
    if match_pattern:
        store_phone_number.append(match_pattern[0])
print(store_phone_number)       
    
driver.quit()