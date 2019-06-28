import unittest
from process.login import Login
from common.read_excel import ReadExcel
import ddt
import time

readlocal = ReadExcel()
testData = readlocal.read_excel('login')


@ddt.ddt
class homePageCase(unittest.TestCase, Login):
    def setUp(self):
        self.open_browser(0, 'baseurl')

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*testData)
    def test_login(self, testdata):
        self.login(testdata[1], testdata[2])  # 通过打印，可以看到testdata的内容为 testData，这个就是ddt数据驱动
        time.sleep(1.5)
        self.assertEqual(self.assert_text(), testdata[3], '断言失败，提示已更改')

    def test_checkSearch(self):
        self.click_search()
        try:
            flag = self.isElementExist(self.search_assert())
            if flag:
                raise ('搜索框存在')
        except:
            raise ('搜索框不存在')

    def test_scrollBottom(self):
        self.scroll_bottom()
        self.assertEqual(self.assert_bottom(), '订阅', '页面出错或未滑动到底部')


if __name__ == '__main__':
    unittest.main()
