dist = graph(edges = c('A','C','A','B','B','E','B','F','C','D','G','H','D','H','E','H',
                       'F','G'), directed = T)
#Pesos Dist
E(dist)$weight = c(2,1,2,1,2,1,1,3,1)
#imprimindo grafo e peso
plot(dist,edge.label=E(dist)$weight)

distances(dist,V(dist)$name == 'A',V(dist)$name =='H')

caminho = shortest_paths(dist,V(dist)$name == 'A', V(dist)$name == 'H',output = c('both'))
#lista de caminhos com vertices e arestas de A -> H
caminho$vpath

for(i in 1:length(V(dist))){
  V(dist)$color[i] <-ifelse(i %in% as.vector(unlist(caminho$vpath)),'green','gray')
}
for(i in 1:length(E(dist))){
  E(dist)$color[i] <-ifelse(i %in% as.vector(unlist(caminho$epath)),
                            'green','gray')
}
plot(dist,edge.label=E(dist)$weight)

comunidades = cluster_edge_betweenness(dist)
comunidades$membership
plot(dist,vertex.color=comunidades$membership,edge.color = 'red')
