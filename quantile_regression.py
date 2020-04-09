import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

data = sm.datasets.engel.load_pandas().data
print(data.head())

mod = smf.quantreg('foodexp ~ income', data)
res = mod.fit(q = 0.5)
print(res.summary())
print(res.prsquared)

prsquareds = []
quantiles = np.arange(.05, .96, .1)
def fit_model(q):
    res = mod.fit(q=q)
    prsquareds.append(res.prsquared)
    return [q, res.params['Intercept'], res.params['income']] + \
            res.conf_int().loc['income'].tolist()

models = [fit_model(x) for x in quantiles]
models = pd.DataFrame(models, columns=['q', 'a', 'b', 'lb', 'ub'])

ols = smf.ols('foodexp ~ income', data).fit()
ols_ci = ols.conf_int().loc['income'].tolist()
ols = dict(a = ols.params['Intercept'],
           b = ols.params['income'],
           lb = ols_ci[0],
           ub = ols_ci[1])

print(models)
print(ols)

x = np.arange(data.income.min(), data.income.max(), 50)
get_y = lambda a, b: a + b * x

fig, ax = plt.subplots(figsize=(8, 6))

colors = ['black', 'red', 'blue', 'green', 'grey', 'purple', 'pink', 'darkgreen', 'orange', 'cyan', 'lightgreen', 'gold']

for i in range(models.shape[0]):
    y = get_y(models.a[i], models.b[i])
    ax.plot(x, y, linestyle='dotted', color=colors[i], label=str(quantiles[i])[0:4] + "_r2=" + str(prsquareds[i])[0:5])

y = get_y(ols['a'], ols['b'])

ax.plot(x, y, color='red', label='OLS_r2=' + str(res.prsquared)[0:5])
ax.scatter(data.income, data.foodexp, alpha=.2)
ax.set_xlim((240, 3000))
ax.set_ylim((240, 2000))
legend = ax.legend()
ax.set_xlabel('Income', fontsize=16)
ax.set_ylabel('Food expenditure', fontsize=16)
plt.show()
