from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument(r"user-data-dir=C:\Users\gkerr\AppData\Local\Google\Chrome\User Data\Ninja")
driver = webdriver.Chrome(executable_path=r'C:\Users\gkerr\Desktop\vs-code\webscraping\chromedriver.exe', options=chrome_options)

driver.get("https://gg.bet/en/")

#my_variable = driver.find_element_by_xpath('')
#my_variable.click()
sleep(3)
img = pyautogui.screenshot()

img.save(r'screenshots\file name.png')
sleep(1)
driver.close()
