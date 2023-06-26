from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


web = webdriver.Chrome()
web.get('https://ncrc.moj.gov.jo/')
time.sleep(2)

Nationality = 'اردني'
nation= web.find_element_by_xpath('//*[@id="cph_Base_cph_Child_ddlNationalityRequest_chosen"]')

nation.send_keys(Nationality)

the_ID_number = 9912016973
ide = web.find_element_by_class_name('riSingle RadInput RadInput_Default RadInputRTL RadInputRTL_Default')

ide.send_keys(the_ID_number)




bdate=4/5/1991
birth=web.find_element_by_class_name('riTextBox riEnabled')
bdate.send_keys(bdate)

lang='عربي'
language=web.find_element_by_xpath('//*[@id="cph_Base_cph_Child_ddlLanguage"]/option[3]')
lang.send_keys(lang)




first="ذكرى"
firstName=web.find_element_by_xpath('//*[@id="ctl00_ctl00_cph_Base_cph_Child_txtFirstName"]')
firstName.send_keys(first)



last="قرعان"
lastName=web.find_element_class_name('ctl00$ctl00$cph_Base$cph_Child$txtFamilyName')
lastName.send_keys(last)

purpose='جهات خارجية'
pu=web.find_element_class_name('جهات خارجية')
pu.send_keys(purpose)

fromwh ='محكمة بداية اربد'
fromWHere=web.find_element_class_name('محكمة بداية اربد')
fromWHere.send_keys(fromwh)

mobile =777924253
mobileN=web.find_element_class_name('form-control intlTelInput')
mobileN.send_keys(mobile)

email ='zekraquraan7@gmail.com'
email1=web.find_element_class_name('riTextBox riEnabled')
email1.send_keys(email)

code =''
code1=web.find_element_by_id('ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox')
code1.send_keys(code)






submit_button = web.find_element_by_xpath('//*[@id="cph_Base_cph_Child_btnRequest"]')




# # Wait for the element with the specified class name to be visible
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".chosen-single")))

# # Click on the element to open the dropdown
# element.click()

# # Find the option with the desired value and select it
# option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'اردني')]")))
# option.click()

# Extract the selected value (optional)
# selected_value = option.text
# print("Selected value:", selected_value)

# # Find the element with the specified ID
# national_number_field = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ctl00_cph_Base_cph_Child_txtNationalNumberRequest")))

# # Clear the field and enter the desired value
# national_number_field.clear()
# national_number_field.send_keys("9912016973")

# # Wait for the language dropdown to be visible
# language_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "cph_Base_cph_Child_ddlLanguage")))

# Select the desired language


# user_name = 9912016973
# user_pass = "ctl00_ctl00_cph_Base_cph_Child_txtNationalNumberRequest"

# user_name_input_field = driver.find_element(By.ID, "ctl00_ctl00_cph_Base_cph_Child_txtNationalNumberRequest")
# user_name_input_field.clear()
# user_name_input_field.send_keys(user_name)


# language_select = Select(language_dropdown)
# language_select.select_by_visible_text("عربي")

# # Find the first name field
# first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ctl00_cph_Base_cph_Child_txtFirstName")))
# if first_name_field.is_enabled():
#     first_name_field.send_keys("zekra")
# else:
#     print("The first name field is disabled.")


# # Enter the first name


# # Find the family name field
# family_name_field = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ctl00_cph_Base_cph_Child_txtFamilyName")))

# # Enter the family name
# family_name_field.send_keys("quraan")

# # Wait for the purpose dropdown to be visible
# purpose_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "cph_Base_cph_Child_ddlPurpose")))

# # Select the desired purpose
# purpose_select = Select(purpose_dropdown)
# purpose_select.select_by_visible_text("جهات خارجية")

# # Wait for the options to be present
# options_locator = (By.XPATH, "//select[@id='cph_Base_cph_Child_ddlCourt']//option")
# options = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(options_locator))

# # Find the desired option and click on it
# desired_option_text = "محكمة بداية اربد"
# for option in options:
#     if option.text == desired_option_text:
#         option.click()
#         break

# # Find the SMS field
# sms_field = wait.until(EC.visibility_of_element_located((By.ID, "cph_Base_cph_Child_txtSms")))

# # Enter the SMS value
# sms_field.send_keys("777924253")

# # Find the email field
# email_field = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ctl00_cph_Base_cph_Child_txtEmail")))

# # Enter the email value
# email_field.send_keys("zekraquraan7@gmail.com")

# # Find the captcha field
# captcha_field = wait.until(EC.visibility_of_element_located((By.ID,"ctl00_ctl00_cph_Base_cph_Child_CaptchaCodeTextBox")))


# captcha_field.send_keys("5FXPR")

# submit_button = driver.find_element_by_id("cph_Base_cph_Child_btnRequest")
# submit_button.click()


# wait.until(EC.url_contains("https://ncrc.moj.gov.jo/"))  

# Get the page source
# page_source = driver.page_source

# # Print all contents
# print("Page Contents:")
# print("https://ncrc.moj.gov.jo/")

# import time
# time.sleep(30) 
# Close the browser

