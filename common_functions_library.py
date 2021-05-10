from selenium import webdriver
import subprocess
import time,csv
from datetime import datetime
import json
import shutil,os
import requests


def read_config_file(path):
    f = open(path)
    data_dic = json.load(f)
    return data_dic


data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
print(data['ext_id'])


def download_crx(ext_ids):
    for ext_id in ext_ids:
        CRX_URL_PREFIX = r"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=45&acceptformat" \
                         r"=crx2,crx3&x=id%3D"
        CRX_URL_SUFFIX = r"%26uc"

        make_crx_url = lambda extid: CRX_URL_PREFIX + extid + CRX_URL_SUFFIX
        # ext_id = 'jifpbeccnghkjeaalbbjmodiffmgedin'
        crx_url = make_crx_url(ext_id)
        file_name = ext_id + '.crx'
        print(crx_url)
        response = requests.get(crx_url)
        with open(file_name, 'wb') as f:
            f.write(response.content)
        time.sleep(2)
        #shutil.move('/root/dynamic_analysis_framework/'+ext_id+'.crx', data['crx_files_path'])
        time.sleep(3)


# upload extension and open the diff cat urls

def install_extn_open_cat_urls(input):
    download_crx(data['ext_id'])
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    extension_path = data['file_path'] + '//' + data['ext_id'] + ".crx"
    if input == 1:
        chrome_options.add_extension(extension_path)
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.google.com/")
        print(len(data['urls']))
        driver.close()
    if input == 0:
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.tutorialspoint.com/pytest/pytest_grouping_the_tests.htm")
        print(len(data['urls']))


# driver code
def run_tcpdump_on_local_machine(int_d, input_func):
    func_name = "run_tcpdump_on_local_machine - "
    print(func_name + "start")
    interface_name = "ens192"
    data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
    d_name = input_func
    filename = "ecommerce"+"_" + str(data['ext_id'])
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    capture_file_name = "/root/"+filename+ "_" +str(int_d)+"_" +interface_name + "_" + curr_time + ".pcap"
    # num_sec_to_sleep = 5
    print(func_name + "about to create capture with name:" + capture_file_name)
    p = subprocess.Popen(["tcpdump",
                          "-i", interface_name,
                          "-w", capture_file_name],
                         stdout=subprocess.PIPE)
    # time.sleep(num_sec_to_sleep)
    input_func
    #print("fun",fun_n)
    #print("input_func",input_func)
    #fun_n(int_d)
    p.terminate()
    #shutil.move(capture_file_name,'/root/dynamic_analysis_framework/tcp_dump_files')
    data = ['ecommerce', input_func, int_d, '/root/dynamic_analysis_framework/tcp_dump_files', data['ext_id']]
    with open('result.csv', 'a', newline='', encoding="utf-8") as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(data)
    print(func_name + "end")
