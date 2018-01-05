library(bnlearn)
library(parallel)

source("./scripts/dedupe.R")

data = read.table("./results/prediction.small.txt", header = TRUE, sep="\t", row.names=1, check.names=F)
blacklist = read.table("./results/blacklist.small.txt", header=T, sep="\t")

cl = makeCluster(8, type = "SOCK")
dag = si.hiton.pc(data, cluster = cl, blacklist = blacklist)
amat.data = amat(dag)
plot(dag)
write.table(amat.data, "./results/dag.small.txt", sep="\t")
