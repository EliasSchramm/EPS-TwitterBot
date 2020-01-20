from selenium import webdriver
from src.Grinder import TwitterGrinder

PathToDriver = "phantomjs.exe"

driver = webdriver.PhantomJS(PathToDriver)

grinder1 = TwitterGrinder("realDonaldTrump", driver)

while True:
    grinder1.grind()