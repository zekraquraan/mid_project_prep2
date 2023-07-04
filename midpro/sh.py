from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button
from PIL import ImageTk, Image


# Start the Chrome browser and navigate to the URL
driver = webdriver.Chrome()
driver.get('https://ncrc.moj.gov.jo/')

# Wait for the nationality dropdown to be clickable
wait = WebDriverWait(driver, timeout=20)
nationality_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlNationalityRequest_chosen"]/a/div')))
nationality_input.click()

nationality_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlNationalityRequest_chosen"]/a/div')))
for option in nationality_options:
    if option.text == 'اردني':
        option.click()
        break

# Wait for the national number input field to be visible
ide_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cph_Base_cph_Child_txtNationalNumberRequest"]')))
ide_input.clear()
ide_input.send_keys('9912016973')

# Select the language from the dropdown
language_input = driver.find_element(By.ID, 'cph_Base_cph_Child_ddlLanguage')
language_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='عربي']")))
language_option.click()

date_of_birth = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_cph_Base_cph_Child_dtpBirthDate_dateInput')))
date_string = '1991/05/04'
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", date_of_birth, date_string)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", date_of_birth)


time.sleep(2)

# Wait for the first name input field to be visible
first_name_input = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_cph_Base_cph_Child_txtFirstName')))
first_name = 'ذكرى'
driver.execute_script("arguments[0].value = arguments[1]", first_name_input, first_name)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", first_name_input)
time.sleep(2)

# Enter the last name
last_name_input = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_cph_Base_cph_Child_txtFamilyName')))
last_name = 'قرعان'
driver.execute_script("arguments[0].value = arguments[1]", last_name_input, last_name)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", last_name_input)
time.sleep(2)

certifcated_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlPurpose"]/option[4]')))
certifcated_input.click()

certifacted_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlPurpose"]/option[4]')))
for option in certifacted_options:
    if option.text == 'جهات داخلية':
        option.click()
        break

time.sleep(2)

issued_from = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlCertificateFrom_chosen"]/a/span')))
driver.execute_script("arguments[0].scrollIntoView(true);", issued_from)
driver.execute_script("arguments[0].click();", issued_from)

# Wait for the dropdown to be visible and contain options
# wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cph_Base_cph_Child_ddlCertificateFrom_chosen"]/div/ul/li')))

# # Click the dropdown to open the options
# issued_options = driver.find_elements(By.XPATH, '//*[@id="cph_Base_cph_Child_ddlCertificateFrom_chosen"]/div/ul/li')
# issued_options[0].click()
# time.sleep(2)
# driver.execute_script("arguments[0].scrollIntoView(true);", issued_from)

wait = WebDriverWait(driver, 10)
mobile_input = wait.until(EC.presence_of_element_located((By.ID, 'cph_Base_cph_Child_txtSms')))
mobile_input.clear()  # Clear any existing value
mobile_input.send_keys('0777924253')
time.sleep(2)

email_input = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_cph_Base_cph_Child_txtEmail')))
e_mail = 'zekraquraan7@gmail.com'
driver.execute_script("arguments[0].value = arguments[1]", email_input, e_mail)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", email_input)
time.sleep(2)


info_element = driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cph_Base_cph_Child_captcha_CaptchaImage"]')
info_screenshot = info_element.screenshot_as_png
with open('info_screenshot.png', 'wb') as file:
            file.write(info_screenshot)


window = Tk()
window.title("Captcha Input")
window.geometry("300x150")

# Load the screenshot image
image = Image.open('info_screenshot.png')
photo = ImageTk.PhotoImage(image)
image_label = Label(window, image=photo)
image_label.pack()

# Create an input field
input_field = Entry(window)
input_field.pack()

def submit():
    user_input = input_field.get()
    # Do something with the user input
    print("User input:", user_input)
    # Close the GUI window after submitting
    captcha_input = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox')))
    captcha_input.send_keys(user_input)
    # window.destroy()
# Create a button to submit the input
    submit_button = driver.find_element(By.XPATH, '//*[@id="cph_Base_cph_Child_btnRequest"]')
    submit_button.click()
    window.destroy()
    
# Start the Tkinter event loop
submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()
window.mainloop()
time.sleep(5)
result_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html')))
result_text = result_element.text
print("Result:", result_text)
# Use the user input in the Selenium code
# iframe = driver.find_element(By.XPATH, '//*[@id="cph_Base_cph_Child_btnRequest"]')
# driver.switch_to.frame(iframe)

submit_button1 =driver.find_element(By.ID, 'cph_Base_cph_Child_btnRequest')

submit_button1.click()
# driver.switch_to.default_content()

# driver.implicitly_wait(10)  # Wait for 10 seconds for elements to appear

# window = Tk()
# image = Image.open('ws.png')
# photo = ImageTk.PhotoImage(image)
# image_label = Label(window, image=photo)
# image_label.pack()
# input_field = Entry(window)
# input_field.pack()


# def submit():
#     user_input = input_field.get()
#     # Do something with the user input
#     print("User input:", user_input)

# # Create a button to submit the input
# submit_button = Button(window, text="Submit", command=submit)
# submit_button.pack()

# # Start the Tkinter event loop
# window.mainloop()


# info_element = driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cph_Base_cph_Child_captcha_CaptchaImage"]')
# info_screenshot = info_element.screenshot_as_png
# with open('ws.png', 'wb') as file:
#    file.write(info_screenshot)

# html = '''
# <img id="ctl00_ctl00_cph_Base_cph_Child_captcha_CaptchaImage" alt="" src="Telerik.Web.UI.WebResource.axd?type=rca&amp;isc=true&amp;guid=76ba5c60-31b6-4431-bfc4-da15ef85f847" style="height:50px;width:180px;display:block;">
# <input id="ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox" name="ctl00$ctl00$cph_Base$cph_Child$CaptchaCodeTextBox" size="20" maxlength="6" class="riTextBox riEnabled" onpaste="return false" type="text" value="" autocomplete="off">
# '''

# soup = BeautifulSoup(html, 'html.parser')

# # Extract the image source
# image_src = soup.find('img', id='ctl00_ctl00_cph_Base_cph_Child_captcha_CaptchaImage')['src']
# print("Image Source:", image_src)

# # Extract the input element's ID and class
# input_id = soup.find('input', id='ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox')['id']
# input_class = soup.find('input', id='ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox')['class']
# print("Input ID:", input_id)
# print("Input Class:", input_class)

# Find and click the submit button
# submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'cph_Base_cph_Child_btnRequest')))
# submit_button.click()

# Wait for the page to load

# Get the page source (optional)
# page_source = driver.page_source
# print(page_source)

# Close the browser
# driver.quit()
