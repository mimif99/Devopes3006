from selenium import webdriver
#from time import sleep
my_driver = webdriver.Chrome(executable_path="c:/Windows/System32/chromedriver.exe")
my_driver.get("c:/Users/mimi/Downloads/tip_calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "3.00"
actual = my_driver.find_element(by="id", value="tip").text

assert expected == actual


