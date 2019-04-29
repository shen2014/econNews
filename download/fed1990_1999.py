

# -*- coding: utf-8 -*-

import urllib.request

from bs4 import BeautifulSoup

import shutil

years = list(range(1990, 2000))

save_dir = './savedownload1990_1999/'


for year in years:
    
    url = 'https://www.federalreserve.gov/monetarypolicy/fomchistorical' + str(year) + '.htm'
    
    source_file = './htm_source/source_' + str(year) + '.htm'
    
    with urllib.request.urlopen(url) as response, open(source_file, 'wb') as f:
        
        shutil.copyfileobj(response, f)
        
        
    with open(source_file) as f:
        
        soup = BeautifulSoup(f, 'html.parser')

        #print(soup.prettify())
    
        hrefs = soup.findAll('a', href = True)
    
        print('fetching minutes of year {0}'.format(year))
        minutes_ref = []
  
        for ref in hrefs:
        
            if year <= 1992:
        
                if  ref.attrs['href'][0:29] == '/monetarypolicy/files/fomcmoa'  and ref.attrs['href'][-4:] == '.pdf':
               
                    minutes_ref.append(ref)
    
            else:
                
                if  ref.text == 'Minutes':
           
                    minutes_ref.append(ref)
                    
        minutes_url = []
        
        for ref in minutes_ref:
        
            url_link = "https://www.federalreserve.gov" + ref.attrs['href']
        
            minutes_url.append(url_link)
            
        for url in minutes_url:
    
            file_name   =  url.split('/')[-1]
    
            file_name   =  save_dir + 'minutes_' + file_name 
    
            with urllib.request.urlopen(url) as response, open(file_name, 'wb') as f:

                shutil.copyfileobj(response, f)      
        

