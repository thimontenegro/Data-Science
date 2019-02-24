modelo = lm(speed ~ dist, data=cars)

> colnames(mtcars)
[1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear" "carb"
> dim(mtcars)
[1] 32 11
> cor(mtcars[1:4])
> modelo = lm(mpg ~ disp, data=mtcars)
> modelo

> summary(modelo)$r.squared
[1] 0.7678877
> summary(modelo)$adj.r.squared
[1] 0.7430186
> predict(modelo, data.frame(disp=200, hp=100, cyl=4))
1 
24.03969 

> eleicao = read.csv(file.choose(),sep=';',header = T)
> View(eleicao)
> fix(eleicao)
> plot(eleicao$DESPESAS, eleicao$SITUACAO)
> summary(eleicao)

> cor(eleicao$DESPESAS,eleicao$SITUACAO)
[1] 0.8121872
> modelo = glm
> modelo = glm(SITUACAO ~ DESPESAS, data = eleicao,family ='binomial')
> summary(modelo)