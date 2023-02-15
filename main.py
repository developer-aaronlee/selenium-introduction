from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver = Service("/Applications/chromedriver")
driver = webdriver.Chrome(service=chrome_driver)

# driver.get("https://www.amazon.com/2022-Apple-iPad-10-9-inch-Wi-Fi/dp/B09V3HN1KC/ref=sr_1_3?crid="
#            "HFXQMWBTRAKV&keywords=iPad+Air&qid=1660613755&sprefix=ipad+air%2Caps%2C78&sr=8-3")

# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute("textContent"))

# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.text)


driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# doc_link = driver.find_element(By.CSS_SELECTOR, ".small-widget.documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

# all_small_widgets = driver.find_elements(By.CLASS_NAME, "small-widget")
# small_widgets_list = [x.text for x in all_small_widgets]
# print(small_widgets_list)

event_dates = [x.text for x in driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last time")]
# print(event_dates)
event_names = [x.text for x in driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last ul a")]
# print(event_names)

# event_dic = {}
# for x in range(len(event_dates)):
#     event_dic[x+1] = {
#         "time": event_dates[x],
#         "name": event_names[x]
#     }
# print(event_dic)

event_dic = {x+1: {event_dates[x]: event_names[x]} for x in range(len(event_dates))}
print(event_dic)





# driver.close()
driver.quit()



