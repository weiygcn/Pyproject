import requests
import re

AddDailyLogURL = 'https://i.cnblogs.com/EditDiary.aspx?opt=1'
DelDailyLogURL = 'https://i.cnblogs.com/post/delete'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
AddData = {'__VIEWSTATE': '', '__VIEWSTATEGENERATOR': '4773056F', 'Editor$Edit$txbTitle': '测试334标题',
           'Editor$Edit$EditorBody': '<p>测试334内容</p>', 'Editor$Edit$lkbPost': '保存'
           }
cookies = {
    '.CNBlogsCookie': '5C6A7F982D1F9442B36B009F4039B8C23FABF31EE4B17EE35292A34F7A72F43CD9CFC48C41B6BD28077FC9EE7CF56DA53CBB5FB3B0CC1CD2F4363D5389CD1A231314439022792B9B5D68A02CBC0FEBDB1D48A53D',
    '.Cnblogs.AspNetCore.Cookies': 'CfDJ8N7AeFYNSk1Put6Iydpme2aDcoQ5oCL6gXQuYUEaTJ3EMeaR_6V9Oehb6HmoJxOLEOa0xJ4kDBqi-BC5utceTDcCbBvAvfq7PCm_NSyHCvncXqXaO6K3I59t1KDpzEg_WFGmP8yE5-yKQe8cJVuAVFqaxpM3Vu0Kx4rkoDkuqR80VkwSUhA6S_yOUI_Mi21bf4vbpptEX3xwFawuSn_sOO5qwj6H6SSs1-V0hs-5TVs4wgTRfRKaSuzlXxPc44K1hd0HE8LPMOppOrcpykZ07MqK4DQds_CXc7VsT-SE6R3C',
    'SERVERID': '5600344ccf6bd2d4bb4775a2baf862da|1513418886|1513418567'
}
session = requests.session()
c = requests.cookies.RequestsCookieJar()
for k, v in cookies.items():
    c.set(k, v)
session.cookies.update(c)
AddReq = session.post(AddDailyLogURL, data=AddData, headers=Headers, verify=True, allow_redirects=True)
PostDoneURL = AddReq.url
postID = re.findall(r'postid=(.+?)&', PostDoneURL)
DelData = {"postId": postID[0]}
print(DelData)
DelReq = session.post(DelDailyLogURL, json=DelData, headers=Headers, verify=True, allow_redirects=True)
print(DelReq.status_code)
print(DelReq)
