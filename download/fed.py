

import urllib.request

from bs4 import BeautifulSoup

import shutil, os

       

source_file_url_fomc_meetings = 'source_fomccalendars.htm'

with open(source_file_url_fomc_meetings) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    #print(soup.prettify())
    
    hrefs = soup.findAll('a', href = True)
    
    monetary_policy_ref = []
  
    for ref in hrefs:
        
        ref_text = ref.text
        
        if  ref_text[0:15] == '/monetarypolicy'  and ref_text[-4:] == '.pdf':
       
            monetary_policy_ref.append(ref)
    
    monetary_policy_url = []
    for ref in monetary_policy_ref:
        
        url_link = "https://www.federalreserve.gov" + str(ref.text)
        
        monetary_policy_url.append(url_link)
        
        
        
for url in monetary_policy_url:
    
    file_name   =  url.split('/')[-1]
    
    file_name   = './savedownload/' + file_name 
    

    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as f:

        shutil.copyfileobj(response, f)        