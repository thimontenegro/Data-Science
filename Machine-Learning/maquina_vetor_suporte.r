credito = read.csv(file.choose(), sep=',',header=T)
head(credito)

dim(credito) #1000 instancias e 21 colunas
#gerar array de 1-2, de forma de 70% de treino e 30% teste
amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))
#separr conjunto de teste e de treino
credito_Treino = credito[amostra==1,] #cria modelo com dados de treino
credito_Teste = credito[amostra==2,] #cria modelo com dados de teste

modelo = svm(class ~ . ,credito_Treino) #utilizar todos os atributos

predicao = predict(modelo, credito_Teste)
predicao

tabela_confusao = table(credito_Teste$class, predicao)
tabela_confusao

#taxa de acertos
taxa_acerto = (tabela_confusao[1] + tabela_confusao[4])/sum(tabela_confusao)
taxa_acerto
#73.74% de acertos

#taxa de erros
taxa_erros = (tabela_confusao[2] + tabela_confusao[3])/sum(tabela_confusao)
taxa_erros
#26.25% de erros

#Refinando nossos conjuntos de avaliacao

#selecionar os atributos mais relevantes
#install.packages('FSelector', dependencies = T) package de selecao de atributos
#library(FSelector)

random.forest.importance(class ~ ., credito) #TODO O CONJUNTO D DANDOS
#seleciona os mais 
#quanto cada um é importante para previsao correta p/ bom ou mal pagador
#criando novo modelo com os dados mais importantes
amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))
novo_credito_Treino = credito[amostra==1,] #cria modelo com dados de treino
novo_credito_Teste = credito[amostra==2,] #

modelo = svm(class ~ checking_status + duration + credit_history + credit_amount, novo_credito_Treino)
modelo

#nova predicao com o novo modelo teste
nova_predicao = predict(modelo,novo_credito_Teste)
nova_predicao

#criacao da tabela confusao
tabela_confusao = table(novo_credito_Teste$class,nova_predicao)
tabela_confusao
#taxa de acertos
taxa_acerto2 = (tabela_confusao[1] + tabela_confusao[4])/sum(tabela_confusao)
taxa_acerto2
#taxa de erros
taxa_de_erros2 = (tabela_confusao[2] + tabela_confusao[3])/sum(tabela_confusao)
taxa_de_erros2

taxa_acerto2 - taxa_acerto

