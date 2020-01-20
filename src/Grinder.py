import time as t
waitTime = 5;
SCROLL_PAUSE_TIME = 6



class TwitterGrinder():
    def __init__(self, toGrind, driver):
        self.file = toGrind + "_grinded.txt"
        self.iter = 0
        self.found = 0
        list = open(self.file, 'a', encoding="utf-8")
        list.close()
        self.driver = driver
        self.grinding = toGrind
        t.sleep(4)
        self.last_height = 0

        self.prepGrind()

    def prepGrind(self):
        self.driver.get("https://twitter.com/" + self.grinding + "/")
        self.last_height = self.driver.execute_script("return document.body.scrollHeight")

    def grind(self):
        t.sleep(waitTime)
        x = self.driver.find_elements_by_class_name("js-original-tweet")
        temps = self.getList()

        for i in x:
            if i.get_attribute("data-screen-name") == self.grinding:

                id = i.get_attribute("data-item-id")
                text = i.find_element_by_class_name("js-tweet-text").text

                timeContainer = i.find_element_by_class_name("tweet-timestamp")

                timeStamp = timeContainer.get_attribute("title");

                if not (str(id) in temps) and text != "":
                    print(self.grinding + " Registered new Tweet\n")
                    print("ID: " + str(id))
                    print("Time: " + str(timeStamp))
                    print("Text: " + text)

                    print("\n")
                    self.found += 1
                    self.appendToList(id, text, timeStamp)

        self.iter += 1
        print(self.grinding + ": " + str(self.iter) + " Iterations, " + str(self.found) + " Tweets Found!")

        # Scroll down to bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




    def getList(self):
        list = open(self.file, 'r', encoding="utf-8")
        ret = list.read()
        list.close()
        return ret

    def appendToList(self, id, text, time):
        list = open(self.file, 'a', encoding="utf-8")
        list.write("ID:" + str(id) + "\n")
        list.write("TIME:" + str(time) + "\n")
        list.write("TEXT:" + text + "\n\n")
        list.close()