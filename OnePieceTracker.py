from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
 
# Create webdriver object in kiosk mode
options = webdriver.FirefoxOptions()
options.add_argument('-kiosk')
driver = webdriver.Firefox(options=options)
 
# Go to mangaplus page
driver.get("https://mangaplus.shueisha.co.jp/error")
time.sleep(2.5)

# Search for One Piece (sometimes the page doesn't work, so we are going to repeat this)
tries = 0;
found = False
while (found == False):
    tries += 1

    try:
        # We try clicking on the first manga
        charge = driver.find_element(By.XPATH, "//p[starts-with(@class, 'AllTitle-module_title_')]")
        charge.click()
        
        found = True
    except NoSuchElementException:
        # If there is not, we execute:
        search = driver.find_element(By.XPATH, "//input[@placeholder='Search by title or author']")
        search.click()
        search.send_keys("One Piece")
        time.sleep(2)
        search.send_keys('\ue006')
        time.sleep(3)

time.sleep(5)

# We search for the last chapters
invert = driver.find_elements(By.CSS_SELECTOR, ('img[alt="sort"][class^="ChapterList-module_sortIcon_"]'))
invert_ = invert[0]
invert_.click()

# We get the number of the last chapter
last = driver.find_element(By.XPATH, "//p[starts-with(@class, 'ChapterListItem-module_title_')]")
last_chapter = last.text
number_chapter = (last_chapter.split()[1]).rstrip(":")

print(number_chapter)
 

driver.quit()
