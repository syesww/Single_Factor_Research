import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 中位数绝对偏差去极值
def mad(factor):
    med = factor.median()
    mad = (factor - med).abs().median()

    high = med + (3 * 1.4826 * mad)
    low = med - (3 * 1.4826 * mad)

    factor = factor.clip(lower=low, upper=high)

    return factor

# 因子市值中性化处理
def market_cap_neutralize(df, x_column, y_column):
	# x为市值，当作特征值
	# y为目标因子

    x = np.array(df[x_column]).reshape(-1, 1)
    y = np.array(df[y_column])

    lr = LinearRegression()
    lr.fit(x, y)

    # 真实值-预测值的误差就是不受市值影响的部分
    y_predict = lr.predict(x)
    res = y - y_predict

    df['residual'] = res
    
    return df


# 因子标准化处理
def stand(factor):
    mean = factor.mean()
    std = factor.std()

    factor_standardized = (factor - mean) / std
    
    return factor_standardized



