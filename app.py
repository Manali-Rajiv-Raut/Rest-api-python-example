#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import random


# In[ ]:


from flask import Flask ,jsonify ,request,redirect,url_for , make_response 
app = Flask(__name__)


# In[ ]:


@app.route('/mean', methods=['GET', 'POST'])
def meaning_and_quotes():
    name = request.args.get('name',type = str)
    #rint(name)
    initial_charactor = list((name).upper())[0]
    #print(initial_charactor)
    
    alp_data = pd.read_csv("alphabet_meaning.csv" , encoding= 'unicode_escape')
   
    for row in range(alp_data.shape[0]):
        if alp_data["Alphabet"][row] == initial_charactor :
            charactor_meaning = alp_data["Meaning"][row]  
            #print(charactor_meaning )
    quote_data = pd.read_csv("quotes.csv" , encoding= 'unicode_escape')
    random_num = random.choice(quote_data["QID"])
    #print(random_num)
    if random_num == len(quote_data) :
        random_num = random.choice(quote_data["QID"])
    else:
        pass
       
    quote = quote_data["Quotes"][random_num]
    
    result = {
              "\n Greeting": "Welcome "+name, 
              "\n Meaning of your name from initial charactor":""+charactor_meaning, 
              "\n Special quote for you": ""+quote,
        }
    return result
    


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




