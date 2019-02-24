install.packages('igraphdata')
library(igraphdata)

plot(Koenigsberg)
degree(Koenigsberg,mode='all') #grau impar

data(kite)
plot(kite)
comunidades = cluster_edge_betweenness(kite)

plot(kite,vertex.color=comunidades$membership)
data(UKfaculty)

comun = cluster_edge_betweenness(UKfaculty)
plot(UKfaculty, vertex.color=comun$membership)