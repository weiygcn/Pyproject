import requests
url='http://chandao.zsmy.cn/zentao/bug-view-382.html'
body = {'account':'yangguangwei','password':'ef5f51746de51adf684c77e81cec26a7','referer':'http%3A%2F%2Fchandao.zsmy.cn%2Fzentao%2Fbug-view-382.html'}
r = requests.post(url,body, verify=False)
print(r.content)
print(r.status_code)