from selenium import webdriver
from PIL import Image # pillow 安裝 Anaconda 時已自動安裝

options = webdriver.ChromeOptions()
#options.add_argument('window-size=1920x1080') #指定瀏覽器解析度
#options.add_argument('--disable-gpu') #谷歌文件提到需要加上這個屬性來規避bug
#options.add_argument('--hide-scrollbars') #隱藏滾動條, 應對一些特殊頁面
#options.add_argument('blink-settings=imagesEnabled=false') #不載入圖片, 提升速度
options.add_argument('--headless') #瀏覽器不提供視覺化頁面. linux下如果系統不支援視覺化不加這條會啟動失敗

# 取出 綱頁圖中的驗證圖片，存入 <img_source.png> 檔
# 請調整解析度
url="https://irs.thsrc.com.tw/IMINT/?locale=tw"
driver=webdriver.Chrome(chrome_options = options)
driver.get(url)
driver.maximize_window()
driver.save_screenshot("img_screenshot.png")
element=driver.find_element_by_id("BookingS1Form_homeCaptcha_passCode")

location = element.location
print(location)

size = element.size
print(size)

left = element.location['x']
top = element.location['y']
right = left + element.size['width']
bottom = top + element.size['height']
print(left,top,right,bottom)

img=Image.open("img_screenshot.png")
img2=img.crop((left,top,right,bottom))
img2.save('img_source.png')

driver.quit()