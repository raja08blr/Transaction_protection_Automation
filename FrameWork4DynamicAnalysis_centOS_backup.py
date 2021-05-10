from selenium import webdriver
import subprocess
import time
from datetime import datetime
import json

CRX_URL_PREFIX = r"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=45&acceptformat" \
                 r"=crx2,crx3&x=id%3D"
CRX_URL_SUFFIX = r"%26uc"

def read_config_file():
    f = open('/root/configData.txt')
    data_dic = json.load(f)
    return data_dic


data = read_config_file()
print(data['ext_id'])
print(data['urls'])

crx_extension_path = data['file_path'] + r'/jifpbeccnghkjeaalbbjmodiffmgedin.crx'


def download_crx():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_extension(crx_extension_path)
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chromeOptions)
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

def download_crx_using_requests_lib():
    make_crx_url = lambda extid: CRX_URL_PREFIX + data['ext_id'] + CRX_URL_SUFFIX
    crx_url = make_crx_url(ext_id)
    file_name = ext_id + '.zip'
    print("crx_url:: ", crx_url)
    response = requests.get(crx_url, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(response.content)


# upload extension and open the diff cat urls

def install_extn_open_cat_urls():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    extension_path = data['file_path'] + '//' + data['ext_id'] + ".zip"
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
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


def run_tcpdump_on_local_machine():
    func_name = "run_tcpdump_on_local_machine - "
    print(func_name + "start")
    interface_name = "ens192"
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    capture_file_name = "/root/guyCapture_interface_" + interface_name + "_" + curr_time + ".pcap"
    # num_sec_to_sleep = 5
    print(func_name + "about to create capture with name:" + capture_file_name)
    p = subprocess.Popen(["tcpdump",
                          "-i", interface_name,
                          "-w", capture_file_name],
                         stdout=subprocess.PIPE)
    # time.sleep(num_sec_to_sleep)
    install_extn_open_cat_urls()
    p.terminate()
    print(func_name + "end")

# driver code
download_crx_using_requests_lib()
run_tcpdump_on_local_machine()