#josie put your code here!
import numpy as np
def I(l1, w1, hh, hw, w2, l2):
    term1=(w1*(l1**3))/12
    term2=(hh*(hw**3))/12
    term3=(w2*(l2**3))/12
    I=term1+term2+term3
    return I

