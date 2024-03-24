from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.example.com Find the input field by XPath
input_field = driver.find_element(By.XPATH, "//input[@id='username']")

# Enter text into the input field
input_field.send_keys("username")
