from selenium import webdriver
import time
from common_functions_library import *
import subprocess
from datetime import datetime


def amazon_fun(input_data):
    if input_data == 1:
        func_name = "run_tcpdump_on_local_machine - "
        print(func_name + "start")
        interface_name = "ens192"
        curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
        capture_file_name = "/root/dynamic_analysis_framework/tcp_dump_files/ecommerce_amazon_with_extension" + interface_name + str(data['ext_id'][0])+"_" + curr_time + ".pcap"
        num_sec_to_sleep = 5
        print(func_name + "about to create capture with name:" + capture_file_name)
        p = subprocess.Popen(["tcpdump",
                              "-i", interface_name,
                              "-w", capture_file_name],
                             stdout=subprocess.PIPE)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')

        extension_path = data['crx_files_path'] + '/' + str(data['ext_id'][0]) + ".crx"
        print("extension_path:: ", extension_path)
        # if input_num == 1:
        chrome_options.add_extension(extension_path)
        time.sleep(3)
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http"
                   "%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs"
                   ".openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F"
                   "%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape"
                   "%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore"
                   "%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_"
                   "%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
        driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('kabalida16@gmail.com')
        driver.find_element_by_xpath('//*[@id="continue"]').click()
        driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('Test@2021')
        driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
        time.sleep(20)
        driver.get('https://www.amazon.in/LG-Inches-Ready-32LM560BPTC-Display/dp/B07TMFQMJC?ref_'
                   '=Oct_s9_apbd_omwf_hd_bw_b1W1fuh&pf_rd_r=N6FWW5PWZFRR6WFZEEVQ&pf_rd_p=4478153b-fbcd-51c5-ab3f'
                   '-c05e9bef31d5&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1389375031')
        driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
        driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()
        p.terminate()
        print(func_name + "end")
        driver.close()

    if input_data == 0:
        func_name = "run_tcpdump_on_local_machine - "
        print(func_name + "start")
        interface_name = "ens192"
        curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        data = read_config_file('/root/dynamic_analysis_framework/config_ext_ids.txt')
        capture_file_name = "/root/dynamic_analysis_framework/tcp_dump_files/ecommerce_amazon_without_extension" + interface_name + str(
            data['ext_id'][0]) + "_" + curr_time + ".pcap"

        print(func_name + "about to create capture with name:" + capture_file_name)
        p = subprocess.Popen(["tcpdump",
                              "-i", interface_name,
                              "-w", capture_file_name],
                             stdout=subprocess.PIPE)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        extension_path = data['crx_files_path'] + '/' + str(data['ext_id'][0]) + ".crx"
        print("extension_path:: ", extension_path)
        # chrome_options.add_extension(extension_path)
        # time.sleep(3)
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        # # to maximize the browser window
        driver.maximize_window()

        driver.get("https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http"
                   "%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs"
                   ".openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F"
                   "%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape"
                   "%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore"
                   "%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_"
                   "%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
        driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('kabalida16@gmail.com')
        driver.find_element_by_xpath('//*[@id="continue"]').click()
        driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('Test@2021')
        driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
        time.sleep(20)
        driver.get('https://www.amazon.in/LG-Inches-Ready-32LM560BPTC-Display/dp/B07TMFQMJC?ref_'
                   '=Oct_s9_apbd_omwf_hd_bw_b1W1fuh&pf_rd_r=N6FWW5PWZFRR6WFZEEVQ&pf_rd_p=4478153b-fbcd-51c5-ab3f'
                   '-c05e9bef31d5&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1389375031')
        driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
        driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()
        p.terminate()
        print(func_name + "end")
        driver.close()


amazon_fun(1)
amazon_fun(0)
