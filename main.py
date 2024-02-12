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



