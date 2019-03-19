from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")

section = soup.find("section", "section chart-grid")
li = section.div.ul
li_list = li.find_all("li")


top_song = []
for i in li_list:
    name = i.h3.string
    artist = i.h4.string
    play_list = OrderedDict({
        "Name": name,
        "Artist": artist,
    })
    top_song.append(play_list)

pyexcel.save_as(records = top_song, dest_file_name = "top_song.xlsx")
