# The operation may take a long time and the site blocks the selenium
# if a return error try to change the ip address

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import csv

URL="https://www.zillow.com/homes/3652-Ash-St-Lake-Elsinore-CA-92530/17951686_zpid/"

PATH = {'sold':{"current value":'//*[@class="ds-home-details-chip"]/p/span',
              "value":'//*[@id="home-details-home-values"]/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/strong',
              "date":'//*[@id="home-details-home-values"]/div/div/div[2]/div[2]/div[2]/div/div'},
      'other': {"current value": '//*[@class="ds-home-details-chip"]/div/div/div/span/span/span',
               "value": '//*[@id="ds-home-values"]/div/div[1]/div/div[4]/div/div/div/div[2]/span',
               "date": '//*[@id="ds-home-values"]/div/div[1]/div/div[4]/div/div[2]/div/div'}
      }



class Manager():
    def __init__(self, url):
        self.url = url
        self.dict = {}
        self.state = ''

    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
        return webdriver.Chrome(options=options)

    def get_url(self):
        self.driver = self.create_driver()
        self.driver.get(self.url)
        self.driver.maximize_window()


    def static_data(self):
        try:
            return self.driver.find_element_by_xpath(PATH[self.state]["current value"]).text
        except NoSuchElementException:
            return False


    def check(self):
        try:
            return self.driver.find_element_by_xpath('//*[@class="ds-home-details-chip"]/p/span').text
        except NoSuchElementException:
            return False


    def getprice_graph(self):
        try:
            return self.driver.find_element_by_xpath(PATH[self.state]["value"]).text
        except NoSuchElementException:
            print("not find price")
            return False


    def getdate_graph(self):
        try:
            return self.driver.find_element_by_xpath(PATH[self.state]["date"]).text
        except NoSuchElementException:
            print("not find date")
            return False


    def move_on_graph(self,graph):
        element_graph = graph
        if not element_graph:
            return False
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element_graph, 0, 10).perform()

        while True:
            action.move_by_offset(4, 0).perform()
            price = self.getprice_graph()
            date = self.getdate_graph()
            print(price,date)
            if price and date:
                if date not in self.dict:
                   self.dict[date] = price
            else:
                break



    def scraper(self,s):
        value = self.static_data()
        if value:
            if self.state == "sold":
                value = value[5:]
            self.dict["Current Value"] = value
            self.dict["Full Address"] = self.driver.title[:-8]
            print(self.dict)
            graph = s.graph()
            if graph:
                self.move_on_graph(graph)
            else:
                print("not find graph")
        else:   
            print("not find page change ip or UA")
        return False


    def create_csv(self, dict):
        with open('zillow_history.csv', 'w',newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dict.items():
                writer.writerow([key, value])


    def situation(self):
        situa = self.check()
        if situa:
            self.state = 'sold'
            s=Sold(self.driver)
        else:
            self.state = 'other'
            s = Other(self.driver)
        self.scraper(s)
        self.create_csv(self.dict)
        self.driver.quit()





class Other():
    def __init__(self,driver):
        self.dict = {}
        self.driver=driver


    def graph(self):
        try:
            return WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.ID, 'This home_0')))
        except TimeoutException:
            print("Loading took too much time!")
            return False




class Sold():
    def __init__(self,driver):
        self.driver = driver
        self.dict = {}


    def graph(self):
        self.driver.find_element_by_xpath('//*[@id="home-details-home-values"]/div/div[2]/a/div/span').click()
        try:
            return WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.ID, 'This home')))
        except TimeoutException:
            return False




if __name__ == '__main__':
    s=Manager(URL)
    s.get_url()
    s.situation()



