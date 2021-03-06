import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def booking(driver, info, alumni=False):
    print("Start booking with ChromeDriver ... ")
    account  = info['account']
    password = info['password']
    floor    = int(info['floor'])
    day      = int(info['day'])
    start_t  = int(info['start_t'])
    end_t    = int(info['end_t'])
    court    = int(info['court'])

    driver.get("https://ntupesc.ntu.edu.tw/facilities/PlaceGrd.aspx") # 新體預約首頁

    # log in
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
    driver.find_element_by_xpath("//*[@id=\"left\"]/ul[1]/li[4]/p/a[1]").click() # 按會員登入
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
    if not alumni:
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_tpValidator_HypLinkStu\"]/p").click() # 按學生登入
        driver.find_element_by_xpath("//*[@id=\"myTable\"]/td/input").send_keys(account)   # 輸入帳號
        driver.find_element_by_xpath("//*[@id=\"myTable2\"]/td/input").send_keys(password) # 輸入密碼
        driver.find_element_by_xpath("//*[@id=\"content\"]/form/table/tbody/tr[3]/td[2]/input").click() # 按登入
    else:
        driver.find_element_by_xpath("//*[@id=\"__tab_ctl00_ContentPlaceHolder1_tcTab_TabPanel3\"]/font").click() # 按校友
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_TabPanel3_txtMemberID\"]").send_keys(account)   # 輸入帳號
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_TabPanel3_txtPassword\"]").send_keys(password) # 輸入密碼
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_TabPanel3_btnLogin\"]").click() # 按登入
        driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
        driver.get("https://ntupesc.ntu.edu.tw/facilities/PlaceGrd.aspx") # 新體預約首頁
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉

    # choose floor
    select = Select(driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_tpValidator_DropLstPlace\"]")) # 選擇樓層
    if floor == 3:
        select.select_by_index(0)
    elif floor == 1:
        select.select_by_index(1)
    if not alumni:
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_tpValidator_Button1\"]").click() # 按搜尋
    else:
        driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_tcTab_tpValidator_ImageButton1\"]").click() # 按搜尋
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
    driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_lblNextWeek\"]/a").click() # 按下週行程
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉

    # refresh until able to book
    day_dict = {1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"日"}
    for i in range(7):
        check_day = driver.find_element(by=By.XPATH, value=f"//*[@id=\"ctl00_ContentPlaceHolder1_tab1\"]/tbody/tr[1]/td[{i+2}]").text
        if day_dict[day] in check_day:
            row, col = str(start_t-6), str(i+2)
    target_xpath = f"/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[{row}]/td[{col}]/img"
    print("Now Ready For Selecting", \
        driver.find_element(by=By.XPATH, value=f"//*[@id=\"ctl00_ContentPlaceHolder1_tab1\"]/tbody/tr[1]/td[{col}]").text, \
        driver.find_element(by=By.XPATH, value=f"//*[@id=\"ctl00_ContentPlaceHolder1_tab1\"]/tbody/tr[{row}]/td[1]").text)
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
            driver.find_element_by_xpath(target_xpath).click()
        except:
            driver.refresh()
            continue
        else:
            break

    # fill in the booking information
    select = Select(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[13]/td[2]/select[1]")) # 開始時間
    if day == 6 or day == 7:
        select.select_by_index(start_t-9)
    else:
        select.select_by_index(start_t-8)
    select = Select(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[13]/td[2]/select[2]")) # 結束時間
    if day == 6 or day == 7:
        select.select_by_index(end_t-10)
    else:
        select.select_by_index(end_t-9)
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[14]/td[2]/input").clear() # 清除預設
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[14]/td[2]/input").send_keys(court) # 場地數量
    driver.find_element_by_xpath("/html/body/div/div[1]/button/span[1]").click() # 按公告叉叉
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[16]/td[2]/input").send_keys() # 將輸入符移至驗證碼欄位