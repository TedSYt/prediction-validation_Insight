#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:04:54 2018

@author: Ted
"""

import pandas as pd
import numpy as np

def read_data(file, chunksz = 100, sp = '|'):
    
    data_reader = pd.read_csv(file, chunksize = chunksz, sep = sp, header = None)
    
    data = pd.DataFrame()
    
    for df_data_pop in data_reader:
        
        data = data.append(df_data_pop)
        
    return data

#Define the address
#For the test 
#path_wd = '../insight_testsuite/tests/test_1/input/window.txt'
#path_ac = '../insight_testsuite/tests/test_1/input/actual.txt'
#path_pd = '../insight_testsuite/tests/test_1/input/predicted.txt'
#path_cp = '../insight_testsuite/tests/test_1/output/cmp_teat.txt'
  
#For the real project
path_wd = '../input/window.txt'
path_ac = '../input/actual.txt'
path_pd = '../input/predicted.txt'
path_cp = '../output/comparison.txt'

#Read the data
print('Reading the data...')
actual = read_data(path_ac,chunksz = 1000, sp = '|').values
predicted = read_data(path_pd,chunksz = 1000, sp = '|').values

total_hr = actual[-1,0]
window = int(np.loadtxt(path_wd))

#Empty Output 
error = np.zeros((total_hr, 2))
avg_error = []


#Calculating...
print('Calculating...')
for hour in range(1,total_hr+1): #???
    ac_temp = actual[actual[:,0]==hour]
    pd_temp = predicted[predicted[:,0]==hour]
    
    num_of_stks = 0
    total_er = 0
    for row in pd_temp:
        counterpart = ac_temp[ac_temp[:,1]==row[1]]
        if np.size(counterpart):
            total_er = total_er + np.abs(counterpart[0,2] - row[2])
            num_of_stks += 1
    error[hour-1] = [total_er/num_of_stks, num_of_stks]
        
    
#Output the result
print('Writing the file...')
file_object = open(path_cp, 'w')

for start in range(1, total_hr - (window-2)):
    err = 0
    total_match = 0
    for idx in range(window):
        total_match += error[start-1 + idx,1]
        err +=  error[start-1 + idx,1]*error[start-1 + idx,0]
    
    av_er = err/total_match   
    string = str(start)+'|'+str(start+window-1)+'|'+str(round(av_er,2))+'\n'
    avg_error.append(string)
    file_object.write(string)
    
file_object.close()

print('Done!')

    
    
    
    
    






