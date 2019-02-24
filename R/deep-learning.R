digitos = read.csv(gzfile(file.choose()), header=F)
dim(digitos)
head(digitos)
#Visualizando digitos
#Dividindo a tela em 4 areas
split.screen(figs=c(2,2))
#Gerando uma matriz 28x28
#transpondo matriz
dig = t(matrix(unlist(digitos[20,-785]),nrow=28,byrow = F)) #pegando o elemetno na coluna 20
dig = t(apply(dig,2,rev))
screen(1)
image(dig, col=grey.colors(255))
digitos[20,785]

#Impressao de 2 uma segudna imagem
screen(2)
dig = t(matrix(unlist(digitos[2,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig, col=grey.colors(255))

#Tela 3
screen(3)
dig = t(matrix(unlist(digitos[18,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev)) #revertendo matrix
image(dig,col=grey.colors(255))

#tela 4
screen(4)
dig=t(matrix(unlist(digitos[55,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig,col=grey.colors(255))
close.screen(all=T)