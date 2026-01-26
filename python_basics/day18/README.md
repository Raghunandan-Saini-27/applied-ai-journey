
'''
-> What dataset is

Dataset is like the collection of data that we use to train,test and eavluate a ML model.

eg. Dataset=x+y where x is input data and y is output data we want to predict.

In short it is raw material req for an ml model.

-> What each metric means

It means on avg how wrong a model is.

it tells us avg absolute diff between 
1) actual value ,and 
2) predicted value

there are multiple types of metrics so far I have learned

1) mae = mean absolute error

eg. mae=7 model is off by 7 units.

2) mse= mean squared error

>Less the mse better the model more the mse worse the model as it is squared mean error so 2**2=4 small error whereas, 
10**10=100 Huge error

3) r2=coeff. of determination 

It means how much of the data's variation the model explains.

range : 1=perfect, 0=useless, <0 worse tha guessing

-> Is the model good or bad?'''

As of my linear regression model train on diabetes data it is like i would say around good as model has R2 score 0f 0.45 it means it explains 45% of the variation.