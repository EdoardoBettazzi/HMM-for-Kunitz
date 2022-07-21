#!/usr/bin/env python
import sys
import numpy as np


def get_confusion(file,th=1e-6):
    '''
    Takes in input:
    - a file containing the ground-truth classification and the model
    predicted e-value for each protein identifier.
    - a threshold used to classify each protein in relation to the 
    predicted e-value 

    Returns a confusion matrix.
    '''
    cm = np.zeros((2,2))
    with open(file) as fh:
        for line in fh:
            l = line.strip().split()
            evalue = float(l[1])
            class_ = int(l[2])
            if evalue> th:
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

def get_accuracy(cm):
    return (cm[0,0] + cm[1,1])/np.sum(cm)

def get_mcc(cm):
    '''Matthew correlation coefficient'''
    n = cm[0,0]*cm[1,1]-cm[0,1]*cm[1,0]
    d = np.sqrt((cm[0,0]+cm[1,1])*(cm[0,0]+cm[0,1])*(cm[1,1]+cm[0,1])*(cm[1,1]+cm[1,0]))
    return n/d

if __name__=='__main__':
  file = sys.argv[1]
  th = float(sys.argv[2])
  confusion = get_confusion(file,th)           
  acc = get_accuracy(confusion)
  mcc = get_mcc(confusion)
  print ("TH:",th,"Accuracy:",acc,"MCC:",mcc,"TN:",confusion[0,0],"FN:",confusion[0,1], "FP:",confusion[1,0], "TP:",confusion[1,1])
