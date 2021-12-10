# final-project-jaime-wang
final-project-jaime-wang created by GitHub Classroo

project members: ziyao guo and haomin wang.

Introduction:  For the final project we choose the topic is house price forecasting. 
               Housing prices are an important indicator of the econmic operation, real estate developers and home buyers are paying close attention to the fluctuations in housing prices, and the construction of an effective housing price forcast model is of great significance to the financial market and people's livelihood. In the whole process of model construction, we first preprocess the data, and extract key features to analyze housing prices through visualization and basic model pre-training.



So far, we have been going well. It is very intuitive to see that some basic housing information can be extracted from the folder; then, through tables and charts show the sales price and housing type of comparative data information, which are the key information that customers are concerned about buying a house, such as which house residential style of the highest price, the size of each lot or the development time of the impact on the sales price; the use of linear regression charts shows that the different correlations with sale price are assessed through three aspects: the ground above the living area square feet, basement area and the assessment of the overall material and decoration of the house.

We also mapped the distribution density of house prices. By controlling the parameter distribution of the fit, it is possible to visually evaluate its correspondence with the observed data (black lines are the definite distribution, but the figure shows that this is the none value in the data, i.e. no fitting is performed). Meantime, we delete a column that contains more than five "none" values. Use get_dummies function to process the data.
