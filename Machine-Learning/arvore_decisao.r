#installar install.packages("rpart",dependences=T)
install.packages("rpart", dependendecies = T)
library(rpart)

credito = read.csv(file.choose(), sep=',', header = T)

#Selecao de amostras
amostra = sample(2,1000, replace=T,prob=c(0.7,0.3))
credito_treino = credito[amostra==1,]
credito_teste = credito[amostra==2,]

arvore = rpart(class ~ ., data=credito_treino,method='class')
print(arvore)
plot(arvore) #plota a arvore
text(arvore, use.n=T, all=T,cex=.8)

teste = predict(arvore, newdata=credito_teste)
teste

#avalicao
cred = cbind(credito_teste,teste) #cria coluna com bad e good
fix(cred)

cred['Result'] = ifelse(cred$bad >= 0.5, 'bad', 'good') #cria coluna baseada no if
fix(cred)

#tabela de confusao
tabela_confusao = table(cred$class,cred$Result) #classificao final
tabela_confusao

#taxa de acertos
taxa_acerto = (tabela_confusao[1] + tabela_confusao[4])/sum(tabela_confusao)
taxa_acerto
#taxa de erros
taxa_erro = (tabela_confusao[2] + tabela_confusao[3])/sum(tabela_confusao)
taxa_erro