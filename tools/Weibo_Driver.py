
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image,ImageEnhance

def geturl(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    #browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(8)
    try:
        #填写微博真实账户名和密码
        browser.find_element_by_css_selector("#loginname").send_keys(
            "微博账户名")
        browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys(
            "密码")
        browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
        time.sleep(5)
    except:
        print("no login")
        time.sleep(1)
        try:
            t = browser.find_element_by_xpath(".//div[@class='WB_text W_f14']").text.replace('\n','').replace(' ','').replace('\r','').strip()
        except:
            t = None
            print("no data")
        browser.close()
        return t
    browser.get(url)
    time.sleep(3)
    try:
        t = browser.find_element_by_xpath(".//div[@class='WB_text W_f14']").text.replace('\n','').replace(' ','').replace('\r','').strip()
    except:
        t = None
        print("no data")
    browser.close()
    return t