import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".storylink")
subtext = soup.select(".subtext")

def sorted_by_votes(list):
	return sorted(list, key= lambda k:k["votes"], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for i, item in enumerate(links):
		title = item.getText()
		href = item.get("href", None)
		vote = subtext[i].select(".score")
		if len(vote):
			points = int(vote[0].getText().replace(" points", ""))
			if points > 199:
				hn.append({"title": title, "link": href, "votes": points})
	return sorted_by_votes(hn)

#pprint.pprint(create_custom_hn(links, subtext))

final_list = create_custom_hn(links, subtext)

for link in final_list[:5]:
	pres = f"""Title : {link["title"]} \nLink : {link["link"]} \nNb Votes : {link["votes"]} \n"""
	print(pres)