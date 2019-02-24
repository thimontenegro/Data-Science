trees
hist(trees$Height, main= 'Árvores', ylab = 'Frequencia', xlab ='Altura',col = 'purple')#ylab nome no eixo y
#xlab nome do eixo x
hist(trees$Height, main= 'Árvores', ylab = 'Frequencia', xlab ='Altura',col = 'purple',
     density = 20, breaks = 20)#ylab nome no eixo y
#breaks dividide o histograma no numero desejado
#================Densidade ================#
densidade = density(trees$Height)
densidade
plot(densidade)

hist(trees$Height,main=NULL,xlab= NULL)
par(new=TRUE)
plot(densidade)

#==============Disperção =====================#
plot(trees$Volume, trees$Girth)

plot(trees$Girth, trees$Volume,main ='Árvores',ylab='Circuferencia',xlab='Volume',col='blue',pch=20,
     type='line')
plot(jitter(trees$Girth), trees$Volume,main ='Árvores',ylab='Circuferencia',xlab='Volume',col='blue',pch=20)


#=====Dispercao com legendas===================#
CO2
plot(CO2$conc,CO2$uptake,pch=20,col=CO2$Treatment)
legend('bottomright',legend=c('nonchille','chilled'),cex=1,fill=c('black','red'))#1 - Argumento da posicao, 2-nomes

#====DIvidindo telas====#
#Variaveis diferentes de um mesmo conjunto!
plot(trees)

split.screen(figs=c(2,2))#Dividindo a tela

screen(1) #No setor 1
plot(trees$Girth,trees$Volume,ylab='Volume',xlab='Circuferencia')

screen(2)
plot(trees$Girth,trees$Height,ylab='Circuferencia',xlab='Altura')

screen(3)
plot(trees$Height,trees$Volume,ylab='Volume',xlab='Altura')

screen(4)
hist(trees$Volume)
close.screen(all=T) #Fecha as telas, desabilita telas
#==============BOX PLOT =================#
#CMPARAR DISTRIBUICAO DE VARIAS VARIAVEIS!
boxplot(trees$Volume,main='Árvores',xlab='Volume',col='purple',notch = T)#notch para efeito grafico
boxplot.stats(trees$Height)

#==========Gráficos E Pizzas ============#
Insect$prays
spray = aggregate( . ~ spray, data=InsectSprays, sum)#Funcao de agreggacao
spray
#Gráfico em barras
barplot(spray$count,col=gray.colors(6),xlab='Spray', ylab='Total', names.arg=spray$spray)
box()


#Pizza
pie(spray$count,labels=spray$spray,main='Spray',col=c(1:6))#1- variavel continua
pie(spray$count,labels=NA,main='Spray',col=c(1:6))
legend('bottomright',legend=spray$spray,cex=1,fill=c(1:6))#posicao