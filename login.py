import env
from robobrowser import RoboBrowser
browser = RoboBrowser()
browser.open(env.Moodle._URLLOGGIN)


def get_html_loged_in(url):
    if verifylogin():
        if verifyInscription(url):
            browser.open(url)
            return browser.select('html')
        else:
            return False
    else:
        browser.open(env.Moodle._URLLOGGIN)
        form = browser.get_form(id='login')
        form['username'].value = env.UserAccount._USERNAME
        form['password'].value = env.UserAccount._PASSWORD
        browser.submit_form(form)

        if verifylogin():
            if verifyInscription(url):
                browser.open(url)
                return browser.select('html')
            else:
                return False

    if not verifylogin():
        print('Connection Failed')
        return False


def verifylogin():

    if "<span class=\"usertext mr-1\">" + env.UserAccount._USERTEXT + "</span>" not in str(browser.select('span.usertext')):
        print('Trying to login with user: ' + env.UserAccount._USERNAME + '......')
        return False
    else:
        return True


def verifyInscription(url):
    browser.open(url)
    if "id=\"mform1\"" in str(browser.select):
        return False
    else:
        return True