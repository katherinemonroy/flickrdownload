
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/katherinemonroy/Downloads/chromedriver')

website = input("Enter your flickr link gallery: ")


driver.get(website) # goes to flickr gallery

# Looks like the cookie button got removed so i dont use this function but i have it jsut in case it comes back
def byecookies(): # closes the cookie thing at the bottom of the page
    time.sleep(5) # waits 5 seconds for page to load
    cookiebutton = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/a')
    cookiebutton.click() # closes the cookie thing at the bottom of the page


def betterview(): # switches to thumbnail view i believe and shows 2 columns of 50 images total
    time.sleep(2) # waits to seconds
    viewbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section[2]/header/div[2]/a[2]')
    viewbutton.click()
betterview()

def scrollpage(): #scrolls to the bottom of the page
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
scrollpage()


#gets photo links and puts them into a list
elems = driver.find_elements_by_tag_name('a.click-target')
photolink =[]
for elem in elems:
    href = elem.get_attribute('href')
    photolink.append(href)
    if href is not None:
        print(len(photolink))
        #MAYBEFIX: make 310 a value that can be changed based on link * not really necessary ngl

        if 310 == (len(photolink)):
            print("equal")
time.sleep(3)
count = 0
#goes to each photos size page and gets the src link
for eachphoto in photolink:
    count +=1
    driver.get(eachphoto)
    time.sleep(2)
    #clicks on download button
    assert 'photos' in driver.current_url
    downloadbutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'download ')))
    downloadbutton.click()
    time.sleep(2)
    #go to size page
    sizebutton = driver.find_element_by_css_selector('a.all-sizes.server-only-link')
    sizebutton.click()
    time.sleep(2)

    #gets src links from current page
    onlies = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/img")
    srclinks =[]

    # goes to src link and takes a screenshot
    for only in onlies:
        src = only.get_attribute("src") # gets src link
        srclinks.append(src) # adds src to list
        driver.get(src) #goes to src link
        #numbers the screenshot [1screenshot.png, 2screenshot.png,3screenshot.png,]
        driver.get_screenshot_as_file((str(count))+"screenshot.png")




driver.quit()
print("end...")
