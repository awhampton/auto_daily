from bs4 import BeautifulSoup as bs
import requests
import getpass

# log into github, s is a requests.Session() object
def github_login(s):
    gh_login_page = bs(s.get('https://github.com/login').text, 'html.parser')
    atoken = gh_login_page.find("input", {"name": "authenticity_token"}).attrs['value']
    button = gh_login_page.find("input", {"name": "commit"}).attrs['value']
    uname = input("github username: ")
    pwd = getpass.getpass("github password: ")
    r = s.post('https://github.com/session', data = {'login':uname, 'password':pwd, 'authenticity_token': atoken, 'commit':button})
    if r.status_code == 200:
        print("** GITHUB LOGIN SUCCESS **")
    else:
        print("** GITHUB LOGIN FAILED **")
    return

# log into derp: requires github credentials in the session
def derp_login(s):
    r = s.get('http://petunia.cs.uoregon.edu:8080/derp/')
    return

# submit daily on derp
def derp_daily(s, content):
    r = s.post('http://petunia.cs.uoregon.edu:8080/derp/daily', data = {'daily':content})
    if r.status_code == 200:
        print("** DAILY SUBMIT SUCCESS **")
    else:
        print("** DAILY SUBMIT FAILED **")
    return

if __name__ == '__main__':
    session = requests.Session()
    github_login(session)
    derp_login(session)
    derp_daily(session, "testing auto submit script")

    # close the session when finished
    session.close()
