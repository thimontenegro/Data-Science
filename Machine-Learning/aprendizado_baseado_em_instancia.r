#Utilizando o KNN
#install.packages("class",dependencies = T)
library(class)
head(iris)
summary(iris)
amostra = sample(2,150,replace = T, prob=c(0.7,0.3)) #criando e separando amostras de treino e teste

iris_treino = iris[amostra==1,] #treino 
classificar = iris[amostra==2,]#teste
%>% 
dim(iris_treino)
dim(classificar)
previsao = knn(iris_treino[,1:4],classificar[,1:4],iris_treino[,5], k=3)
tabela_confusao = table(classificar$Species, previsao)
tabela_confusao

