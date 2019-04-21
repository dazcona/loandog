#!/usr/bin/python

import random
import numpy as np

def get_transactions_data():

    user = []

    f = open("/web/data/data.yaml", 'r')
    line = f.readline()
    array_to_add = []
    
    while(line != ""):
        try:
            target_name = line.split(":")[0]
            content = line.split(":")[1].strip()
        except:
            a = None

        if " amount" in target_name:
            array_to_add = []
            array_to_add.append(float(content.strip().replace("'", "")))


        elif "bookingDate" in target_name:
            date = content.strip().replace("'", "")
            array_to_add.append(int(date.split("-")[2].split("T")[0]))


        elif "balanceamount" in target_name:
            array_to_add.append(float(content.strip().replace("'", "")))
            array_to_add.append(random.randint(0,4))
            user.append(array_to_add)

        line = f.readline()

    presentation = [[], [], [], [], []]
    
    for x in user:
        presentation[x[3]].append(x)
    
    array = np.zeros((5, 31))

    for i, x in enumerate(presentation):
        for y in x:
            array[i, y[1]-1] += y[0]
        
    return array  

