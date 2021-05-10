from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# unpacked_extension_path = r'C:\Users\rv\Downloads\ccecihahjmplendgebiobdabbmnllnan.crx'
unpacked_extension_path = r'C:\Users\rv\Downloads\jifpbeccnghkjeaalbbjmodiffmgedin.crx'
# chrome_driver_path = r"C:\Users\rv\Downloads\chromedriver_win32_80\chromedriver.exe"
chrome_driver_path = r"C:\Users\rv\Downloads\chromedriver_win32_88\chromedriver.exe"
options = Options()
# options.add_argument('--load-extension={}'.format(unpacked_extension_path))
options.add_extension(unpacked_extension_path)
driver = webdriver.Chrome(executable_path=chrome_driver_path,options=options)
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
# driver.get("https://www.tutorialspoint.com/index.htm")

# driver.get("https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
# driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('kabalida16@gmail.com')
# driver.find_element_by_xpath('//*[@id="continue"]').click()
# driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('Test@2021')
# driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
# time.sleep(20)
# driver.get('https://www.amazon.in/LG-Inches-Ready-32LM560BPTC-Display/dp/B07TMFQMJC?ref_=Oct_s9_apbd_omwf_hd_bw_b1W1fuh&pf_rd_r=N6FWW5PWZFRR6WFZEEVQ&pf_rd_p=4478153b-fbcd-51c5-ab3f-c05e9bef31d5&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1389375031')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
# driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()
#
# #Make my trip
#
# driver.get('https://www.makemytrip.com/flights/?cmp=SEM|D|DF|G|Brand|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact'
#            '|Expanded|162031058804&s_kwcid=AL!1631!3!162031058804!e!!g!!makemytrip&ef_id'
#            '=EAIaIQobChMIkLa3hvHa7gIV_p1LBR28IAYoEAAYASAAEgLmgfD_BwE:G:s&gclid'
#            '=EAIaIQobChMIkLa3hvHa7gIV_p1LBR28IAYoEAAYASAAEgLmgfD_BwE')
# # time.sleep(2)
# # driver.find_element_by_xpath('//*[@id="SW"]/div[1]/div[2]/div/div/nav').click() driver.find_element_by_xpath(
# # '//div[contains(@class,"ui-dialog") and @aria-describedby="dialogContent2"]//button[@title="Close"]').click()
# # drop=Select(driver.find_element_by_xpath('//*[@id="SW"]/div[1]/div[1]/ul/li[6]/div'))
# # drop.select_by_index(0)
# driver.find_element_by_xpath('//*[@id="SW"]/div[1]/div[1]/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[1]/div[3]/label/span').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div/div/div/div['
#                              '2]/div/div[1]/span[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div/div/div/div['
#                              '2]/div/div[2]/div[1]/div[3]/div[5]/div[4]/div').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/p/a').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="bookbutton-RKEY:e7aa2954-45d6-4bfc-812f-2cc6b590005a:120_0"]').click()
# driver.find_element_by_xpath('//*[@id="fli_list_item_4_RKEY:e7aa2954-45d6-4bfc-812f-2cc6b590005a:120_0"]/div[3]/div['
#                              '1]/div[2]/div[2]/div[2]/button').click()
# time.sleep(4)
# driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div/div[2]/div['
#                              '2]/div/div/label/div/span[1]/span').click()
# driver.find_element_by_xpath('//*[@id="insurance-section"]/div/div[3]/label[2]/input').click()
# driver.find_element_by_xpath('//*[@id="review-continue"]').click()
#
#
# ######## booking.com
#
# driver.get('https://www.booking.com/')
# driver.find_element_by_xpath('//*[@id="ss"]').send_keys('Goa')
# driver

####### flipkart.com

# driver.get("https://www.flipkart.com/")
# driver.find_element_by_xpath('//div[2]//div/div/div/div[2]/div/form/div[1]/input').send_keys('8310503349')
# # driver.find_element_by_xpath('//*[@id="continue"]').click()
# driver.find_element_by_xpath('//div[2]/div/form/div[2]/input').send_keys('Test@2021')
# driver.find_element_by_xpath('//div[2]/div/form/div[4]/button').click()
# time.sleep(20)
# driver.get('https://www.amazon.in/LG-Inches-Ready-32LM560BPTC-Display/dp/B07TMFQMJC?ref_=Oct_s9_apbd_omwf_hd_bw_b1W1fuh&pf_rd_r=N6FWW5PWZFRR6WFZEEVQ&pf_rd_p=4478153b-fbcd-51c5-ab3f-c05e9bef31d5&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1389375031')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
# driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()


######### Aliexpress.com

# driver.get("https://login.aliexpress.com/?returnUrl=https%3A%2F%2Ftrade.aliexpress.com%2ForderList.htm%3Fspm%3Da2g0o"
#            ".home.1000001.31.650c2145W7LNqg%26tracelog%3Dws_topbar%26tsp%3D1613701899557")
driver.get('https://www.aliexpress.com/')
time.sleep(6)
driver.find_element_by_xpath('//div[4]/div/div/img[2]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/img').click()
options.add_argument("--disable-popup-blocking")
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-user-account"]/span/a/i')
signIn = driver.find_element_by_xpath('//*[@id="nav-user-account"]/div/div/p[3]/a[2]')
action.move_to_element(firstLevelMenu).move_to_element(signIn).click().perform()
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('kabalida16@gmail.com')
# driver.find_element_by_xpath('//*[@id="continue"]').click()
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('Testali2021')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/button').click()
time.sleep(20)


######### Aliexpress.com

# driver.get("https://www.ebay.com/")
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="gh-ug"]/a').click()
# driver.find_element_by_xpath('//*[@id="userid"]').send_keys('kabalida16@gmail.com')
# driver.find_element_by_xpath('//*[@id="signin-continue-btn"]').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Test@2021')
# driver.find_element_by_xpath('//*[@id="sgnBt"]').click()
# time.sleep(20)