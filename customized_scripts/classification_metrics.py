#!/usr/bin/env python
import sys
import numpy as np


def get_confusion(file,th=1e-6):
    '''We need to open the file and to read line by line, check what is the class and the evalue, and depending on the correspondace of the evalue to the trashold
    define the positives and negaives, and build the confusion matrix'''
    cm = np.zeros((2,2))
    with open(file) as fh:
        for line in fh:
            l = line.strip().split()
            evalue = float(l[1])
            class_ = int(l[2])
            if evalue> th:       #we could optimize like him, but this is clearer
                if class_ == 0:
                    cm[0,0] += 1
                elif class_ == 1:
                    cm[0,1] += 1
            elif evalue <= th:
                if class_ == 0:
                    cm[1,0] += 1
                elif class_ == 1:
                    cm[1,1] += 1
    return cm

#we have in the first row the true negatives and the fals negatives;
#in the second there are false positives and true positives

def get_accuracy(cm):
    return (cm[0,0] + cm[1,1])/np.sum(cm)

def get_mcc(cm):
    '''Matthew correlation coefficient'''
    n = cm[0,0]cm[1,1]-cm[0,1][1,0]   #numerator
    d = np.sqrt((cm[0,0]+cm[1,1])(cm[0,0]+cm[0,1]) * (cm[1,1]+cm[0,1])(cm[1,1]+cm[1,0])) #denominator
    return n/d

if _name=='main_':
    file = sys.argv[1]
    th = float(sys.argv[2])   #trashold
    confusion = get_confusion(file,th)
		print(confusion)            #around [[1.97..,2][2.87.. ,3.47..]
    acc = get_accuracy(confusion)
    mcc = get_mcc(confusion)
    print("TH: ",th,"Q2: ",acc,"MCC: ",mcc)   #acc around 0.9857
