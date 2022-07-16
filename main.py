from selenium import webdriver
from selenium.webdriver import FirefoxProfile
import time



def openAmazon():
    profile = FirefoxProfile()
    profile.set_preference('browser.cache.disk.enable', False)
    profile.set_preference('browser.cache.memory.enable', False)

    fireFoxOptions = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(executable_path=r'geckodriver.exe', firefox_profile=profile,
                               options=fireFoxOptions)
    # driver=webdriver.Chrome(executable_path=r'C:\Users\AA\Headless\chromedriver.exe')
    URL = "https://www.amazon.com/"

    driver.get(URL)
    return driver

def reload(driver:webdriver):
    RELOAD_URL='https://www.amazon.com/gp/product/B086KKT3RX'
    driver.get(RELOAD_URL)
    amount=driver.find_element_by_name("oneTimeReloadAmount")
    driver.execute_script("arguments[0].scrollIntoView();", amount)
    amount.send_keys("0.5")
    buy_button=driver.find_element_by_class_name("a-button-oneclick")
    driver.execute_script("arguments[0].scrollIntoView();", buy_button)
    buy_button.click()

    try:
        continue_button=driver.find_element_by_class_name("a-button-primary")
        driver.execute_script("arguments[0].scrollIntoView();", continue_button)
        continue_button.click()
    except:
        print("no continue")

    time.sleep(5)
    place_order_button = driver.find_element_by_name("placeYourOrder1")
    driver.execute_script("arguments[0].scrollIntoView();", place_order_button)
    place_order_button.click()
def main():
    driver=openAmazon()
    input("Please sign in. After log in successfully, press Enter")
    amount_text=input("Total amount you want to load?")
    amount_num=float(amount_text)
    times=amount_num//0.5
    count=1
    for i in range(times):
        reload(driver)
        print("have loaded "+str(count*0.5)+"dollars")
        count+=1




if __name__=='__main__':
    main()