###################################
# Import modules
###################################

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from numpy import genfromtxt, savetxt

###################################
# Attempy at Random Forest
###################################

def main():
    #create the training & test sets, skipping the header row with [1:]
    #dataset = genfromtxt(open('bls_test_data.csv','r'), delimiter=',', dtype='f8')[1:]
    df = pd.read_csv(('bls_data.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in df]
    train = [x[1:] for x in df]
    #test = genfromtxt(open('bls_test_data.csv','r'), delimiter=',', dtype='f8')[1:]
    test = pd.read_csv(('bls_data.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)

    savetxt('bls_result.csv', rf.predict(test), delimiter=',', fmt='%f')

###################################
# Run script
###################################

if __name__=="__main__":
    main()