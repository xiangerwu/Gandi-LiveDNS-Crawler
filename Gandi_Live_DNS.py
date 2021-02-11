#!/usr/bin/env python
import urllib3
import requests
import logging
# LOG 紀錄
FORMAT = '[%(asctime)s] %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT,filename='Live_DNS.log', filemode='a')
urllib3.disable_warnings()
# 取得外部 IP
IP = requests.get("https://api.ipify.org").text
# 讀檔，domain&token 要保密
text = open('api.txt','r')
domain = text.readline()
token=text.readline()
# Gandi LiveDNS API
# https://api.gandi.net/v5/livedns/domains/你的域名/records/DNS 名稱'
url = ' https://api.gandi.net/v5/livedns/domains/'+domain
# 封包資料
data='{"items": [{"rrset_type": "A","rrset_values": ["%s"],"rrset_ttl": 300}]}'%IP
Api_key= "Apikey "+token
header={'Authorization':Api_key}
req = requests.put(url,data,headers=header)
if req.text==str('{"message":"DNS Record Created"}'):
    logging.info('DNS Succes')
else:
    logging.error(req.text)

