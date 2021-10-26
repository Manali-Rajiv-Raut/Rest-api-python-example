#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random


# In[2]:


from flask import Flask ,jsonify 
app = Flask(__name__)


# In[3]:


@app.route('/', methods=['GET', 'POST'])
def meaning_and_quotes():
    name = request.args.get('name',type = str)
    #print(name)
    initial_charactor = list((name).upper())[0]
    #print(initial_charactor)
    
    alp_data = pd.read_csv("alphabet_meaning.csv" , encoding= 'unicode_escape')
   
    for row in range(alp_data.shape[0]):
        if alp_data["Alphabet"][row] == initial_charactor :
            charactor_meaning = alp_data["Meaning"][row]  
            print(charactor_meaning )
    quote_data = pd.read_csv("quotes.csv" , encoding= 'unicode_escape')
    random_num = random.choice(quote_data["QID"])
    #print(random_num)
    if random_num == len(quote_data) :
        random_num = random.choice(quote_data["QID"])
    else:
        pass
       
    quote = quote_data["Quotes"][random_num]
    
    result = {
              "Greeting": "Welcome "+name, 
              "Meaning of your name from initial charactor": "\n"+charactor_meaning, 
              "Special quote for you": "\n"+quote,
        }
    return result
    


# In[4]:


if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:




