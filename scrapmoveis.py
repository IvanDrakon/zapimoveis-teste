import time
from selenium import webdriver
from selenium.webdriver.common.by import By


SCROLL_PAUSE_TIME = 1
VALUE = 0.60


class ScrapMoveis:
    def __init__(self, site):
        self.site = site
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.site)

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            global VALUE
            VALUE += 0.10
            self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {VALUE});")
            if VALUE > 0.85:
                VALUE = 0.60
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_values(self):
        price_text = self.driver.find_elements(By.CSS_SELECTOR,
                                               '.ListingCard_result-card__wrapper__6osq8 .w-full .l-text--weight-bold')
        price_list = []
        for e in price_text:
            price_month = e.text.split(" ", 1)[1]
            price = price_month.split("/", 1)[0]
            try:
                price_formated = int(f"{price.split('.', 1)[0]}{price.split('.', 1)[1]}")
            except IndexError:
                price_formated = int(price)
                print("IndexError")
            price_list.append(price_formated)
        print(price_list)
        local_text = self.driver.find_elements(By.CSS_SELECTOR, '.card__location .l-text--weight-medium')
        local_list = []
        for e in local_text:
            local = e.text.split(",", 1)[0]
            local_list.append(local)
        print(local_list)
        size_text = self.driver.find_elements(By.CSS_SELECTOR, ".Amenities_card-amenities__kpLh7 p[itemprop='floorSize']")
        size_list = []
        for e in size_text:
            size = e.text.split(" ", 1)[0]
            size_list.append(size)
        print(size_list)
        if len(price_list) == len(local_list) == len(size_list):
            return {
                    "prices": price_list,
                    "Locals": local_list,
                    "sizes": size_list
                    }


teste = ScrapMoveis("https://www.zapimoveis.com.br/aluguel/imoveis/pr+curitiba/?__ab=sup-hl-pl:newC,exp-aa-test:control,super-high:new,off-no-hl:new,pos-zap:new,new-rec:b,zapproppos:control,ltroffline:ltr&transacao=aluguel&onde=,Paran%C3%A1,Curitiba,,,,,city,BR%3EParana%3ENULL%3ECuritiba,-25.426899,-49.265198,&pagina=1")
print(teste.get_values())
