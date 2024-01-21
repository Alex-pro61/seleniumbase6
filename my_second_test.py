from seleniumbase import BaseCase

class MySecondTestClass(BaseCase):
    def test_open_website(self):
        self.open("https://peugeot-pechersk.ilta.ua/used-cars")
