# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import array
import numpy as np

FileInput = open('out.txt')

#Matrix for newfile
probe,mean,std,var =   ([[],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        []] for z in range (4))

i = 0
j = 0
cnt = 0
sumTemp = 0

newfilecnt = 11

while 1: 
      
    # read by character 
    char = FileInput.read(1)           
    if not char:  
        break
          
    if char == '+':
        #read time value
        temp =FileInput.read(11)
        #replace question marks for float conversion
        temp = temp.replace('?', '0')
        #convert to µs
        temp = float(temp)*1000000
        #set the inital value to zero as reference
        if i == 0 :
            temp = 0
        #write to matrix
        probe[i].append(temp)
        sumTemp += temp
        i += 1
        cnt += 1
        if i == newfilecnt:
            probe[i].append(sumTemp)
            sumTemp = 0
            i = 0
  
FileOutput = open('result.txt',"w")

for j in range(newfilecnt+1):
    #creating mean
    FileOutput.write("Mean of probe " + str(j)+ ": ")
    mean[j] = np.mean(probe[j])
    mean[j] = round(mean[j],2)
    FileOutput.write(str(mean[j]))
    FileOutput.write("\n")
FileOutput.write("\n")

for j in range(newfilecnt+1):
    #creating variance
    FileOutput.write("Var of probe " + str(j)+ ": ")
    var[j] = np.var(probe[j])
    var[j] = round(var[j],2)
    FileOutput.write(str(var[j]))
    FileOutput.write("\n")
FileOutput.write("\n")
   
for j in range(newfilecnt+1):
    #creating standard aviation
    FileOutput.write("Std of probe " + str(j)+ ": ")
    std[j] = np.std(probe[j])
    std[j] = round(std[j],2)
    FileOutput.write(str(std[j]))
    FileOutput.write("\n")
FileOutput.write("\n")

FileOutput.write("Measurement Count= "+ str(cnt/newfilecnt))
    
FileInput.close() 
FileOutput.close() 
