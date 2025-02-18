import sys
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get('https://www.daraz.com.bd/products/3-i316734118-s1434548589.html?pvid=2e6f9c66-99d9-48db-bdc6-27aaad2de32f&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335411.just4u.d_316734118')

height = driver.execute_script('return document.body.scrollHeight')


for i in range(0,height,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)


wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div')))

global element
element = None
store_comments = {}
last_page = driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]')
total_page = int(last_page.text)
for i in range(1,total_page+1):
    wait = WebDriverWait(driver, 10)
    if(i>=4 and i<total_page):
        j='4'
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{j}]')
    elif(i==total_page):
        element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]')
    else:
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')

    all_comment = driver.find_elements(By.CLASS_NAME,'content')
    comment_list=[]
    for index,comment in enumerate(all_comment):
        if not index==0:
            comment_list.append(comment.text)
    store_comments[f"Page-{i}"]=comment_list
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)

print(store_comments)
time.sleep(5)
driver.quit()