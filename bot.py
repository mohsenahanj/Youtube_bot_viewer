from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Yt:
    EXECUTABLE = 'C:/Users/ahanj/Downloads/chromedriver_win32/chromedriver.exe'
    service = Service(executable_path=EXECUTABLE)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors=yes')
    driver = webdriver.Chrome(service=service, options=options)

    def __init__(self, link, views=50):
        self.link = link
        self.views = views

    def RunBot(self):
        self.driver.get(self.link)
        handles = self.driver.window_handles
        actions = ActionChains(self.driver)
        self.driver.execute_script(f'''window.open("{self.link}","secondtab");''')
        second_tab = self.driver.window_handles[-1]
        for i in range(self.views):
            try:
                if i % 8 == 0:
                    self.driver.switch_to.window(second_tab)
                actions.send_keys(Keys.SPACE).perform()  # Start the video
                time.sleep(15)  # Wait for 15 seconds
                actions.send_keys(Keys.SPACE).perform()  # Pause the video
                self.driver.refresh()
                for handle in handles:
                    self.driver.switch_to.window(handle)
            except Exception as e:
                print(f"An error occurred: {e}")
        self.driver.quit()

V_LINK = 'https://www.youtube.com/watch?v=PSsN6Y4Nqi8'
if __name__ == '__main__':
    abc = Yt(V_LINK)
    abc.RunBot()
