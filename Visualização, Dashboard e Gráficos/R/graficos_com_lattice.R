library(lattice)
#=========BOX PLOT ============#
bwplot(trees$Volume,main = 'Árvores',xlab='Volume')

#======Histograma =============#
histogram(trees$Volume, main = 'Árvores',xlab='Volume',aspect=0.5,type='count',nint = 10)
chickwts
aggregate(chickwts$weight,by=list(chickwts$feed),FUN=sum)

histogram(~ weight | feed, data = chickwts)

#GRAFOS DE DENSIDADE
densityplot(CO2$conc)
densityplot(~ CO2$conc | CO2$Treatment, plot.points = F)

#==========DISPERÇÃO==========#
xyplot(CO2$conc ~ CO2$uptake)
xyplot(CO2$conc ~ CO2$uptake | CO2$Type)
xyplot(CO2$conc ~ CO2$uptake | CO2$Treatment)

dotplot(esoph$alcgp ~ esoph$ncontrols, data=esoph)

dotplot(esoph$alcgp ~ esoph$ncontrols | esoph$tobgp, data=esoph)

#==============GRÁFICO 3D =========#
cloud(decrease ~ rowpos * colpos,groups=treatment, data = OrchardSprays)