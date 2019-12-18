import requests
import socket
from bs4 import BeautifulSoup
from time import sleep
a=input("Enter the name or email:")
url = "http://viewdns.info/reversewhois/?q=" + a
org_dict = dict()
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
print(soup)
"""domain_list = [row('td')[0].string for row in domain_table.findAll('tr')]
if domain_list and domain_list[0] is not None:
    domain_list.remove("Domain Name")  # filter the header
    org_dict[search_terms] = domain_list"""
