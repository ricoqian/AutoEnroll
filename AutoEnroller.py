from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
F = 1
S = -1
wd = WebDriver()
courses = ["apm236", "MUS206H1"] # Course code (e.g. ["apm236", "MUS206H1"])
term = S # F: 1, S: -1
utorid = "<UTORID>" # Your Portal UTORid
password = "<PASSWORD>" # Your Portal Password
program_year = "ASPRGHBSC 2015-2016 Fall/Winter" ## Program year (e.g. "ASPRGHBSC 2015-2016 Fall/Winter")
for course in courses:
    while True:
        try:
            wait = randint(10,20)
            wd.implicitly_wait(wait)
            wd.get("https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/")
            if wd.find_elements_by_id("inputID"):
                wd.find_element_by_id("inputID").click()
                wd.find_element_by_id("inputID").clear()
                wd.find_element_by_id("inputID").send_keys(utorid) 
                wd.find_element_by_id("inputPassword").click()
                wd.find_element_by_id("inputPassword").clear()
                wd.find_element_by_id("inputPassword").send_keys(password)
                wd.find_element_by_name("login").click()
            wd.find_element_by_link_text("Manage Courses").click()
            wd.find_element_by_link_text(program_year).click() 
            wd.find_element_by_id("searchBox").click()
            wd.find_element_by_id("searchBox").clear()
            wd.find_element_by_id("searchBox").send_keys(course)
            wd.find_element_by_id("searchBox").click()
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, "course_search_results_list")))
            wd.find_elements_by_xpath("//ul[@id='course_search_results_list']//li//a")[term].click()
            if wd.find_elements_by_link_text("Enrol"):
                wd.find_element_by_link_text("Enrol").click()
                break
        except Exception:
            continue

    print("%s was successfully enrolled. Congrats!\n" % course)
wd.quit()


