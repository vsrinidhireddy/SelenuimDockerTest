
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

try:
    driver.get("http://webapp:8000/Seleniumtest.html")

    wait = WebDriverWait(driver, 15)

    print("Page title:", driver.title)
    print("Current URL:", driver.current_url)

    name = wait.until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    name.send_keys("Srinidhi")

    email = driver.find_element(By.ID, "email")
    email.send_keys("srinidhi@gmail.com")

    driver.find_element(By.ID, "registrationForm").submit()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    if message.text == "Registration Successful!":
        print("TEST PASSED: Registration Successful")
    else:
        print("TEST FAILED")

finally:
    driver.quit()
