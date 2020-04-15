import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

df = pd.read_csv('../data/pontos_nas_dimensoes_porte_uf_idade.csv', sep=';')

mod = smf.quantreg('protestos ~ porte', df)
res = mod.fit(q = 0.5)
res_ols_prsquared = res.prsquared
print(res.summary())
print(res.prsquared)

quantiles = np.arange(.85, .99, .01)

# get all result instances in a list
prsquareds = []
res_all = []
for q in quantiles:
    res = mod.fit(q=q)
    prsquared = res.prsquared
    prsquareds.append(prsquared)
    res_all.append(res)

res_ols = smf.ols('protestos ~ porte', df).fit()

plt.figure()

# create x for prediction
x_p = np.linspace(df.porte.min(), df.porte.max(), 50)
df_p = pd.DataFrame({'porte': x_p})

colors = ['black', 'red', 'blue', 'green', 'grey', 'purple', 'pink', 'darkgreen', 'orange', 'cyan', 'lightgreen', 'gold', 'darkblue', 'yellow', 'lightblue']
i = 0
for qm, res in zip(quantiles, res_all):
    # get prediction for the model and plot
    # here we use a dict which works the same way as the df in ols
    plt.plot(x_p, res.predict({'porte': x_p}), linestyle='--', lw=1, color=colors[i], zorder=2, label=str(qm)[0:4] + "_r2=" + str(prsquareds[i]))
    i += 1

y_ols_predicted = res_ols.predict(df_p)
plt.plot(x_p, y_ols_predicted, color='red', zorder=1, label='OLS' + "_r2=" + str(res_ols_prsquared))
plt.plot(df.porte, df.protestos, 'o', alpha=.2, zorder=0)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('porte')
plt.ylabel('protestos')
plt.title('')
plt.show()
