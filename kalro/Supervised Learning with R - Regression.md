
# Regression

In this task, one wishes to find some simple pattern in the data - a functional relationship between the X and Y components of the data. Linear regression was developed in the field of statistics and is studied as a model for understanding the relationship between input and output numerical variables assumes a linear relationship between the input variables (x) and the single output variable (y). More specifically, that y can be calculated from a linear combination of the input variables (x).

These equations take the form Y=∑ni=1BiXi+e

As we already know, the objective of regression learning is to obtain the values of the coefficients that will minimize the difference between the predicted value and the actual value given the training examples.

## 1.  Simple Linear Regression

Simple linear regression is used to predict the value of an outcome variable Y based on one input predictor variables X.
&gt; The goal is to come up with a linear relationship (a mathematical formula) between the predictor variable and the response variable. This mathematical formula will then be used to estimate the value of the response variable Y, when the predictor variable X value is known.

This mathematical equation can be generalized as follows:
&gt; Y = β1 + β2X + ϵ

where, β1 is the intercept and β2 is the slope. Collectively, they are called regression coefficients. ϵ is the error term, the part of Y the regression model is unable to explain.

#### 1.1 Simple Linear Regression Code Example
```{R}
head(mtcars)
```


```{R}
## Example 
# ---
# Simple linear regression example 
# ---
# OUR CODE GOES BELOW
# 

# Let's first import ggplot
library(ggplot2) 

# Examining the data before fitting models by creating a scatter plot 
# Scatter plots can help visualize any linear relationships between the dependent (response) variable 
# and independent (predictor) variables. 
ggplot(mtcars, aes(hp, mpg))+
  geom_point()+
  labs(title = "Gross Horse Power VS Miles Per Gallon",
       x = "hp",
       y = "mpg")

```

```{R}
# Examining the data by also finding the correlation coefficient
# Correlation is a statistical measure that suggests the level of linear dependence between two variables.
# Correlation can take values between -1 to +1. If we observe for every instance where speed increases, 
# the distance also increases along with it, then there is a high positive correlation between them 
# and therefore the correlation between them will be closer to 1. 
# The opposite is true for an inverse relationship, in which case, the correlation between the variables will be close to -1.
cor(mtcars$hp, mtcars$mpg)


```


```{R}
# The linear model function lm, used below will create the relationship model between the predictor and the response variable. 
# mpg~hp presenting the relation between x and y and mtcars the vector on which the formula will be applied.
simple_lm <- lm(mpg~hp, mtcars)
simple_lm


```


```{R}
# Generating the anova table. This table will 
# contain the sums of squares, degrees of freedom, F statistic, and p value
# 
anova(simple_lm)


```


```{R}
# Predicting the response variables
# 
pred1 <- predict(simple_lm, mtcars)
pred1


```

#### 1.2 Simple Linear Regression Code Example 


```R
## Example 
# ---
# 
# Considering two vectors
height <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
weight <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

# Examining the data by also finding the correlation coefficient
cor(height, weight)

# Apply the lm() function.
relation <- lm(weight~height)
relation


```


```R
# Then getting the Summary of the relationship
summary(relation)


```


```R
# Then wrapping the parameters inside a new data frame named 
# and later finding the weight of a person with height 170 and 
# 
a <- data.frame(height = 170)
result <-  predict(relation,a)

result


```

#### 1.3 Simple Linear Regression Code Example


```R
# Challenge
# ---
# Apply simple linear regression to the faithful dataset 
# and estimate the next eruption duration if the waiting time 
# since the last eruption has been 80 minutes
# ---
# OUR CODE GOES BELOW
# 

# Previewing the database
# 
head(faithful)

# Examining the data before fitting models by creating a scatter plot
# 

```


```R
# Examining the data by also finding the correlation coefficient


```


```R
# Applying the lm() function.


```


```R
# Working on the solution


```

## 2.  Multiple Linear Regression

Multiple linear regression is an extension of simple linear regression used to predict an outcome variable (y) on the basis of multiple distinct predictor variables (x). In simple linear relation we have one predictor and one response variable, but in multiple regression we have more than one predictor variable and one response variable.

With three predictor variables (x), the prediction of y is expressed by the following equation:

&gt; y = b0 + b1*x1 + b2*x2 + b3*x3

#### 2.1 Multiple Linear Regression Code Example


```{R}
## Example  
# ---
# Multiple Linear Regression Example 
# ---
# Use the diamonds dataset
# 

head(diamonds)


```


```{R}
# Applying the lm() function.
multiple_lm <- lm(price ~ ., diamonds)

summary(multiple_lm)
```


```{R}
# Generating the anova table
anova(multiple_lm)


```


```{R}
# Then performing our prediction 
pred2 <- predict(multiple_lm, diamonds)


# Printing out our result
head(pred2)


```

#### 2.2 Multiple Linear Regression Code Example


```R
# Having "disp","hp" and "wt" as predictor variables - we've selected these variables from the mtcars database
input <- mtcars[,c("mpg","disp","hp","wt")]

# Previewing these selected input predictor variables
head(input)
 

```


```R
# Creating the relationship model
model <- lm(mpg~disp+hp+wt, data = input)


```


```R
# Getting the summary of the model 


```


```R
# For a car with disp = 221, hp = 102 and wt = 2.91 the predicted mileage is 
# 
a <- data.frame(disp = 221, hp = 102, wt = 2.91)
predicted_mileage <- predict(model, a)

# printing the predicted mileage
pred2


```

#### 2.3 Multiple Linear Regression Code Example



```R
## Challenge  
# ---
# Apply multiple linear regression  for the stackloss dataset, 
# and predict the stack loss if the air flow is 62, water temperature is 19 and acid concentration is 84.
# ---
# OUR CODE GOES BELOW
# 

# Previewing the database stackloss
# 
head(stackloss)


```

### 3. Cross Validation

How do we know that an estimated regression model is generalizable beyond the sample data used to fit it? Ideally, we can obtain new independent data with which to validate our model. For example, we could refit the model to the new dataset to see if the various characteristics of the model (e.g., estimates regression coefficients) are consistent with the model fit to the original dataset.

However, most of the time we cannot obtain new independent data to validate our model. An alternative is to partition the sample data into a training (or model-building) set, which we can use to develop the model, and a validation (or prediction) set, which is used to evaluate the predictive ability of the model. This is called cross-validation. Again, we can compare the model fit to the training set to the model refit to the validation set to assess consistency. The simplest approach to cross-validation is to partition the sample observations randomly with 50% of the sample in each set.

Instead of doing a single training/testing split, we can systematise this process, produce multiple, different out-of-sample train/test splits, that will lead to a better estimate of the out-of-sample RMSE.

For 3-fold valiadation for instance, we split the data into 3 random and complementary folds, so that each data point appears exactly once in each fold. This leads to a total test set size that is identical to the size as the full dataset but is composed of out-of-sample predictions.

Schematic of 3-fold cross validation producing three training (blue) and testing (white) splits.

After cross-validation, all models used within each fold are discarded, and a new model is build using the whole dataset, with the best model parameter(s), i.e those that generalised over all folds.

This makes cross-validation quite time consuming, as it takes x+1 (where x in the number of cross-validation folds) times as long as fitting a single model, but is essential.

It is important to maintain the class proportions within the different folds, i.e. respect the proportion of the different classes in the original data. This is also taken care when using the caret package.

The procedure of creating folds and training the models is handled by the train function in caret. Below, we apply it to the diamond price example that we used when introducing the model performance.
&gt; 1. We start by setting a random to be able to reproduce the example.

&gt; 2. We specify the method (the learning algorithm) we want to use. Here, we use “lm”, but, as we will see later, there are many others to choose from.

&gt; 3. We then set the out-of-sample training procedure to 10-fold cross validation (method = "cv" and number = 10).

To simplify the output in the material for better readability, we set the verbosity flag to FALSE, but it is useful to set it to TRUE in interactive mode.



#### 3.1 Cross Validation Code Example


```R
## Example 
# ---
# Cross Validation Example 
# ---
# OUR CODE GOES BELOW
# 

# Using the previous diamonds dataset 
set.seed(42)

multiple_lm2 <- train(price ~ ., diamonds,
               method = "lm", 
               trControl = trainControl(method = "cv", 
                                        number = 10, 
                                        verboseIter = FALSE))
summary(multiple_lm2)

multiple_lm2
```


```R
# Once we have trained our model, we can directly use this train object as input to the predict method:

pred3 <- predict(multiple_lm2, diamonds)

error <- pred3 - diamonds$price

rmse_xval <- sqrt(mean(error^2)) ## xval RMSE

rmse_xval


```


```R
## Challenge
# ---
# Question: Train a linear model using 10-fold cross-validation and then use it to predict the median 
# value of owner-occupied homes in Boston from the Boston dataset as described above. Then calculate the RMSE.
# ---
# OUR CODE GOES BELOW
# 

```
