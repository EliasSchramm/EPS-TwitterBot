from Stalker import TwitterStalker
from selenium import webdriver

PathToDriver = "C:/Users/Elias/Documents/selemium/chromedriver.exe"

driver = webdriver.Chrome(PathToDriver)

Stalker1 = TwitterStalker("elonmusk", driver)
Stalker2 = TwitterStalker("realDonaldTrump", driver)

while True:
    Stalker1.search()
    Stalker2.search()