# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

# 登陆
driver = webdriver.Chrome()
driver.get("http://scxiaoshou.i56yun.com")
driver.maximize_window()

driver.find_element_by_xpath("//a[@class='login ztag']").click()
time.sleep(1)
driver.find_element_by_id("pasloginCheck").click()
driver.find_element_by_id("txtLoginName").send_keys("****")
driver.find_element_by_id("txtPassword").send_keys('****')
# 验证码还没有处理，暂时通过等待时间手动输入
time.sleep(4)
driver.find_element_by_id("btnLogin").click()

time.sleep(8)
# 先定位父节点-采购
driver.find_element_by_xpath("//div[@data-code='Menu.Purchase1']").click()
# 层级定位子节点-采购单
driver.find_element_by_xpath("//div[@data-code='Menu.Purchase1']").find_element_by_xpath("//a[@data-code='Menu.Purchase.PurchaseBill']").click()

time.sleep(4)
# 弹出frame页面要先跳转至新页面才能继续定位
driver.switch_to_frame("scxiaoshouGmhlMenu.Purchase.PurchaseBill")
#        sreach_window = driver.current_window_handle 新页面跳转之后用这个操作
title = driver.title
print title
driver.find_element_by_xpath("//a[@title='库存采购']").click()
time.sleep(2)

# 页面没有id属性，需要先用xpath定位
#        supplier = driver.find_element_by_css_selector("span.l-btn-icon.icon-inpurchase-large")
supplier = driver.find_element_by_xpath("//iframe[contains(@src,'http://scxiaoshougmhl.gmhl.i56yun.com/Purchase/PurchaseBillAdd')]")
driver.switch_to.frame(supplier)
time.sleep(3)
#        driver.find_element_by_id("//div[@id='form']/div/div[5]/span[2]/span/a[2]").click()
driver.find_element_by_id("_easyui_textbox_input8").clear()
# 手动输入
driver.find_element_by_id("_easyui_textbox_input8").send_keys(u"dell.供应商")
#        driver.find_element_by_id("_easyui_textbox_input8").send_keys(Keys.TAB)
driver.find_element_by_id("_easyui_textbox_input9").clear()
driver.find_element_by_id("_easyui_textbox_input9").send_keys(u"dell.工程")
driver.find_element_by_id("_easyui_textbox_input10").clear()
driver.find_element_by_id("_easyui_textbox_input10").send_keys(u"dell.往来公司[1]")
time.sleep(1)
driver.find_element_by_id("form").click()    # 收动输入会保留下拉框，在空白处点击一下消除下拉框
dr = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[2]/div").click()
# 层级定位
time.sleep(2)
driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[2]/div").find_element_by_xpath("//html/body/div[16]/div[1]/div[2]").click()
# ActionChains(driver).move_to_element(doubleLocate).perform()
#        dr = driver.find_element_by_xpath("//td[contains(@class,'datagrid-cell,datagrid-cell-c1-SpecificationsId')]").click()
#        dr.find_element_by_xpath("//span[@text='螺纹钢']/div[2]").click()
time.sleep(5)
driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[3]/div").find_element_by_xpath("//html/body/div[16]/div[1]/div[3]").click()
# ActionChains(driver).move_to_element(material).perform()

# /html/body/div[17]  /html/body/div[17]   doubleLocate =  /html/body/div[17]/div[1]


