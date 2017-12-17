import requests
import unittest

class TestKuaiDi(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
        self.Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        self.session = requests.session()

    def test_kuaidi(self):
        r = self.session.get(self.url, headers=self.Headers, verify=False)
        result = r.json()
        com_name=result['company']
        data = result['data']
        self.assertEqual(com_name,u'韵达快递')
        get_result = data[0]['context']
        self.assertIn(u'已签收',get_result)

if __name__== '__main__':
     unittest.main()