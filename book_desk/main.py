from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(50)
file = open('log.txt', 'w', encoding="utf-8")

driver.get("https://synopsys.iwmsapp.com/archibus/schema/ab-products/essential/jll-workplace.axvw")
# wait = WebDriverWait(driver, 60)

# Find the element with inner text "RESERVE WORKSPACE" and click it
html = driver.page_source

print("a", html, file=file)

element = driver.find_element(By.XPATH, '//div[contains(text(), "RESERVE WORKSPACE")]')

# element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="service-card-title"]')))

element.click()

html = driver.page_source
print("b", html, file=file)

driver.quit()
file.close()
