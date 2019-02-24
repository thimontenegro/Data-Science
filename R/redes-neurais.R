#install.packages('neuralnet')
#library(neuralnet)
#1 - copia do dataset
myiris = iris


#Binarizando colunas

myiris = cbind(myiris,myiris$Species=='setosa')
myiris = cbind(myiris,myiris$Species=='versicolor')
myiris = cbind(myiris,myiris$Species=='virginica')


#Dando nome as colunas de acordo com a classe
names(myiris)[6] = 'setosa'
names(myiris)[7] = 'versicolor'
names(myiris)[8] = 'virginica'

#Dividir o conjunto de dados em teste e treino
#criando modelo

amostra = sample(2,150,replace=T,prob=c(0.7,0.3))
#Treino Rede Neural
myiristreino = myiris[amostra==1,]
myiristeste = myiris[amostra==2,]
dim(myiristreino)
dim(myiristeste)

#Criando modelo
modelo = neuralnet(setosa + versicolor + virginica ~ Sepal.Length +
                     Sepal.Width + Petal.Length + Petal.Width, myiristreino, hidden=c(5,4))
 #1 - formla, 2 - variavel de dependencias, 3-conjunto treino, 5- camada de neuronios
plot(modelo)

teste = compute(modelo,myiristeste[,1:4]) #passar as colunas de treino
teste$net.result
#Dando nomes nas variaveis
resultado = as.data.frame(teste$net.result)
names(resultado)[1] = 'setosa'
names(resultado)[2] = 'versicolor'
names(resultado)[3] = 'virginica'
head(resultado)
#Adicionando o nome da classe p/ ver resolucao
resultado$class = colnames(resultado[,1:3])[max.col(resultado[,1:3],ties.method='first')]
#tabela de matrix de confusao
confusao = table(resultado$class,myiristeste$Species)
sum(diag(confusao) * 100 / sum(confusao))
confusao