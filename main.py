from selenium import webdriver
import subporcess
from config import username, password

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

if login.response_statuscode == 200 :
   print("DANG NHAP THANH CONG VAO FACEBOOK")
else :
   print("KHONG DANG NHAO DUOC VAO FACEBOOK, CHECK TKMK")





