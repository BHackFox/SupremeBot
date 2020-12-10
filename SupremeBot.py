from selenium import webdriver
import urllib.request
import json
import datetime
import time
from selenium.webdriver.support.ui import Select
import sys

def Banner():
    banner = r"""
     ______  __  __  ______  ______  ______  __    __  ______  ______  ______  ______
    /\  ___\/\ \/\ \/\  == \/\  == \/\  ___\/\ "-./  \/\  ___\/\  == \/\  __ \/\__  _\
    \ \___  \ \ \_\ \ \  _-/\ \  __<\ \  __\\ \ \-./\ \ \  __\\ \  __<\ \ \/\ \/_/\ \/
     \/\_____\ \_____\ \_\   \ \_\ \_\ \_____\ \_\ \ \_\ \_____\ \_____\ \_____\ \ \_\
      \/_____/\/_____/\/_/    \/_/ /_/\/_____/\/_/  \/_/\/_____/\/_____/\/_____/  \/_/

"""
    return banner

def Legal():
    legal = r"""
                            SupremeBot by BHackFox
                    https://github.com/BHackFox/SupremeBot
    """
    print(legal)

class Bot_Supreme:
    def __init__(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            self.driver = webdriver.Chrome("./chromedriver")
        elif sys.platform == "win32":
            self.driver = webdriver.Chrome("chromedriver.exe")
        else:
            try:
                self.driver = webdriver.Chrome("./chromedriver")
            except:
                print("Error configuring webdriver")

    def Start(self,link):
        with open('data/data.JSON') as json_file:
            self.jsonconfigfile = json.load(json_file)
        self.link = link
        self.driver.get("https://www.supremenewyork.com"+self.link)
        select = Select(self.driver.find_element_by_id('size'))
        select.select_by_visible_text(self.jsonconfigfile["size"])
        self.driver.find_element_by_name('commit').click()
        #self.driver.get("https://www.supremenewyork.com/checkout")
        time.sleep(0.5)
        self.driver.get("https://www.supremenewyork.com/checkout")
        self.name = self.jsonconfigfile["name"]
        self.email = self.jsonconfigfile["email"]
        self.phone = self.jsonconfigfile["phone"]
        self.addr1 = self.jsonconfigfile["addr1"]
        self.addr2 = self.jsonconfigfile["addr2"]
        self.addr3 = self.jsonconfigfile["addr3"]
        self.zip = self.jsonconfigfile["zip"]
        self.city = self.jsonconfigfile["city"]
        self.country = self.jsonconfigfile["country"]
        self.cardtype = self.jsonconfigfile["cardtype"].lower()
        if self.cardtype == "mastercard":
            self.cardtype = "master"
        elif self.cardtype == "american express":
            self.cardtype = "american_express"
        self.cardnumber = self.jsonconfigfile["cardnumber"]
        self.cardexpmonth = self.jsonconfigfile["cardexpmonth"]
        self.cardexpyear = self.jsonconfigfile["cardexpyear"]
        self.cardcode = self.jsonconfigfile["cardcode"]
        self.driver.find_element_by_id('order_billing_name').send_keys(self.name)
        self.driver.find_element_by_id('order_email').send_keys(self.email)
        self.driver.find_element_by_id('order_tel').send_keys(self.phone)
        self.driver.find_element_by_id('bo').send_keys(self.addr1)
        self.driver.find_element_by_id('oba3').send_keys(self.addr2)
        self.driver.find_element_by_id('order_billing_address_3').send_keys(self.addr3)
        self.driver.find_element_by_id('order_billing_city').send_keys(self.city)
        self.driver.find_element_by_id('order_billing_zip').send_keys(self.zip)
        select = Select(self.driver.find_element_by_id('order_billing_country'))
        select.select_by_value(self.country)
        select = Select(self.driver.find_element_by_id('credit_card_type'))
        select.select_by_value(self.cardtype)
        gett = self.driver.find_element_by_id('cnb')
        for i in self.cardnumber:
            gett.send_keys(i)
            time.sleep(0.2)
        select = Select(self.driver.find_element_by_id('credit_card_month'))
        select.select_by_value(self.cardexpmonth)
        select = Select(self.driver.find_element_by_id('credit_card_year'))
        select.select_by_value(self.cardexpyear)
        self.driver.find_element_by_id('vval').send_keys(self.cardcode)
        time.sleep(4000)


class ChangeInPage:
    def __init__(self,base_url):
        self.base_url = base_url

    def ImportFile(self):
        tmp = urllib.request.urlopen(self.base_url)
        tmp_string = tmp.read().decode()
        j = 0
        tmp_comp = []
        for i in range(len(tmp_string)):
            if tmp_string[i] == ">":
                tmp_comp.append(tmp_string[j:i+1])
                j = i+1
        with open("data/new.txt","w") as wr:
            wr.write("\n".join(tmp_comp))

    def CheckChange(self):
        self.ImportFile()
        self.new = open("data/new.txt")
        self.old = open("data/old.txt")

        self.old = [lines.strip() for lines in self.old]
        self.new = [lines.strip() for lines in self.new]
        self.changes = []
        for i in range(len(self.new)):
            if self.new[i] not in self.old:
                self.changes.append(self.new[i])
        return self.changes


def Scrap():
    search = ChangeInPage("https://www.supremenewyork.com/shop")

    result = search.CheckChange()
    if len(result) > 1:
        ind_i = result[0].index('"') + 1
        ind_f = result[0][ind_i:].index('"') + ind_i
        content = result[0][ind_i:ind_f]

        return content
    else:
        return None

class JsonContent:
    def __init__(self):

        self.CheckContent()

    def CreateContent(self):

        self.jsonconfigfile = {"name":str(input("[*] Name: ")),
                            "email":str(input("[*] Email: ")),
                            "phone":str(input("[*] Phone Number: ")),
                            "size":str(input("[*] Size (Large,Medium,Small): ")),
                            "addr1":str(input("[*] Address 1: ")),
                            "addr2":str(input("[*] Address 2: ")),
                            "addr3":str(input("[*] Address 3: ")),
                            "zip":str(input("[*] Zip Code: ")),
                            "city":str(input("[*] City: ")),
                            "country":str(input("[*] Country (GB,IT..): ")),
                            "cardtype":str(input("[*] Card Type (Visa,Mastercard..): ")),
                            "cardnumber":str(input("[*] Card Number: ")),
                            "cardexpmonth":str(input("[*] Card Exp. Mounth: ")),
                            "cardexpyear":str(input("[*] Card Exp. Year: ")),
                            "cardcode":str(input("[*] Card CVV: "))}

        with open("data/data.JSON","w") as wr:
            json.dump(self.jsonconfigfile,wr)
        self.CheckContent()

    def CheckContent(self):
        with open('data/data.JSON') as json_file:
            self.jsonconfigfile = json.load(json_file)

        for i in self.jsonconfigfile:
            print(self.jsonconfigfile[i])
        rs = str(input("Your data are correct? (Yes/No): ")).lower()
        if rs == "n" or rs == "no":
            self.CreateContent()



def main():
    print(Banner())
    Legal()
    time.sleep(1)
    first = str(input("Do you want to check your data? (Yes/no): ")).lower()
    if first == "y" or first == "yes":
        JsonContent()
    print("Open Webdriver...")
    Bot = Bot_Supreme()
    print("Start Listening for new articles...")
    tmp = urllib.request.urlopen("https://www.supremenewyork.com/shop/")
    tmp_string = tmp.read().decode()
    j = 0
    tmp_comp = []
    for i in range(len(tmp_string)):
        if tmp_string[i] == ">":
            tmp_comp.append(tmp_string[j:i+1])
            j = i+1
    with open("data/old.txt","w") as wr:
        wr.write("\n".join(tmp_comp))
    content = Scrap()
    while content == None:
        time_now = datetime.datetime.now().strftime("%X")
        print("No change at:", time_now)
        content = Scrap()
    print(content)
    Bot.Start(content)

if __name__ == "__main__":
    main()
