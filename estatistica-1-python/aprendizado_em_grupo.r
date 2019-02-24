#Ensamble Learning
#install.packages("randomForest",dependeces = T)
install.packages("randomForest",dependencies = T)
library(randomForest)
credito = read.csv(file.choose(), sep=',', header = T)

#Selecao de amostras
amostra = sample(2,1000, replace=T,prob=c(0.7,0.3))
credito_treino = credito[amostra==1,]
credito_teste = credito[amostra==2,]

floresta = randomForest(class ~ ., data=credito_treino, ntree=100, importance = T)
#MeanDecreaseAccurance = Nivel de Importancia sem o elemento 
#MeanDecreaseGini = Grau de Pureza do elemento

varImpPlot(floresta)
previsao = predict(floresta,credito_teste)
tabela_confusao = table(previsao, credito_teste$class)
tabela_confusao

taxa_acerto = (tabela_confusao[1] + tabela_confusao[4])/sum(tabela_confusao)
taxa_acerto

#taxa de erros
taxa_erros = (tabela_confusao[2] + tabela_confusao[3])/sum(tabela_confusao)
taxa_erros