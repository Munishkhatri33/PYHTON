#code starts from here
#guys this is the only script which is working on google colab
#guys if you want to donate me please give me a google playstore reedem code at munishkhatri33@gmail.com
#guys i am a student in 11th non-medical currently studying in suraj school bawal


import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 35

#youtube link
link = 'https://youtu.be/9v8VD11-Zpw'

#number of views
views = 9999

driver = webdriver.Chrome('chromedriver',options=options)
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
