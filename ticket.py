from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration for headless mode (optional)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# Instantiate the driver
driver = webdriver.Chrome('./chromedriver', options=options)

try:
    # Open the website
    driver.get('YOUR_TARGET_URL')

    # Wait for the element to be clickable and then click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="e3_buy"]/span'))
    ).click()

    # Log in
    account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]'))
    )
    account.clear()
    account.send_keys('YOUR_USERNAME')

    password = driver.find_element_by_xpath('//*[@id="j_password"]')
    password.clear()
    password.send_keys('YOUR_PASSWORD')

    driver.find_element_by_xpath('//*[@id="login_btn"]').click()

    # Fill in details after login
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="billingname"]'))
    )
    name.clear()
    name.send_keys('YOUR_NAME')

    phone = driver.find_element_by_xpath('//*[@id="billingmobile"]')
    phone.clear()
    phone.send_keys('YOUR_PHONE')

    email = driver.find_element_by_xpath('//*[@id="billingemail"]')
    email.clear()
    email.send_keys('YOUR_EMAIL')

    city = driver.find_element_by_xpath('//*[@id="addConsigneeCityId2"]')
    city.send_keys('YOUR_CITY')

    year = driver.find_element_by_xpath('//*[@id="birthday_year"]')
    year.send_keys('YOUR_BIRTH_YEAR')

    month = driver.find_element_by_xpath('//*[@id="birthday_month"]')
    month.send_keys('YOUR_BIRTH_MONTH')

    day = driver.find_element_by_xpath('//*[@id="birthday_day"]')
    day.send_keys('YOUR_BIRTH_DAY')

    address = driver.find_element_by_xpath('//*[@id="address3"]')
    address.send_keys('YOUR_ADDRESS')

    cvc = driver.find_element_by_xpath('//*[@id="creidtcard_record_area_default"]/div/div[2]/input[2]')
    cvc.clear()
    cvc.send_keys('YOUR_CARD_CVC')

    # Select gender (update the selector as needed)
    driver.find_element_by_xpath('//*[@id="gender1"]').click()

    # Clicking other required fields (update selectors as needed)
    driver.find_element_by_xpath('//*[@id="same"]').click()
    driver.find_element_by_xpath('//*[@id="same2"]').click()
    driver.find_element_by_xpath('//*[@id="use3d"]/input[2]').click()

    # Add any additional interactions here

    # Close the browser after the operation
    driver.quit()

except Exception as e:
    print("An error occurred:", e)
    driver.quit()  # Make sure to close the browser even if an error occurs
