import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 682912115 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    #var_x = np.var(x)
    #n = x.shape[0]
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return np.sqrt((loc - scale * norm.ppf(1 - alpha / 2))/6), \
           np.sqrt((loc - scale * norm.ppf(alpha / 2))/6)
