from  selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:63342/HRXT/HRXT/uidriver/213.html")
a = driver.find_element_by_id("boy").is_selected()
print(a)
driver.find_element_by_id("boy").click()
b = driver.find_element_by_id("boy").is_selected()
print(b)

c = driver.find_element_by_id("c1").is_selected()
print(c)

driver.find_element_by_id("c1").click()

d = driver.find_element_by_id("c1").is_selected()
print(d)