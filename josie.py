#josie put your code here!
import numpy as np
def I(l1, w1, hh, hw, w2, l2):
    term1=(w1*(l1**3))/12
    term2=(hh*(hw**3))/12
    term3=(w2*(l2**3))/12
    I=term1+term2+term3
    return I
import os
print(os.getcwd())
np.loadtxt("/Users/josiesoles/Downloads/W flange beams sae table.csv", dtype=str ,delimiter=',')

#pull url from github
url = 'https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/Beam%20Table.csv'
#read the CSV file with numpy example
csv_data = np.genfromtxt(url, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')