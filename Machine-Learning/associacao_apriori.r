#install.packages('arules')
library(arules)
transacoes = read.transactions(file.choose(),format = 'basket', sep=',')
transacoes
inspect(transacoes) #visualizar os itens!
image(transacoes)

#REGRAS DE TRANSACAO!
regras = apriori(transacoes,parameter = list(supp=0.5,conf=0.5)) #suporte e confianca
#
inspect(regras) #ver regras geradas
#install.packages("arulesViz") visualizar regras
library(arulesViz)
plot(regras)
plot(regras, method='graph',control=list(type ='items'))

#======USANDO O ECLAT=========#
transacoes = read.transactions(file.choose(), format='basket',sep=',')
image(transacoes)
regras = eclat(transacoes,parameter = list(supp = 0.1, maxlen = 15))#maxlen = num max de iteins
inspect(regras)
plot(regras,method='graph',control=list(type='items'))