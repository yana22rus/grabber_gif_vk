from os import devnull,getenv
from time import sleep
from random import randint
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


options = Options()
#options.headless = True
profile = webdriver.FirefoxProfile(getenv("path"))
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "none"
driver = webdriver.Firefox(options=options,service_log_path=devnull,firefox_profile=profile)

driver.maximize_window()
driver.implicitly_wait(10)


count = 0

while count != 10:


    driver.get(f"{getenv('parsing_wall')}{randint(1, 76975)}")

    sleep(3)

    try:

        post_text = driver.find_element_by_css_selector(".wall_post_text > a:nth-child(1)").text

        driver.find_element_by_css_selector(".page_gif_actions:nth-child(2) .page_gif_add_icon").click()

    except:

        continue

    sleep(1)

    driver.get(getenv("group_to_post"))

    sleep(1)

    driver.find_element_by_css_selector(".new_post_placeholder__text").click()

    driver.find_element_by_css_selector(".textfield").send_keys(post_text)

    driver.find_element_by_css_selector(".cp_icon_btn > .i_icon").click()

    sleep(1)

    driver.find_element_by_link_text('Файл').click()

    driver.find_element_by_css_selector(".simple_fit_item:nth-child(1) .si_owner").click()

    sleep(1)

    driver.find_element_by_css_selector('.Btn_theme_regular:nth-child(1)').click()

    sleep(1)

    count += 1


driver.close()



