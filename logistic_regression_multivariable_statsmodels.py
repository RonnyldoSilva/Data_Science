import numpy as np
import statsmodels.api as sm
import pandas as pd
from sklearn.model_selection import train_test_split

base = pd.read_csv('../data/pontos_nas_dimensoes_porte_uf_idade_flag.csv', sep=';')
base2 = base[base['uf'] != 2]

x = pd.DataFrame(np.c_[base2['porte'], base2['uf'], base2['data_inicio_ativ']], columns=['porte','uf', 'data_inicio_ativ'])
y = pd.DataFrame(np.c_[base2['tem_protesto']], columns=['tem_protesto'])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.95, random_state=42)

xtrain = sm.add_constant(xtrain)
xtest = sm.add_constant(xtest)

model = sm.Logit(ytrain, xtrain)
result = model.fit(method='newton')

#xtest = ((result.predict(xtest) >= 0.2).astype(int))
xtest = result.predict(xtest)
ytest['xtest'] = xtest

print(ytest)
print(result.summary())
print('\n')