from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from api.logic import *
from selenium.webdriver.chrome.options import Options

def create_webdriver_instance():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("start-maximized")  
    chrome_options.add_argument("disable-infobars")  
    chrome_options.add_argument("--disable-extensions")  


    driver = webdriver.Chrome(options=chrome_options)
    return driver






def scrapeSingleNewsletter(url):
    driver = create_webdriver_instance()
    driver.get(url)

    time.sleep(1)

    content_blocks = driver.find_element(By.ID, "content-blocks")
    all_text = content_blocks.text
    print(all_text)
    return all_text

def scrapeNewsletterPosts(url):
    driver = create_webdriver_instance()
    driver.get(url)
    time.sleep(1)

    
    while True:
        try:
           
            load_more_button = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[style="color:#222222"].text-lg.sm\\:text-xl.font-regular.wt-body-font'))
            )

           
            if load_more_button.text == "Load More":
                load_more_button.click()
                print("Clicked 'Load More' button.")
                time.sleep(1)  
            else:
                print("'Load More' button found, but text does not match.")
                break  

        except TimeoutException:

            print("'Load More' button not found. All content loaded.")
            break
    
    

    links = driver.find_elements(By.CSS_SELECTOR, 'a.group.flex.h-full.w-full.border')

    hrefs = []

    for link in links:
        href = link.get_attribute('href')
        hrefs.append(href)

    newsletter_data = []

    for href in hrefs:
        scrapeSingleNewsletter(href)
        text = scrapeSingleNewsletter(href)  
        newsletter_item = {'url': href, 'text': text}  
        newsletter_data.append(newsletter_item) 
        
    driver.quit()

    return newsletter_data

