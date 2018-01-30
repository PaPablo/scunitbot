# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[104]:

def get_phrase():

    #extracts random phrase from the dictionary
    def random_phrase(ph):
        import random
        random_selector = random.SystemRandom()

        unit = random_selector.choice(ph)
        phrase_type = random_selector.choice([k for k in unit.keys() if k not in ['Name','Unit Summary']])
        phrase = random_selector.choice(unit[phrase_type])
        return {'name':unit['Name'],'phrase':phrase}

    units = pd.read_csv('sc_units_phrases.csv')
    heroes = pd.read_csv('sc_heroes_phrases.csv')

    import math

    complete = units.append(heroes).fillna(value='')
    columns = complete.columns
    col_phrases = [c for c in columns if c!= 'Name']
    phrases = []
    for i,r in complete.iterrows():
        unit ={}
        unit['Name']=r['Name']
        for c in col_phrases:
            if r[c]!='':
                unit[c] = [p for p in r[c].split(';') if p != '']
        phrases.append(unit)
    return random_phrase(phrases)

