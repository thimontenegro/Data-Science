#conjunto de dados iris
dim(iris)
head(iris)
summary(iris)
#Dados iris para tarefa de Classificacao
# Mas para agrupamento?

cluster = kmeans(iris[1:4],center= 3) #agrupar sem a classe, e 3 grupos
cluster

tabela = table(iris$Species, cluster$cluster)  #tabela dos grupos

#Gerando Grafico de dispersao
plot(iris[,1:4], col=cluster$cluster) #Gera grafico com os elementos de todas as linhas e das colunhas
#1-4 sem a classe, e com os agrupamentos gerados

#cor verde = setosa
#cor vermelha virginica
#preta = versicolor

#==================#
#USANDO FUZZY 
#==================#
#Um elemento pode esta mais de um grupo
library(e1071)
cluster = cmeans(iris[,1:4],center = 3) #3 grupos
cluster
tabela = table(iris$Species, cluster$cluster)
tabela
plot(iris[,1:4], col=cluster$cluster)
