from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# start web browser
options = Options()
options.add_argument('--headless')
browser = webdriver.Firefox(options = options)
passed = False

# get source code
try:
    browser.get("https://localhost")
    html = browser.page_source

    if "<div class=\"App\">" in str(html): 
        passed = True

except:
    print("Failed")

# close web browser
browser.close()

def test_react():
    assert passed
