import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

base = pd.read_csv('../data/pontos_nas_dimensoes_porte_uf_idade.csv', sep=';')

def quantile_regression(xi, yi):
    print(xi + ' ' + yi)
    X = pd.DataFrame(np.c_[base[xi]], columns=[xi])
    Y = pd.DataFrame(np.c_[base[yi]], columns=[yi])

    xtrain, xtest, ytrain, ytest = train_test_split(X, Y, train_size=0.60, random_state=42)

    print("Model: Zero Inflated Poisson")
    zip_mod = sm.ZeroInflatedPoisson(ytrain, xtrain).fit(method="nm", maxiter=50)
    zip_mean_pred = zip_mod.predict(xtest, exog_infl=np.ones((len(xtest), 1)))
    zip_ppf_obs = stats.poisson.ppf(q=0.95, mu=zip_mean_pred)
    zip_rmse = np.sqrt(mean_squared_error(ytest, zip_ppf_obs))

    '''print("Model: Zero Inflated Neg. Binomial")
    zinb_mod = sm.ZeroInflatedNegativeBinomialP(ytrain, xtrain).fit(method="nm", maxiter=50)
    zinb_pred = zinb_mod.predict(xtest, exog_infl=np.ones((len(xtest), 1)))
    zinb_rmse = np.sqrt(mean_squared_error(ytest, zinb_pred))'''

    print("RMSE ZIP", zip_rmse)
    print("R2 ZIP", zip_mod.prsquared)
    '''print("RMSE ZINB: ", zinb_rmse)
    print("R2 ZINB", zinb_mod.prsquared)'''
    print('\n')

    '''plt.scatter(X, Y)
    plt.plot(X, zip_mod.predict(xtest), color = 'red')
    plt.title('Zero-inflated')
    plt.xlabel(xi)
    plt.ylabel(yi)
    plt.show()'''

def test():
    x_arr = ['porte', 'uf', 'data_inicio_ativ']
    y_arr = ['protestos', 'valorProtestado']

    for x in x_arr:
        for y in y_arr:
            quantile_regression(x, y)
            
test()