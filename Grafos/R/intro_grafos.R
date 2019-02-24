install.packages('igraph')
library(igraph)

grafo1 = graph(edges = c(1,2,2,3,3,4,4,1)) 
plot(grafo1)
grafo2_bidirecional = graph(edges = c(1,2,2,3,3,4,4,1,1,4,4,3,3,2,2,1)) 
plot(grafo2_bidirecional)

grafo3 = graph_from_literal(1-+2,2-+3,3++4,4-+1)#Cria uma aresta em direcao do -+ vertice
#++ bidirecional
plot(grafo3)

#Grafo nao direcionado
grafo4 = graph_from_literal(1-2,2-3,3-4,4-1,5)
plot(grafo4)

grafo5 = graph(edges=c(1,2,3,3,3,4,4,1), directed=F)
plot(grafo5)

grafo6 = graph(edges=c(1,2,2,3,3,4,4,1), directed=F,n=10)
plot(grafo6)

grafo7 = graph(edges=c('A','B','B','C','C','D','D','E','E','E','A','A','C','C','B'),isolates=c('F','G'))
plot(grafo7)

grafo7[] #matriz adgjacente
grafo7[1,]
grafo7[,1]
V(grafo7)$name
grafo8 = graph(edges =c('Fernando','Pedro','Jose','Antonio','Fernando','Jose','Fernando','Antonio'))
plot(grafo8)
V(grafo8)$Peso = c(20,34,55,60)
plot(grafo8)
vertex_attr(grafo8)

E(grafo8)$TipoAmizade = c('Amigo','Irmao','Inimigo','Inimigo')
plot(grafo8)
edge_attr(grafo8)
vertex_attr(grafo8)$Peso
E(grafo8)$weight = c(1,2,1,3) 
grafo8
V(grafo8)$type = 'Humanos' #definindo tipo do grafo

#===========#
#IMPRESSOES #
#===========#
vertex_attr(grafo8)$Peso
plot(grafo8,vertex.size =vertex_attr(grafo8)$Peso)
edge_attr(grafo8)$weight
#Imprimindo pesos dos vertices
plot(grafo8, vertex.size = vertex_attr(grafo8)$Peso, edge.width= vertex_attr(grafo8)$weight)
vertex_attr(grafo8)$Cor = c('Blue','Red','Yellow','Green')
plot(grafo8, vertex.size = vertex_attr(grafo8)$Peso, edge.width= vertex_attr(grafo8)$weight,
     vertex.color = vertex_attr(grafo8)$Cor,
     edge.curved=0.4, frame=T, main='Grafo')

plot(grafo8, vertex.size = vertex_attr(grafo8)$Peso, edge.width= vertex_attr(grafo8)$weight,
     vertex.color = vertex_attr(grafo8)$Cor,
     edge.curved=0.4, frame=T, main='Grafo', vertex.shape = 'square')
tkplot(grafo7)

grafo10 = graph(edges = (c(2,1,2,3,3,2,2,4,4,2,1,4,4,1,3,1)))
plot(grafo10)
get.adjedgelist(grafo10,mode=c('all'))