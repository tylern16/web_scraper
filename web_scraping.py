from bs4 import BeautifulSoup

import requests
import json

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.title
# print(tag.prettify())

# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, 'html.parser')

# prices = doc.find_all(text="$")

# parent = prices[0].parent

# strong = parent.find("strong")

# print(strong.string)



# .find("a")
# .find_all("a")

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")


# tags = doc.find_all(class_="btn-item", limit=3)

# print(tags)


# tags = doc.find_all("input")

# for tag in tags:
#     tag['placeholder'] = "i Change You!"

# with open("changed.html", "w") as file:
#     file.write(str.doc)



url = "https://www.eurosport.com/football/world-cup/2022/standings.shtml"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# # table = doc.table

# # tbodies = table.contents

# # tbodies = doc.find_all(class_="table-body")

# trs = doc.find_all(class_="table-body-row")

# trs = doc.find_all("tr", class_='bg-br-2-100')




# world_cup_data = {}

# for tr in trs:
#     team_name = tr.find(class_="absolute right-1 max-w-full truncate left-8 lg:caps-s5-fx hidden md:block").text

#     points = tr.find_all("td")[-2].text
    
#     world_cup_data[team_name] = points

# print(world_cup_data)

# class Team:
#     def __init__(self, name, position, wins, draws, losses, points):
#         self.name = name
#         self.position = position
#         self.wins = wins
#         self.draws = draws
#         self.losses = losses
#         self.points = points

world_cup_data = []

trs = trs = doc.find_all("tr", class_='bg-br-2-100')

for tr in trs:
    team_dict = {
        'team_name': f'{tr.find(class_="absolute right-1 max-w-full truncate left-8 lg:caps-s5-fx hidden md:block").text}',
        'position': f'{tr.find_all("td")[1].text}',
        'wins': f'{tr.find_all("td")[-8].text}',
        'draws': f'{tr.find_all("td")[-7].text}',
        'losses': f'{tr.find_all("td")[-6].text}',
        'points': f'{tr.find_all("td")[-2].text}'
    }
    

    # team = Team(team_name, position, wins, draws, losses, points)

    world_cup_data.append(team_dict)

# for i in range(0, len(world_cup_data)):
#     print(world_cup_data[i].name, world_cup_data[i].points)

json_string = json.dumps(world_cup_data)
# print(json_string)

with open('data.json', 'w') as f:
    f.write(json_string)

