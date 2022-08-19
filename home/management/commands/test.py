import time, os, random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from coinmarket.settings import BASE_DIR, LOGGER
from home.models import user


class Command(BaseCommand):
    help = 'Create random users'
    
    def __init__(self) -> None:
        self.driver = get_driver('113')
        self.logger = LOGGER

    def handle(self, *args, **kwargs):
        print('Strated 1')
        LOGGER.info('Hello this is loggeer')


        self.driver.get('https://yopmail.com/en/email-generator')
        time.sleep(10)
        genrated_email = self.find_element('email','egen',By.ID).get_attribute('text')
        genrated_email = self.getvalue_byscript('document.querySelector("#egen").innerText')
        print(genrated_email,'------------------')

        # input('Enter :')
        time.sleep(4)
        self.new_tab('https://coinmarketcap.com/')
        self.switch_tab('-1')
        self.driver.refresh()
        user.objects.create(
            username = '''sadegadega''',
            email = f"{genrated_email}"
        )


        #starting to create an account
        self.driver.refresh()
        # to close pop up for search suggestion if it is exists
        time.sleep(5)
        try:self.driver.execute_script("document.getElementsByClassName('HBft')[1].click()")
        except Exception as e: ...
        time.sleep(3)
        self.click_element('signup btn','//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/button[2]',By.XPATH)
        windowss = self.driver.window_handles
        time.sleep(5)
        print(windowss,'----------------------------')
        print(len(windowss),'----------------------------')

        # self.driver.refresh()
        inputs = self.driver.find_elements(By.CLASS_NAME,'dqGVRN')
        print(inputs,'----------------------')
        for  inp in inputs:
            if inp.get_attribute('type') == 'email' :
                inp.send_keys(genrated_email)
            if inp.get_attribute('type') == 'password' :
                inp.send_keys(str(genrated_email).capitalize())
                
        random_sleep()
        self.click_element('create an account btn','dKttWP',By.CLASS_NAME) # click create an account btn

        # captcha is going to solve here

        input('Enter :')
        # --------------------------------------------
        self.driver.refresh()
        self.click_element('signup btn','//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/button[2]',By.XPATH)
        windowss = self.driver.window_handles
        time.sleep(5)
        print(windowss,'----------------------------')
        print(len(windowss),'----------------------------')

        # self.driver.refresh()
        inputs = self.driver.find_elements(By.CLASS_NAME,'dqGVRN')
        print(inputs,'----------------------')
        for  inp in inputs:
            if inp.get_attribute('type') == 'email' :
                inp.send_keys(genrated_email)
            if inp.get_attribute('type') == 'password' :
                inp.send_keys(str(genrated_email).capitalize())
                
        random_sleep()
        self.click_element('create an account btn','dKttWP',By.CLASS_NAME) # click create an account btn

        # captcha is going to solve here

        input('Enter :')
        # --------------------------------------------

        




        self.switch_tab(0)
        self.driver.refresh()
        self.driver.get('https://yopmail.com/en/')

        self.input_text(genrated_email,'get email inbox input','ycptinput',By.CLASS_NAME)
        self.click_element('go to email inboc btn','refreshbut',By.ID)
        self.click_element('go to email inboc btn2','//*[@id="refreshbut"]/button',By.XPATH)


        # sqwitch to email box I-framework
        for i in range(5):
            inbox_ifram = self.find_element('if inbox iframe','ifinbox',By.ID)
            if inbox_ifram :
                self.driver.switch_to.frame(inbox_ifram)
                break

        # find coin market email from inbox
        all_emails_div = self.driver.find_elements(By.CLASS_NAME,'m')
        for emails_div in all_emails_div :
            email_sender = emails_div.find_element(By.CLASS_NAME,'lmf')
            if 'coinmarketcap'in str(email_sender).lower() :
                emails_div.find_element(By.CLASS_NAME,'lm').click()

        # switch to email content i-framwork
        random_sleep(4,8)
        for i in range(5):
            inbox_ifram = self.find_element('if email content iframe','ifmail',By.ID)
            if inbox_ifram :
                self.driver.switch_to.frame(inbox_ifram)
                break

        # open up email and get verification code
        verification_code = self.find_element("genrated email's verification code",'//*[@id="mail"]/div/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[10]/td/h1',By.XPATH)
        try:
            verification_code = int(verification_code)
        except Exception as e: print(e)



        # switch to coin market tab and open verification code inputs
        self.switch_tab(1)
        self.click_element('open verification inputs','ijUBDg ',By.CLASS_NAME)


        # enter verification code
        all_verification_inputs = self.driver.find_elements(By.CLASS_NAME,'bCRBAJ')[0]
        if len(verification_code) == len(all_verification_inputs):
            for (inputs,code) in zip(all_verification_inputs,verification_code) :
                inputs.send_keys(code)
                time.sleep(0.3)
        
        random_sleep(5,8)
        self.driver.refresh()



        

            
        

        




        # allemails_sendername = self.driver.find_elements(By.CLASS_NAME,'lmfd')
        # for sendername in allemails_sendername :
        #     if 'coinmarketcap'in str(sendername).lower() :







        input('Enter :')
        self.driver.quit()

    

    def switch_tab(self,index=0,**link):
        self.driver.switch_to.window(self.driver.window_handles[int(index)]) 
        if link:
            self.driver.get(f'{link}')

    def new_tab(self,link='www.google.com'):
        self.driver.execute_script(f"window.open('{link}')")
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        
    def getvalue_byscript(self,script = ''):
        # made for return value from ele or return ele
        value = self.driver.execute_script(f'return {script}')
        return value

    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        time.sleep(3)
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                ele = wait_obj.until(
                        condition_func((locator_type, locator),
                            *condition_other_args))
            else:
                print(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type, 
                        value=locator)
            if page:
                print(
                        f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                print(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')
            
            return False

    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10,page=None):
        time.sleep(3)
        
        """Find an element, then click and return it, or return None"""
        try:
            ele = self.find_element(element, locator, locator_type, timeout=timeout,page=page)
            if ele:
                ele.click()
                print(f'Clicked the element: {element}')
                return ele

            else:return False
        except Exception as e:print(e)

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, page=None):
        time.sleep(3)
        
        """Find an element, then input text and return it, or return None"""
        try:
            
            ele = self.find_element(element, locator, locator_type=locator_type,
                    timeout=timeout,page=page)
            if ele:
                ele.clear()
                ele.send_keys(text)
                print(f'Inputed "{text}" for the element: {element}')
                return ele
        except Exception as e :
            print(f'Got an error in input text :{element} {e}')
            
            return False

    def connect_vpn(self):
        driver = self.driver

        driver.switch_to.window(driver.window_handles[0])
        driver.get('chrome-extension://ffbkglfijbcbgblgflchnbphjdllaogb/index.html')
        time.sleep(10)
        # driver.refresh()
        # input('Enter :')
        # Disconnect if already connected
        # try:
        #     driver.execute_script('document.querySelector("body > app-root > main > app-home > div > div.spinner > app-switch > div > div.spinner > div.spinner-inner").click()')
        # except Exception as e:print(e)
        time.sleep(3)
        try:
            connected_btn = driver.find_element(By.CLASS_NAME, 'connected')
            connected_btn.click() if connected_btn else None
        except Exception as e:...# document.querySelector("body > app-root > main > app-home > div > div.spinner > app-switch > div > div.spinner > div.spinner-inner").click()

        # Select country
        countries_drop_down_btn = driver.find_elements(By.TAG_NAME, 'mat-select-trigger')
        countries_drop_down_btn[0].click() if countries_drop_down_btn else None

        # randomly select a country name from a list
        country_list = ['United States','Romania','Netherlands','Germany']
        vpn_country = random.choice(country_list)

        total_option_country = driver.find_elements(By.TAG_NAME, 'mat-option')
        for i in total_option_country:
            i_id = i.get_attribute('id')
            country_text_ele = i.find_element(By.XPATH, f"//*[@id='{i_id}']/span")
            country_text = country_text_ele.text
            
            # checking if the country is whether same or not and click on it
            if vpn_country == country_text:
                country_text_ele.click()
                break

        # Checking is the VPN connected or not
        try:
            time.sleep(1)
            self.driver.find_element(By.CLASS_NAME,'disconnected').click()
        except Exception as e:print(e)

def random_sleep(min_sleep_time=1, max_sleep_time=4):
    sleep_time = random.randint(min_sleep_time, max_sleep_time)
    LOGGER.debug(f'Random sleep: {sleep_time}')
    time.sleep(sleep_time)

def get_driver(profile_dir='profile_dir'):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    options = webdriver.ChromeOptions() 

    # options.add_extension("CyberGhost_VPN.crx")#crx file path
    options.add_argument('--no-sandbox')
    options.add_argument('--autoplay-policy=no-user-gesture-required')
    options.add_argument('--start-maximized')    
    # options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--enable-javascript")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--enable-popup-blocking")
    options.add_argument("--ignore-certificate-errors-spki-list")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_extension(os.path.join(BASE_DIR, "Stay-secure-with-CyberGhost-VPN-Free-Proxy.crx"))
    options.add_argument(f'--user-data-dir={os.path.join(BASE_DIR, "profiles")}')
    options.add_argument(f"--profile-directory={profile_dir}")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

    
    return driver