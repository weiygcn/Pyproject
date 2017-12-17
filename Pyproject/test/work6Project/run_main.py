import unittest
import HtmlTestRunner
import os
import time
def all_case(case='testcase'):
    case_dir = os.getcwd()+'\\'+case
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
        print(testcase)
        return testcase

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    report_path=os.getcwd()+'\\report\\'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.html'
    fp=open(report_path,'wb')
    runner=HtmlTestRunner.HTMLTestRunner(stream=fp,report_title=u'这是接口自动化测试报告',descriptions=u'用例执行情况',output=None)
    # runner.run(all_case())
    print(all_case())
    fp.close()
