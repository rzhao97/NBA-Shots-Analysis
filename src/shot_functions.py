import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
sns.set(color_codes=True)

def binary_shot_result(shot):
    if shot == 'made':
        return 1
    else:
        return 0
    
def game_seconds(period, clock):
    '''
    Parameters:
    -----------
    period: int
    clock: string
    '''
    # First 4 periods are 12 min
    if period <= 4:
        p_secs = period * 720
    # OT periods are 5 min
    else:
        ot = period - 4
        p_secs = 2880 + (ot * 300)

    # Remove the time left in the period
    minsec = clock.split(':')
    c_secs = (int(minsec[0]) * 60) + int(minsec[1])
    
    return p_secs - c_secs

def third():
    pass