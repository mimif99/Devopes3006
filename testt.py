from selenium import webdriver

driver = webdriver.Chrome()
url = "https://hub.docker.com"
driver.get(url)
get_title = driver.title
if get_title == ["Docker Hub Container Image Library | App Containerization"]:
    print("the title is Docker Hub Container Image Library | App Containerization")
else:
    print("the title is not Docker Hub Container Image Library | App Containerization", get_title)

