import requests

url = 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'

CNBlogsCookie = 'F9F232BBB94897FB16B24929DD56380808122996A5223D287F66F95C20FEC92B92BEA737305E55854021B4953F2DF1A49D62E6430A5A31B10E930FAF35D8A9B82A4A5A30AE26566EE22D7C2B23D2115CAAF087BF'
Cnblogs_AspNetCore_Cookies = 'CfDJ8N7AeFYNSk1Put6Iydpme2Yh0INgKDhlVfumZIM7MJkEr2w20DlPc3L1vKFF5L9JzMVMgk_4v0rwQF40Lhe--ovCUBR48uWq3ra6Wt6X7e_d_eWIt_9plthjx3h9SdACx_8LhnLY0cRYSCCv4TR12_5F2cCUBAPU-z2oaz6mmMwDixBkgFo8te392Mu9ySlJM7PAn1yea-G6prrgvmFSW--F5iRT5S8xZx4I414bVmRdlsnhae9f7zZf2WbbHRMFhRKjVvHgPTsbCP7vJtuy43gC10sy93ZV9hXpoFBL6Wzw'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive', 'Content-Type': 'text/html; charset=utf-8'}
par = {'_': '1513308841375'}
r = requests.get(url, headers=headers, verify=True)
print(r.cookies, '\n=========================')
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie',
      CNBlogsCookie,
      path='/', domain='.cnblogs.com')
c.set('.Cnblogs.AspNetCore.Cookies',
      Cnblogs_AspNetCore_Cookies,
      path='/', domain='.cnblogs.com')
r.cookies.update(c)
print(r.cookies)