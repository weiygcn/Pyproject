import requests


def login():
    login_url = 'http://doc.zsmy.cn/dologin.action'
    login_body = {
        'os_username': 'yangguangwei', 'os_password': 'yangguangwei@1234', 'login': 'Log in', 'os_destination': ''
    }
    login = requests.post(login_url, data=login_body, verify=False)
    print('=====content=======', login.text)
    print('=====status_code=======', login.status_code)
    print('=====cookies=======', login.cookies)


def logout():
    logout_url = 'http://doc.zsmy.cn/logout.action'
    logout = requests.get(logout_url)
    print('=====logout content=======', logout.text)
    print('=====logout status_code=======', logout.status_code)
    print('=====logout cookies=======', logout.cookies)


login()
logout()
