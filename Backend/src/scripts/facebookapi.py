from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login(driver,link,username,password):
    driver.get(link)
    driver.implicitly_wait(30)
    element=driver.find_element(By.CSS_SELECTOR,"#email")
    element.send_keys(username)
    element=driver.find_element(By.CSS_SELECTOR,"#pass")
    element.send_keys(password)
    element.send_keys(Keys.ENTER)
    return driver

def post_story(driver,story_path_list):
    try:
        element=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]")
        element.click()
    except:
        print("Post Story 0 Failed: Cannot switch to post story page")
    for num in range(len(story_path_list)):
        driver.execute_script("window.scrollTo(0,0)")
        try:
            time.sleep(3)
            element=driver.find_element(By.CSS_SELECTOR,"body._6s5d._71pn.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z div.x9f619.x1n2onr6.x1ja2u2z:nth-child(4) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4:nth-child(1) div.x78zum5.xdt5ytf.x1t2pt76:nth-child(1) div.x78zum5.xdt5ytf.x1iyjqo2.x1t2pt76.xeuugli div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6 div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x1qjc9v5.xozqiw3.x1q0g3np.x1l90r2v.x1ve1bff:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.x1swvt13.x1pi30zi.xqdwrps.x16i7wwg.x1y5dvz6 div.x6s0dn4.x78zum5.xvrxa7q.x9w375v.xxfedj9.x1roke11.x1es02x0 div.x1ifrov1.x1i1uccp.x1stjdt1.x1yaem6q.x4ckvhe.x2k3zez.xjbssrd.x1ltux0g.xit7rg8.xc9uqle.x17quhge div.x78zum5.x1a02dak.x139jcc6.xcud41i.x9otpla.x1ke80iy div.xsgj6o6.xw3qccf.x1xmf6yo.x1w6jkce.xusnbm3:nth-child(1) div.xh8yej3 a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 > div.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1r1pt67")
            element.click()
        except:
            print(f"Post Story {num} Failed: Cannot find add button")
            driver.refresh()
            continue
        try:
            time.sleep(2)
            element=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
            element.send_keys(story_path_list[num])
        except:
            print(f"Post Story {num} Failed: Cannot choose image")
            driver.refresh()
            continue
        try:
            time.sleep(2)
            element=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]")
            element.click()
            print(f"Post Story {num} Success")
            time.sleep(7)
        except:
            print(f"Post Story {num} Failed: Cannot post story")
            driver.refresh()
            continue
    driver.close()