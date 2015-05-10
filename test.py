#coding=utf-8
#!/usr/bin/python

from bs4 import BeautifulSoup
import cookielib,hashlib
import urllib2,urllib,os,time,random
import socket,os

import get_page_content as get_page


# set parameters

Enconding='utf-8'

url_1='http://epub.cnki.net/kns/brief/default_result.aspx'

url_2='http://www.cnki.net/KCMS/detail/detail.aspx?QueryID=1&CurRec=1&recid=&filename=2007097337.nh&dbname=CDFD9908&dbcode=CDFD&pr=&urlid=&yx=&uid=WEEvREcwSlJHSldSdnQ1V1lyYm5jY1ZBbnAyaGd6YTV5amhuTlZhS3duTUtJNFhwZDlBQmNScU1BMW51UjJZMGd3PT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&v=MTY0MTMzcVRyV00xRnJDVVJMK2ZZdVptRmlqZ1VMelBWMTI3R2JPeEdkTFBxSkViUElSOGVYMUx1eFlTN0RoMVQ='

url_3='http://www.cnki.net/KCMS/download.aspx?filename=FR5oEWVxGS2QjcG9SVodUWtxkcx8CRhdmeU10K1s0KzMDeyBjN1NHZ24WToxmcFVlZ4QUV2dHZTdFe=0DOjNWUwZ3ZMh1bGZ0ZzoGN4QVcm9GaU90dWtmWTRkVkFUN380dNJ1QKtWTzBzRnhUSYRkaK5EMSR&dflag=nhdown&tablename=CDFD9908'

# process

page_1=get_page.getPageContent(url_1)
# print page_1
# soup = BeautifulSoup(page_1,fromEncoding=Enconding)
# print(soup.prettify())
# os.system("pause")

page_2=get_page.getPageContent(url_2)
# print page_2
soup = BeautifulSoup(page_2,fromEncoding=Enconding)
print(soup.prettify())

pdf=get_page.getPageContent(url_3)
# print pdf