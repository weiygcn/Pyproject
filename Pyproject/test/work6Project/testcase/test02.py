import requests
import re
import unittest
import time


class test01(unittest.TestCase):
    def setUp(self):
        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        self.AddDailyLogURL = 'https://i.cnblogs.com/EditDiary.aspx?opt=1'
        self.AddData = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '4773056F',
            'Editor$Edit$txbTitle': '测试334标题',
            'Editor$Edit$EditorBody': '<p>测试334内容</p>',
            'Editor$Edit$lkbPost': '保存'}
        self.cookies = {
            '.CNBlogsCookie': '5C6A7F982D1F9442B36B009F4039B8C23FABF31EE4B17EE35292A34F7A72F43CD9CFC48C41B6BD28077FC9EE7CF56DA53CBB5FB3B0CC1CD2F4363D5389CD1A231314439022792B9B5D68A02CBC0FEBDB1D48A53D',
            '.Cnblogs.AspNetCore.Cookies': 'CfDJ8N7AeFYNSk1Put6Iydpme2aDcoQ5oCL6gXQuYUEaTJ3EMeaR_6V9Oehb6HmoJxOLEOa0xJ4kDBqi-BC5utceTDcCbBvAvfq7PCm_NSyHCvncXqXaO6K3I59t1KDpzEg_WFGmP8yE5-yKQe8cJVuAVFqaxpM3Vu0Kx4rkoDkuqR80VkwSUhA6S_yOUI_Mi21bf4vbpptEX3xwFawuSn_sOO5qwj6H6SSs1-V0hs-5TVs4wgTRfRKaSuzlXxPc44K1hd0HE8LPMOppOrcpykZ07MqK4DQds_CXc7VsT-SE6R3C',
            'SERVERID': '5600344ccf6bd2d4bb4775a2baf862da|1513418886|1513418567'}
        self.session = requests.session()
        c = requests.cookies.RequestsCookieJar()
        for k, v in self.cookies.items():
            c.set(k, v)
            self.session.cookies.update(c)
        self.AddReq = self.session.post(
            self.AddDailyLogURL,
            data=self.AddData,
            headers=self.Headers,
            verify=True,
            allow_redirects=True)
        print('########### test02')

    def tearDown(self):
        self.DelDailyLogURL = 'https://i.cnblogs.com/post/delete'
        PostDoneURL = self.AddReq.url
        postID = re.findall(r'postid=(.+?)&', PostDoneURL)
        DelData = {"postId": postID[0]}
        print(DelData)
        DelReq = self.session.post(
            self.DelDailyLogURL,
            json=DelData,
            headers=self.Headers,
            verify=True,
            allow_redirects=True)
        print(DelReq.status_code)
        print(DelReq)

    def testTest(self):
        ygwT = time.strftime('%Y_%m_%d_%H_%M_%S')
        print(ygwT)
        print('执行testTest用例')
        self.assertEqual(1, 2, '对比一致')


if __name__ == '__main__':
    unittest.main()
