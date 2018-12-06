import json
from selenium import webdriver
import requests
import base64
import re
from time import sleep
from PIL import Image

def zhihu_cookies():
  browser = webdriver.Chrome()

  url= 'https://www.zhihu.com/'

  s = requests.Session()

  s.headers.clear()#清除requests头部中的Python机器人信息，否则登录失败

  browser.get(url)

  browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()#避免屏幕失去焦点

  browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('13560414027')

  browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('a3ddf35')
  try:

    img = ''#验证码图片链接--倒立文字

    sleep(5)

  except:

      img=browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/span/div/img').get_attribute("src")
      image_codea = re.findall('base64,(.*)', img, re.S)[0]
      print(image_codea)
      if image_codea!='null':
        #验证码图片链接--字母数字
        sleep(5)
        image_code=re.findall('base64,(.*)',img,re.S)[0]
        with open('copath.jpg','wb') as fb:
          fb.write(base64.b64decode(image_code))
          fb.close()
          im=Image.open('copath.jpg','r')
          im.show()
          im.close()
          sleep(5)
          yzm=input('输入验证码\n>')
          browser.find_element_by_css_selector('.SignFlowInput .Input-wrapper input').send_keys(yzm)
  else:
     pass
  # sleep(10)
  browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/button").submit()#登录
  sleep(5)#等待Cookies加载
  #
  # cookies = browser.get_cookies()
  # with open("zhihucookiesxtg.json","w") as fp:
  #   json.dump(cookies,fp)
  browser.quit()
  # return cookies

zhihu_cookies()