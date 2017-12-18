import requests

LoginURL = 'https://passport.cnblogs.com/user/signin'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive', 'Content-Type': 'text/html; charset=utf-8'}
Data = {
    "input1": "V01AMDKLkWn/CjDo8u2CHTS9P9a0GgHVkZHQ03QulS02A0SjUr0B+YFMG7rpEdbesqcg1hh4VIkr/S4+VRKXPxqIY3LlwlfayEOoVWXCwY+z+H3jIlUOzdnoVE6Hms/ZIyfGY81zhaFenzpPgcxDD28M0ysVp3aMFVmq7ItnQ60=",
    "input2": "X/fpPIBf4fzuTMXju2e9GYOlAhmRYdKrlkT0+6lAMM5VSjjCVvhkB/+LX6gp9IO2NRQGiwz/+8zu4r7du3rNeDrtyYfp+1QlBYKIckxKtItHyrDgJiUDLhqjV3TBjrXD36FgT8mrehTIhw3/MA53mw4Gmhe3IFeME/ieFUxX9I0=",
    "remember": False, "geetest_challenge": "ec1c8fa4ad35fe19d85b09482ab052695x",
    "geetest_validate": "ff16ca18093a2740f87ebad0629f10c2",
    "geetest_seccode": "ff16ca18093a2740f87ebad0629f10c2|jordan"}
# cookies = {'_ga': 'GA1.2.459050785.1511866831',
#            '_gid': 'GA1.2.90769525.1513221241',
#            '__gads': '',
#            'ID': 'cf189aefb7acf2bd:T=1513320903:S=ALNI_MYvsY8jSHA2uXH9ULYHrFPnGFmMQA',
#            '.CNBlogsCookie': '6D7A6D16C6DA61EA864B7EC0304CD92CE1FC15F5129DA2F497F79920849A5765D92FB2DC0DF963D2BB6C03B4716B3DC2F6CCC1996611CC44B4D6A554950F755E4A44AAB84FC4F60AA607EE1EC563F31E5A5E5355',
#            '.Cnblogs.AspNetCore.Cookies': 'CfDJ8N7AeFYNSk1Put6Iydpme2YJVwwflaL7Z8F2BA3N_zNvKX8gcXbs2KqHqO2GvdEYqvmPLwLGUpjbZVC8fHPCM4jDbB2HQy0DjCWTG3K4hVfGTK9ijtqcJPDbzOeEtJmspZ15mzdLERHCBs9JHId2f8A2U9C-inOZ8L0AYog5XKUSTPwrkeEliVN_3DzVBqXoW4YOpz3Tva7Dek4KvoPD-RKulX9J9I1WmurNnMmWYkmx7q33nBjWQYmAFTjLWx3Ia22oKsIq3Z3kbC6zCG9JuBDzoi7I0XrsadXP-jSCqr1D',
#            '_gat': '1'}
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
print('=========', c)
r = session.post(LoginURL, data=Data, headers=Headers)
print(r.json())
# https://passport.cnblogs.com/logout.aspx?ReturnUrl=https://home.cnblogs.com/u/1299582/
