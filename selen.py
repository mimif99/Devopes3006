from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.ycombinator.com/"
driver.get(url)
get_title = driver.title
if get_title == "Y Combinator":
    print("The title is Y Combinator")
else:
    print("The title is not Y Combinator", get_title)
