import cv2, mss, mss.tools, cv2, imutils, pyautogui, numpy as np
from pytesseract import pytesseract
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument(r"user-data-dir=C:\Users\gkerr\AppData\Local\Google\Chrome\User Data\Ninja")
driver = webdriver.Chrome(executable_path=r'C:\Users\gkerr\Desktop\vs-code\webscraping\chromedriver.exe', options=chrome_options)


driver.get("https://gg.bet/en/")
sleep(3)
img = pyautogui.screenshot()
img.save(r'screenshots\file name.png')
sleep(1)
driver.close()

img = cv2.imread('screenshots\image.png', cv2.IMREAD_GRAYSCALE)
#img = img[450:550, 1100:1600]
img_cut = img[200:800, 300:1600]
cv2.imshow('img',img_cut)
cv2.waitKey(0)
cv2.destroyAllWindows()

blurred = cv2.GaussianBlur(img_cut, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
ret,thresh = cv2.threshold(img_cut,85,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img_cut,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
ret3,th3 = cv2.threshold(img_cut,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None


pytesseract.tesseract_cmd = r"F:\Program Files\Tesseract-OCR\tesseract.exe"
data = pytesseract.image_to_string(th3)
data = list(data)
data = [x for x in data if x.isdigit()]

team1 = data[0:int(len(data)/2)]
team2 = data[int(len(data)/2):len(data)]
team1.insert(1,'.')
team2.insert(1,'.')
team1 = ''.join(map(str,team1))
team2 = ''.join(map(str,team2))
print(team1)
print(team2)









thresh = imutils.resize(thresh, width=700)
th3 = imutils.resize(th3, width=700)

cv2.imshow('OTSU',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()