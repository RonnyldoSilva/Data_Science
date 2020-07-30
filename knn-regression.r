df <- data(iris) ##load data
 head(iris) ## see the studcture##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
 ## 1          5.1         3.5          1.4         0.2  setosa
 ## 2          4.9         3.0          1.4         0.2  setosa
 ## 3          4.7         3.2          1.3         0.2  setosa
 ## 4          4.6         3.1          1.5         0.2  setosa
 ## 5          5.0         3.6          1.4         0.2  setosa
 ## 6          5.4         3.9          1.7         0.4  setosa##Generate a random number that is 90% of the total number of rows in dataset.
 ran <- sample(1:nrow(iris), 0.9 * nrow(iris)) 
 
 ##the normalization function is created
 nor <-function(x) { (x -min(x))/(max(x)-min(x))   }
 
 ##Run nomalization on first 4 coulumns of dataset because they are the predictors
 iris_norm <- as.data.frame(lapply(iris[,c(1,2,3,4)], nor))
 
 summary(iris_norm)##   Sepal.Length     Sepal.Width      Petal.Length     Petal.Width     
 ##  Min.   :0.0000   Min.   :0.0000   Min.   :0.0000   Min. :0.00
 ##  1st Qu.:0.2222   1st Qu.:0.3333   1st Qu.:0.1017   1st Qu.:0.08  
 ##  Median :0.4167   Median :0.4167   Median :0.5678   Median :0.50
 ##  Mean   :0.4287   Mean   :0.4406   Mean   :0.4675   Mean   :0.45
 ##  3rd Qu.:0.5833   3rd Qu.:0.5417   3rd Qu.:0.6949   3rd Qu.:0.70
 ##  Max.   :1.0000   Max.   :1.0000   Max.   :1.0000   Max.   :1.00##extract training set
iris_train <- iris_norm[ran,] ##extract testing set
 iris_test <- iris_norm[-ran,]  ##extract 5th column of train dataset because it will be used as 'cl' argument in knn function.
 iris_target_category <- iris[ran,5] ##extract 5th column if test dataset to measure the accuracy
 iris_test_category <- iris[-ran,5]##load the package class
 library(class) ##run knn function
 pr <- knn(iris_train,iris_test,cl=iris_target_category,k=13)
 
 ##create confusion matrix
 tab <- table(pr,iris_test_category)
 
 ##this function divides the correct predictions by total number of predictions that tell us how accurate teh model is.
 
 accuracy <- function(x){sum(diag(x)/(sum(rowSums(x)))) * 100}
 accuracy(tab)## [1] 80
