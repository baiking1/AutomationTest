from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Go to BaiDu
driver = webdriver.Ie()
#driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
element = WebDriverWait(driver,10,0.5).until(
                    EC.presence_of_element_located((By.ID,"kw"))
                    )

# Set browser size
driver.set_window_size(800,600)

# Search
driver.find_element_by_id("kw").send_keys("robotframework")
sleep (2)
driver.find_element_by_id("su").click()
sleep (2)
# set up scroll's location
js="window.scrollTo(100,450);"
driver.execute_script(js)
sleep (10)

driver.quit()
