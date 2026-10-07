import numpy as np

x = np.array([1, 2, 3, 4])
print(x)


# =================================================
print("=================================================")


print(np.mean(np.array([10, 20, 30])))
print(np.median(np.array([1, 2, 100])))


x = np.array([5, 2, 9, 1])
print(np.sum(x))
print(np.min(x))
print(np.max(x))



# =================================================
print("=================================================")

x = np.array([1, 2, 3, 4, 5, 6])
print(x.reshape(2, 3))


# =================================================
print("=================================================")


import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Omar"],
    "Age": [20, 22, 21]
    })
print(df)


ages = pd.Series([20, 22, 21])
print(ages)


df2 = pd.DataFrame({
"Department": ["IT", "IT", "HR"],
"Salary": [5000, 6000, 4000]
})
print(df2.groupby("Department")["Salary"].mean())


# =================================================
print("=================================================")


import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [10, 20, 15]
#plt.plot(x, y)
#plt.show()



# =================================================
print("=================================================")

from scipy import stats

data = [10, 20, 30]
print(stats.tmean(data))

print(stats.zscore([10, 20, 30]))


# =================================================
print("=================================================")

from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42
)
print(X_train)
print(X_test)


# =================================================
print("=================================================")

import torch

x = torch.tensor([1, 2, 3])
print(x)


print(torch.zeros(2, 3))
print(torch.ones(2, 2))