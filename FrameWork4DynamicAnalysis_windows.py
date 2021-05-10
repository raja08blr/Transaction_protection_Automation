from selenium import webdriver
import subprocess
import requests
from datetime import datetime
import json

chrome_driver_path = r"C:\Users\rv\Downloads\chromedriver_win32_88\chromedriver.exe"


def read_config_file():
    f = open(r'C:\Users\rv\Downloads\\configData.txt')
    data_dic = json.load(f)
    return data_dic

data = read_config_file()
print(data['ext_id'])
print(data['urls'])


# upload extension and open the diff cat urls

def install_extn_open_cat_urls(input):
    # download_crx(data['ext_id'])
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    extension_path = data['file_path'] + '//' + data['ext_id'] + ".zip"
    if input == 1:
        chrome_options.add_extension(extension_path)
        # driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.google.com/")
        print(len(data['urls']))
        driver.close()
    if input == 0:
        # driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.tutorialspoint.com/pytest/pytest_grouping_the_tests.htm")
        print(len(data['urls']))
        driver.close()

    # Looping the script to open N new tabs

    # for i in range(len(data['urls'])):
    #     driver.execute_script("window.open('','_blank');")
    #     driver.switch_to.window(driver.window_handles[-1])
    #     driver.get(data['urls'][i])
    #     time.sleep(5)
    # driver.close()


# driver code
def run_tcpdump_on_local_machine():
    func_name = "run_tcpdump_on_local_machine - "
    print(func_name + "start")
    interface_name = "ens192"
    filename = data['url'] + data['ext_id']
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    capture_file_name = "C:\\Users\\rv\\Downloads\\" + filename + interface_name + "_" + curr_time + ".pcap"
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

    # And now you can add your website / app testing functionality:


# run_tcpdump_on_local_machine()
def test():
    install_extn_open_cat_urls(0)
    install_extn_open_cat_urls(1)


test()
