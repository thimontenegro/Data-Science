#install.packages('h2o')
library(h2o)
h2o.init()

#Treino
treino = h2o.importFile(file.choose())

#Teste
teste = h2o.importFile(file.choose())
dim(treino)
dim(teste)
#Transformando treino e teste de classes em fatores
treino[,785] = as.factor(treino[,785]) 
teste[,785] = as.factor(teste[,785])

#Formalizando o modelo de Deep Learning
modelo = h2o.deeplearning(x=colnames(treino[,1:784]),y='C785',training_frame = treino, validation_frame = teste,distribution='AUTO',activation='RectifierWithDropout',
                          hidden=c(64,64,64), sparse =TRUE, epochs = 20)
plot(modelo)
h2o.performance(modelo)

treino[20,785]
predicao = h2o.predict(modelo,newdata=treino[20,1:784])
predicao
predicao$predict