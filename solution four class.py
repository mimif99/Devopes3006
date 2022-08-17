import requests
import names
from selenium import webdriver

# 1
print("\n\n solution 1\n ")
response = requests.get("https://api.github.com/users/avielb/repos")

repos_list = [repo["full_name"] for repo in response.json() if repo["private"] == False]

for repo in repos_list:
    print(repo)

# 2
print("\n \n solution 2\n ")

# must install names library


for i in range(3):
    rand_name = names.get_first_name()
    response = requests.get("https://api.agify.io/?name=" + rand_name)
    ages = response.json()
    if ages["age"] >= 120 & ages["age"] >= 0:
        print(rand_name, "valid, age", ages["age"])
    else:
        print("not good ", rand_name)

# 3
print(" \n \n solution 3\n ")

uni_list = []
data = requests.get("http://universities.hipolabs.com/search?country=Israel").json()

for i, uni in enumerate(data):
    if "University" in uni["name"]:
        uni_list += [uni["name"]]
if len(uni_list) > 5:
    print("list larger then 5, list length: ", len(uni_list))
else:
    print("list smaller then 5, list length: ", len(uni_list))

for i, uni in enumerate(uni_list):
    print(i, "-", uni)

# 4
print("\n \n solution 4\n ")

driver = webdriver.Chrome()
url = "https://www.ycombinator.com/"
driver.get(url)
get_title = driver.title
if get_title == "Y Combinator":
    print("The title is Y Combinator")
else:
    print("The title is not Y Combinator", get_title)

#5
print(" \n \n solution 5\n ")

driver = webdriver.Chrome()
url = "https://hub.docker.com"
driver.get(url)
get_title = driver.title
if get_title == "Docker Hub Container Image Library | App Containerization":
    print("the title is Docker Hub Container Image Library | App Containerization")
else:
    print("the title is not Docker Hub Container Image Library | App Containerization", get_title)

