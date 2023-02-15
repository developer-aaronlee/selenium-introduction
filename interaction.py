from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = Service("/Applications/chromedriver")
driver = webdriver.Chrome(service=chrome_driver)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# wikipedia_article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, "Contents")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("python")
# search_bar.send_keys(Keys.ENTER)


driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("aaron")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("lee")
email = driver.find_element(By.NAME, "email")
email.send_keys("abc123@email.com")
# submit = driver.find_element(By.TAG_NAME, "button")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()


# driver.quit()