# coding=utf-8

'''
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.sogou.com")

driver.find_element_by_id("query").clear()
driver.find_element_by_id("query").send_keys(u"光荣之路自动化测试")
driver.find_element_by_id("stb").click()

time.sleep(2)

driver.quit()
'''
'''
# unittest
import unittest

# 被测试类
class myclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b # 将两个传入参数相加

    @classmethod
    def sub(cls, a, b):
        return a - b # 将两个传入参数相减



class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化类固件"""
        print "---setUpClass"


    @classmethod
    def tearDownClass(cls):
        """重构类固件"""
        print "---tearDownClass"


    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 1
        print "--setUp"


    # 退出清理工作
    def tearDwon(self):
        print "--tearDown"


    # 具体的测试用例要以test开头
    def testsum(self):
        res = 3/0
        # 断言两数之和是否等于4
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        # 断言两数之差是否等于2
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')



if __name__ == '__main__':
    unittest.main()

'''

'''
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)


    def tearDown(self):
        pass

    def test_chioce(self):
        # 从序列seq中随机选取一个元素
        element = random.choice(self.seq)
        # 验证随机元素确实属于列表中
        self.assertTrue(element in self.seq)

    def test_sample(self):

        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_shuffle(self):
            # 随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
            # 验证执行函数时抛出了TypeError
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


# print TestDictValueFormatFunctions
# print TestSequenceFunctions

if __name__ == '__main__':
    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1, testCase2])
    # 设置verbosity = 2 可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity = 2).run(suite)
'''
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r"D:\python\htmlTest\table.html")
table = driver.find_element_by_id("table")
# 通过标签名获取表格中的所有对象
trList = table.find_elements_by_tag_name("tr")
# print trList
assert len(trList) == 5,"表格数不符"
for row in trList:
    tdList = row.find_elements_by_tag_name("td")
    for col in tdList:
        print col.text + "\t",
    print
driver.quit()
'''
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r"D:\python\htmlTest\table2.html")
driver.find_element_by_xpath("//td[contains(text(),'化妆')]/input[1]").click()
'''

'''
from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):
    # 启动浏览器
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_visitSogou(self):
        # 访问所搜索网页
        self.driver.get("http://www.sogou.com")
        # 打印当前网页网址
        print self.driver.current_url

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
'''

from selenium import webdriver
import unittest
import time

class VisitChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    #   网页前进后退
    # def test_visitRecentURL(self):
    #     firstURL = "http://www.sogou.com"
    #     # secondURL = "http://www.baidu.com"
    #     self.driver.maximize_window()
    #     self.driver.get(firstURL)
    #     # self.driver.get(secondURL)
    #     # self.driver.back()
    #     time.sleep(3)
    #     # self.driver.forward()
    #     self.driver.refresh()
    #
    #     time.sleep(3)

    #   设置浏览器窗口位置
    # def test_windows_position(self):
    #     self.driver.get("http://www.sogou.com")
    #     position = self.driver.get_window_position()
    #     print "当前浏览器所在位置横坐标：",position['x']
    #     print "当前浏览器所在位置纵坐标：",position['y']
    #     self.driver.set_window_position(y = 600, x = 1000)
    #     print self.driver.get_window_position()
    #   设置当前窗口大小
    # def test_window_size(self):
    #     self.driver.get("http://www.baidu.com")
    #     sizeDict = self.driver.get_window_size()
    #     print "当前浏览器宽",sizeDict['width']
    #     print "当前浏览器高",sizeDict['height']
    #     self.driver.set_window_size(width = 200, height = 400, windowHandle = 'current')
    #     print self.driver.get_window_size(windowHandle = 'current')
    #     time.sleep(5)

    #   获取页面title
    # def test_title(self):
    #     self.driver.get("http://www.baidu.com")
    #     title = self.driver.title
    #     print "当前页面的title为：",title
    #     # 断言页面的title值是否正确
    #     self.assertEqual(title,u'百度一下，你就知道','页面title错误！')

    #   获取页面源码
    # def test_getPageSource(self):
    #     self.driver.get("http://www.sogou.com")
    #     pageSource = self.driver.page_source
    #     print pageSource
    #     self.assertTrue(u'新闻' in pageSource,"页面源码中未找到'新闻'关键字")

    '''
    #   获取与切换浏览器窗口句柄
    def test_opearteWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        fisrt_handle = self.driver.current_window_handle
        print fisrt_handle
        self.driver.find_element_by_id('kw').send_keys("w3cschool")
        self.driver.find_element_by_id('su').click()

        time.sleep(3)

        self.driver.find_element_by_xpath("//div[@id='1']//a[text() = 'w3']").click()
        time.sleep(3)

        all_handles = self.driver.window_handles
        print "++++", self.driver.window_handles[-1]

        # 循环遍历句柄  跳转页面 方法1
        # for handle in all_handles:
        #     if handle != first_handle:    # 判断是否是首页句柄
        #         self.driver.switch_to.window(handle)
        #         print self.driver.title
        # 跳转页面 方法2
        self.driver.switch_to.window(all_handles[1])
        print self.driver.title

        self.driver.find_element_by_link_text('HTML5').click()
        time.sleep(3)
        self.driver.close()
        time.sleep(2)
        print fisrt_handle
        self.driver.switch_to.window(fisrt_handle)
        print self.driver.title
        time.sleep(2)
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试培训")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
    '''
    #    获取页面元素的基本信息
    # def test_getBasicInfo(self):
    #     self.driver.get("http://www.baidu.com")
    #     newElement = self.driver.find_element_by_xpath("//a[text() = '新闻']")
    #     print u"元素的标签名：", newElement.tag_name
    #     print u"元素的size：",newElement.size
    def test_getWebElementIsDisplay(self):
        self.driver.get("D:/python/htmlTest/showAndHidden.html")
        div2 = self.driver.find_element_by_id("div2")
        print div2.is_displayed()
        self.driver.find_element_by_id("button1").click()
        print div2.is_displayed()
        div4 = self.driver.find_element_by_id("div4")
        print div4.is_displayed()
        self.driver.find_element_by_id("button2").click()
        print div4.is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()