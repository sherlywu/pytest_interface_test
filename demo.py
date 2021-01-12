from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://49.233.108.117:3000/')

# 针对单个元素设置显示等待
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav pull-right"]/li[2]')))
driver.find_element(By.XPATH, '//ul[@class="nav pull-right"]/li[2]').click()
