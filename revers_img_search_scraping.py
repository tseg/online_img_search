import stanford

import sys
import os
# command line parsing
import argparse
# random selection of user agents
import random
import xml.etree

from xml.etree import ElementTree
import libxml2
from HTMLParser import HTMLParser

import nltk
import re
# check for ssl availability in general
try:
    import ssl
except ImportError:
    print "error: no ssl support"

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

import os.path
import time

class MyHTMLParser(HTMLParser):
    datafields = []

    def handle_data(self, data):
        self.datafields.append(data)

    def get_data(self):
        return ' '.join(self.datafields)

    def clean(self):
        self.datafields = []

class revers_img_search:

    def __init__(self):
        self.xpath = {}
        self.xpath['bestguess'] = "/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col'][1]/div[@id='center_col']/div[@id='res']/div[@id='topstuff']/div[@class='card-section']/div[@class='_hUb']/a[@class='_gUb']"
        self.xpath['wikipage'] = "/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col'][2]/div[@id='rhs']/div[@id='rhs_block']/div[@class='g rhsvw kno-kp mnr-c g-blk']/div[@class='kp-blk _Jw _Rqb _RJe']/div[@class='xpdopen']/div[@class='_OKe']/div[2]/div[@class='kp-header']/div[@class='_axe _T9h']/div[@class='_cFb']/div[@class='_tN _IWg _HWg mod']/div[@class='_fdf']/div[2]/div[@class='kno-ecr-pt kno-fb-ctx']"

        
    def get_simple_xpath(self, doc, xpath ):
        ctxt = doc.xpathNewContext()
        # get xpath result
        xp_results  = ctxt.xpathEval(xpath)
        results = []
        i = 0
        # simply remove all tags
        parser = MyHTMLParser()
        parser.clean()
        for xp in xp_results:
            s = str(xp)
            if len(s)>0:
                parser.feed( s )

        ctxt.xpathFreeContext()
        
        return parser.get_data()

    def search_image_file(self, filepath):
        browser = webdriver.Firefox()
        browser.get('http://www.google.com.au/imghp')

        elem = browser.find_element_by_class_name('gsst_a')
        elem.click()

        browser.execute_script("google.qb.ti(true);return false")
        elem = browser.find_element_by_id("qbfile")
        elem.send_keys(filepath)

        psource = browser.page_source
        
        browser.quit()
        
        return psource

    def image_scraper(self, filePath):
        gis_raw_result = self.search_image_file(filePath)
        string_for_output = gis_raw_result.encode('utf8', 'replace')
        parse_options = libxml2.HTML_PARSE_RECOVER + libxml2.HTML_PARSE_NOERROR + libxml2.HTML_PARSE_NOWARNING
        doc = libxml2.htmlReadDoc(string_for_output, '', None, parse_options)

        scrapeResults = self.get_simple_xpath(doc, self.xpath['bestguess'])
        doc.freeDoc()
        
        return scrapeResults 

if __name__ == '__main__':
    revers_img_search_obj = revers_img_search()
    return_txt = revers_img_search_obj.image_scraper('C:\Users\ADMIN\Pictures\Ben.jpg')
    
    sent_result = stanford.Sanitize_Result()
    person_name = sent_result.sanitize_result(return_txt)
    print person_name
