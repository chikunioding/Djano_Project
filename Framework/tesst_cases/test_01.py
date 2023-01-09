
import time

from Framework.POM.login import Login

class Test001:
    url="https://www.makemytrip.com/"
    number="9028782326"
    Shahar="Nagpur"
    Nagar="Bengaluru"
    Date1="29"
    Date2="9000"

def test_login(self,setup):
    self.driver=setup
    self.lp=Login(self.driver)
    self.driver.get(self.url)
    self.lp.login()
    self.lp.mobile(self.number)
    time.sleep(12)
    self.lp.submit_tab()
    self.lp.city(self.Shahar,self.Nagar)
    self.lp.date1(self.Date1)
    self.lp.date2(self.Date2)
    self.lp.Done()

