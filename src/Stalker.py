import time as t


class TwitterStalker():
    def __init__(self, toStalk, driver):
        self.file = toStalk + ".txt"
        self.iter = 0
        self.found = 0
        list = open(self.file, 'a')
        list.close()
        self.driver = driver
        self.stalk = toStalk;
        t.sleep(4)

    def search(self):

        self.driver.get("https://twitter.com/" + self.stalk + "/")
        t.sleep(5)
        x = self.driver.find_elements_by_class_name("js-original-tweet");
        temps = self.getList();

        for i in x:
            if i.get_attribute("data-screen-name") == self.stalk:

                id = i.get_attribute("data-item-id")
                text = i.find_element_by_class_name("js-tweet-text").text

                timeContainer = i.find_element_by_class_name("tweet-timestamp")

                timeStamp = timeContainer.get_attribute("title");

                if not (str(id) in temps) and text != "":
                    print(self.stalk + " Registered new Tweet\n")
                    print("ID: " + str(id))
                    print("Time: " + str(timeStamp))
                    print("Text: " + text)

                    print("\n")
                    self.found += 1;
                    self.appendToList(id, text, timeStamp)

        self.iter += 1;
        print(self.stalk + ": " + str(self.iter) + " Iterations, " + str(self.found) + " Tweets Found!")

    def getList(self):
        list = open(self.file, 'r')
        ret = list.read()
        list.close()
        return ret

    def appendToList(self, id, text, time):
        list = open(self.file, 'a')
        list.write("ID:" + str(id) + "\n")
        list.write("TIME:" + str(time) + "\n")
        list.write("TEXT:" + text + "\n\n")
        list.close()
