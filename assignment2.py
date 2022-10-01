print("In this assignment, you will write a program that scapes the Wikipedia list of top-level domains and writes a " +
       "CSV file that contains all the top-level domains and whether their "'example'" "+
       "second-level domain resolves to an address that returns an HTTP responses. \n")

import requests
from bs4 import BeautifulSoup
import re
import csv

p = re.compile("^(.)")
exclude = ".भारत";

#Check if value of string starts with .
def is_absolute(domain):
    return bool(domain.startswith("."))

#Writes to csv 
def csv_generat(domain, api ,output):
    fieldnames = ['domain', 'api', 'output']    
    with open("./BIA660-Assignment2/file.csv", 'a', newline='') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=fieldnames)              
       writer.writerow({'domain': domain, 'api': api,'output': output })

#Get request to check responce
def check_second_domain(domains):           
    domian_split = domains.split()
    for domain in domian_split:
       if domain not in exclude:
              try:
                     api = "http://example"+domain
                     getResponce = requests.get(api);    
                     csv_generat(domain,api,getResponce)
              except requests.exceptions.RequestException as error:
                     csv_generat(domain,api,error)


getResponce = requests.get("https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains");

#Parse the response of type html 
soup = BeautifulSoup(getResponce.content, 'html.parser')

#Loop html and find all the tables and collect domain 
for tr in soup.find_all('tr')[1:]:
     tds = tr.find_all('td')
     cols = [ele.text.strip() for ele in tds]  
     for domain in cols:              
       if is_absolute(domain):
              check_second_domain(domain)
       break;

print(" Gracefully completed ")