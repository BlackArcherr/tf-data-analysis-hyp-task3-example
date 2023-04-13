import pandas as pd
import numpy as np
import scipy.stats as stats
chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    a, p = stats.ttest_ind(x, y)
    return p < 0.07
