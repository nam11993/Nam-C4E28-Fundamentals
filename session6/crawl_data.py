# 1. creat connection
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url ="https://dantri.com.vn"
conn = urlopen(url)

# 2. Download page
raw_data = conn.read()
html_content = raw_data.decode("utf-8")

with open("dantri.html", "wb") as f:
    f.write(raw_data)

# #3 Find ROI
# soup = BeautifulSoup(html_content, "html.parser")
# ul = soup.find("ul","ul1 ulnew")


# li_list = ul.find_all("li")
# new_list =[]
# for i in li_list:
#     h4 = i.h4
#     a = h4.a 
#     title = a.string
#     link = url + a["href"]
#     print(link)

#     news =  OrderedDict({
#         "Title": title,
#         "Link": link
#     })
#     new_list.append(news)


# pyexcel.save_as(records=new_list, dest_file_name="dantri1.xlsx")





    