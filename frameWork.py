from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import json

chrome_driver_path = r"C:\Users\rv\Downloads\chromedriver_win32_88\chromedriver.exe"


def read_config_file():
    f = open(r'C:\Users\rv\Downloads\configData.txt')
    data_dic = json.load(f)
    return data_dic


data = read_config_file()
print(data['ext_id'])
print(data['urls'])

crx_extension_path = data['file_path'] + r'\jifpbeccnghkjeaalbbjmodiffmgedin.crx'


def download_crx():
    options = Options()
    options.headless = True
    options.add_extension(crx_extension_path)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    # # to maximize the browser window
    driver.maximize_window()
    url = "chrome-extension://jifpbeccnghkjeaalbbjmodiffmgedin/crxviewer.html?crx=https%3A%2F%2Fclients2.google.com" \
          "%2Fservice%2Fupdate2%2Fcrx%3Fresponse%3Dredirect%26os%3Dwin%26arch%3Dx86-64%26os_arch%3Dx86-64%26nacl_arch" \
          "%3Dx86-64%26prod%3Dchromecrx%26prodchannel%3Dunknown%26prodversion%3D80.0.3987.116%26acceptformat%3Dcrx2" \
          "%2Ccrx3%26x%3Did%253D12345678%2526uc&zipname=12345678.zip "

    sourceUrl = url.replace('12345678', data['ext_id'])
    print(sourceUrl)
    driver.get(sourceUrl)
    time.sleep(10)

    if driver.find_element_by_id("download-link").is_displayed():
        driver.find_element_by_id("download-link").click()
        print(driver.find_element_by_id("download-link").get_attribute("href"))
        time.sleep(4)

    driver.close()


# upload extension and open the diff cat urls

def install_extn_open_cat_urls():
    options = Options()
    options.headless = True
    extension_path = data['file_path'] + '\\' + data['ext_id'] + ".zip"
    options.add_extension(extension_path)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    # # to maximize the browser window
    driver.maximize_window()

    driver.get("https://www.google.com/")
    print(len(data['urls']))
    # Looping the script to open N new tabs

    for i in range(len(data['urls'])):
        driver.execute_script("window.open('','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(data['urls'][i])
        time.sleep(5)
    driver.close()


# driver code
# download_crx()
install_extn_open_cat_urls()
