import os, time
import getpass
import subprocess
import selenium
import tools.ntuinfo as ntuinfo
import tools.ntudriver as ntudriver
from selenium.webdriver.chrome.service import Service

# check chromedriver path
try:
    # for brew users
    chromedriver_path = subprocess.run(['which','chromedriver'], capture_output=True)
    chromedriver_path = str(chromedriver_path.stdout).strip("b,\',\"").replace("\\n", "")
except:
    # for general users
    chromedriver_path = ""
finally:
    if chromedriver_path == "" or "chromedriver" not in chromedriver_path:
        chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
    print(f"ChromeDriver successfully found : {chromedriver_path}")

info = ntuinfo.get_info()
driver = selenium.webdriver.Chrome(service=Service(chromedriver_path))
driver.get("https://ntupesc.ntu.edu.tw/facilities/PlaceGrd.aspx") # 新體預約首頁

ntudriver.booking(driver, info, alumni=False)
while True:
    quit = input("Enter q to quit : ")
    if quit == 'q':
        driver.quit()
        break