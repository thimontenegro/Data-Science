install.packages('e101071',dependecies = T)
library(e1017)
credito = read.csv(file.choose(), sep=',',header=T)
head(credito)

dim(credito) #1000 instancias e 21 colunas
#gerar array de 1-2, de forma de 70% de treino e 30% teste
amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))
#separr conjunto de teste e de treino
credito_Treino = credito[amostra==1,]
credito_Teste = credito[amostra==2,]
dim(credito_Treino) #tamanho de credito treino

dim(credito_Teste) #tamanho do credito de teste

#===================#
#Criacao do Modelo
#===================#
modelo = naiveBayes(class ~ . , credito_Treino) #1 paramentro = treinar modelo, 2 parametro dados
# ponto = seletor universal
#modelo para criar previsoes
#vetor que vai conter bom e mal pagador
predicao = predict(modelo, credito_Teste) #passar o modelo e dados que contem os atributos p/ predicao com mesma estrutura 
#predicao em dados novos que o modelo nao conhecia


#Avaliar modelo

#criando tabela de confusao
tabela_confusao = table(credito_Teste$class, predicao)
tabela_confusao

#indice de acertos
taxa_acertos = (tabela_confusao[1] + tabela_confusao[4])/sum(tabela_confusao)
#pegando os acertos dividindo pelo total da tabela
#taxa_acertos # 76.45%

taxa_erros = (tabela_confusao[2] + tabela_confusao[3])/sum(tabela_confusao)
taxa_erros


#===================#
# Simulando o modelo 
#===================#

novo_credito = read.csv(file.choose(),sep=',', header = T)
novo_credito #tem que ter todas as caracteristicas do modelo!
dim(novo_credito) # n tem o modelo class!
novo_cliente = predict(modelo,novo_credito)
novo_cliente
