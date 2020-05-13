# My Data Science
 
### Requeriments Setup:

* statsmodels
* pandas
* numpy
* matplotlib

### Examples

Discrete quantile regression:
![](https://github.com/RonnyldoSilva/Data_Science/blob/master/Figure_2.png)

Continuos quantile regression:
![](https://github.com/RonnyldoSilva/Data_Science/blob/master/quantile_regression_example.png)
```
       income     foodexp
0  420.157651  255.839425
1  541.411707  310.958667
2  901.157457  485.680014
3  639.080229  402.997356
4  750.875606  495.560775
                         QuantReg Regression Results                          
==============================================================================
Dep. Variable:                foodexp   Pseudo R-squared:               0.6206
Model:                       QuantReg   Bandwidth:                       64.51
Method:                 Least Squares   Sparsity:                        209.3
Date:                qui, 09 abr 2020   No. Observations:                  235
Time:                        09:17:42   Df Residuals:                      233
                                        Df Model:                            1
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     81.4823     14.634      5.568      0.000      52.649     110.315
income         0.5602      0.013     42.516      0.000       0.534       0.586
==============================================================================

The condition number is large, 2.38e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
      q           a         b        lb        ub
0  0.05  124.880099  0.343361  0.268632  0.418090
1  0.15  111.693660  0.423708  0.382780  0.464636
2  0.25   95.483539  0.474103  0.439900  0.508306
3  0.35  105.841294  0.488901  0.457759  0.520043
4  0.45   81.083647  0.552428  0.525021  0.579835
5  0.55   89.661370  0.565601  0.540955  0.590247
6  0.65   74.033434  0.604576  0.582169  0.626982
7  0.75   62.396584  0.644014  0.622411  0.665617
8  0.85   52.272216  0.677603  0.657383  0.697823
9  0.95   64.103964  0.709069  0.687831  0.730306
{'a': 147.47538852370573, 'b': 0.48517842367692354, 'lb': 0.4568738130184233, 'ub': 0.5134830343354237}

```

### Pandas
Delete row by value:
```python
df = df[df.uf != target]
```
