from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

uri_list = [
    {
        "pid": "8008970041094",
        "uri": "https://www.canva.com/design/DAD5ZlPn4wA"
    }
]

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\eugen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
options.add_argument("profile-directory=Profile 1")
driver = webdriver.Chrome(executable_path="I:\\chromedriver.exe", options=options)

for entry in uri_list:
    currenturi = entry["uri"]
    print(currenturi)
    print("-----------------------------------------")
    driver.get(currenturi)
    print("Clicking on 'Download' button")
    button = driver.find_element_by_xpath("//button[@aria-pressed='false']")
    button.click()
    print("Clicking on dropdown")
    button2 = driver.find_element_by_xpath("//span[@class='HngW0A']")
    button2 = driver.find_element_by_xpath("//span[@class='HngW0A']")
    driver.implicitly_wait(50)
    button2.click()
    print("Clicking on 'JPG' button")
    button3 = driver.find_element_by_xpath("//div[text()='JPG']")
    button3.click()
    driver.implicitly_wait(200)
    print("Waiting and clicking on the 'Download' button")
    button4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ehVb1g']")))
    button4.click()
    #print("Waiting for 'Download' button")
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_8VoL_g']"))).click()
    #print("Clicking on 'Download' button")
    #button4 = driver.find_element_by_xpath("//div[@class='_8VoL_g']")
    #driver.implicitly_wait(500)
    #button4.click()
    print("\n")
    driver.execute_script('''window.open("chrome://newtab","_blank");''')
