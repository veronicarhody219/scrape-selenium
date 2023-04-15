from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys
import pandas as pd
websites = []
titles=[]
subtitles=[]
links=[]
imgs = []

for i in range (10):
    if i == 0:
        website = 'https://ngoisao.vnexpress.net/trac-nghiem'
        websites.append(website)
    else:
        website = f'https://ngoisao.vnexpress.net/trac-nghiem-p{i}'
        websites.append(website)
print(websites)
options = Options()
options.headless = True
path = '/Users/veronicarhody/Desktop/pma/python/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)



for website in websites:
    driver.get(website)
   
    
    title_containers = driver.find_elements(by='xpath', value="//div[@class='content']/h2/a")
    link_containers = driver.find_elements(by='xpath', value="//div[@class='content']/h2/a")
    subtitle_containers=driver.find_elements(by='xpath', value="//div[@class='description']")
    img_containers = driver.find_elements(by='xpath', value="//img[contains(@class, 'lazy loading')]")

    for container in title_containers:
        container = container.text
        if len(container) > 3:
            titles.append(container)
    for link in link_containers:
        link = link.get_attribute("href")
        if "box_comment" not in  link:
            links.append(link)
    for img in img_containers:
        img = img.get_attribute('src')
        imgs.append(img)    
    for subtitle in subtitle_containers:
        subtitle = subtitle.text
        subtitles.append(subtitle)

# print(len(titles))
# print(len(subtitles))
# print(len(imgs))
# print(len(links))
# print(titles)
# print(imgs)
# print(links)

my_dict = {'title':titles, 'link':links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.dropna(axis = 0, how='all')
application_path = os.path.dirname(sys.executable)
now = datetime.now()
now.strftime('%d%m%Y')
file_name = f'headlines-{now}.csv'
file_name_excel = f'headlines-{now}.xlsx'
file_name_json = f'headlines-{now}.json'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(file_name)
df_headlines.to_excel(file_name_excel)
df_headlines.to_json('quiz.json')
driver.quit()
