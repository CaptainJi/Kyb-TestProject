import csv
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.desiredCaps import appium_desired
from common.commonFun import Common
from base.baseView import BaseView

driver = appium_desired()
com = Common(driver)
i = True
# com.active_page()

while i:
    i = com.get_miaocoin()
