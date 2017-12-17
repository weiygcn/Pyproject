import requests

'''
首先手动登录获得有效cookie，然后使用代码获得session，通过RequestsCookieJar修改session中的cookie绕过登录，然后直接使用关联的session访问其他依赖登录的功能
'''
GetNewMessageURL = 'https://msg.cnblogs.com/api/user/current'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
Data = {
    "input1": "V01AMDKLkWn/CjDo8u2CHTS9P9a0GgHVkZHQ03QulS02A0SjUr0B+YFMG7rpEdbesqcg1hh4VIkr/S4+VRKXPxqIY3LlwlfayEOoVWXCwY+z+H3jIlUOzdnoVE6Hms/ZIyfGY81zhaFenzpPgcxDD28M0ysVp3aMFVmq7ItnQ60=",
    "input2": "X/fpPIBf4fzuTMXju2e9GYOlAhmRYdKrlkT0+6lAMM5VSjjCVvhkB/+LX6gp9IO2NRQGiwz/+8zu4r7du3rNeDrtyYfp+1QlBYKIckxKtItHyrDgJiUDLhqjV3TBjrXD36FgT8mrehTIhw3/MA53mw4Gmhe3IFeME/ieFUxX9I0=",
    "remember": False, "geetest_challenge": "ec1c8fa4ad35fe19d85b09482ab052695x",
    "geetest_validate": "ff16ca18093a2740f87ebad0629f10c2",
    "geetest_seccode": "ff16ca18093a2740f87ebad0629f10c2|jordan"}
cookies = {
    '.CNBlogsCookie': '890497436B7C6B28CFA9FB3756E9CA394F5F6457674C9672E4AA827BF696D83EE682047D76057DB388E8AA38A37E0746CE5C874067B9E9CE733AB100CFC141E04A39A28CFD6A842D4C9528293FE6DB1B3F9C8FE2',
    '.Cnblogs.AspNetCore.Cookies': 'CfDJ8N7AeFYNSk1Put6Iydpme2aZKugZufmrw5ty_ujkEUiC6FeP4ljJtlu1aUTncb7eQJKq517T7DU08VPjfWai5qyOgqt-q2HiLysYmu_XBfFdcw0-CVB2IS6PlZ1SBO4TkW-mZ3AJ6WYDrulT7NHLwPIvbJequVrxqG-hbSOypXb3qVxxFxSHRLcHaLtFWyBavp_YbOpO0Ru7oKCarZl_l_Pp-KrrhmyqpQb4g_EIK3BZkZme0aDvg4Mt-R34K0SHaZm5VOtQ3EVGd9tveW1BYhVY5srjrzrc8AGgU1djf66K',
    'SERVERID': 'fc59f0882c6e4b75dcaad92e7e90772e|1513331278|1513327308'
}
session = requests.session()
c = requests.cookies.RequestsCookieJar()
for k, v in cookies.items():
    c.set(k, v)
session.cookies.update(c)
print('====修改的后cookie=====', c)
r = session.get(GetNewMessageURL, headers=Headers)
print('请求我的新信息-响应：',r.json())
