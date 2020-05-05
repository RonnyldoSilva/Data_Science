import numpy as np
import statsmodels.api as sm

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])
x = sm.add_constant(x)

model = sm.Logit(y, x)

result = model.fit(method='newton')

print('\n')
print(result.params)
print('\n')
print(result.predict(x))
print('\n')
print(result.pred_table())
print('\n')
print(result.summary2())