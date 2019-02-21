import sys
from importlib import reload
reload(sys)


import pandas as pd
import requests
from joblib import Parallel, delayed             
import pickle                                   
from tqdm import tqdm                            


def html_extractor(url):                         
    try:
        cookies = dict(cookies_are='working')
        r = requests.get(url, cookies=cookies)
        return r.text
    except:
        return "no html"


clickbaits = pd.read_csv('/Users/yeezhianliew/Desktop/Clickbait.csv')             
non_clickbaits = pd.read_csv('/Users/yeezhianliew/Desktop/NonClickbait.csv')

clickbait_urls = clickbaits.status_link.values                    
non_clickbait_urls = non_clickbaits.status_link.values


clickbait_html = Parallel(n_jobs=40)(delayed(html_extractor)(u) for u in tqdm(clickbait_urls))    
pickle.dump(clickbait_html, open('/Users/yeezhianliew/Desktop/clickbait_html.pkl', 'wb'), -1)

non_clickbait_html = Parallel(n_jobs=40)(delayed(html_extractor)(u) for u in tqdm(non_clickbait_urls))
pickle.dump(non_clickbait_html, open('/Users/yeezhianliew/Desktop/non_clickbait_html.pkl', 'wb'), -1)


