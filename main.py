from selenium import webdriver
import subporcess
from config import username, password
from selenium.webdriver.common.by import By


banner = ("""
┃┏━━━┓┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┓┃┃┏┓┏┓┃
┃┃┏━━┛┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┗┓┏┛┃┛┃┃
┃┃┗━━┓━━┓┃━━┓━━┓━┓┃┃┃┓┃┃┏┛┓┃┃
┃┃┏━━┛┃┓┃┃┏━┛┏┓┃┏┛┃┃┃┃┗┛┃┃┃┃┃
┏┛┗┓┃┃┗┛┗┓┗━┓┃━┫┃┃┃┃┃┗┓┏┛┃┛┗┓
┗━━┛┃┃━━━┛━━┛━━┛┛┃┃┃┃┃┗┛┃┃━━┛
┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃
┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃

coded by hphong 
version : 0.1

""')

driver = webdriver.Google()
driver.get("https://www.facebook.com/")

usr = driver.find_element(By.NAME, "email")
usr.send_keys(f{username})

pwd = driver.find_element(By.NAME, "pass")
pwd.send_keys(f'{password})

login = driver.find_element(By.NAME, "login")
login.click()
driver.wait(5)

if driver.title == "Facebook" :
   print("INFO : DANG NHAP THANH CONG VOI TK  {username}")
else :
   print("INFO : KHONG DANG NHAP DUOC TK {username}")


gr_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[4]/span/div/a/span/svg/path[2]")
gr_button.click()





driver.quit()




