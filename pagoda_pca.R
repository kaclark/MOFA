require(scde)
cd <- readRDS('./data/rna/cd.rds')
knn <- readRDS('./data/rna/knn.rds')
varinfo <- readRDS('./data/rna/pagoda_results.rds')
env <- readRDS('./data/rna/env_cc.rds')
pwpca <- pagoda.pathway.wPCA(varinfo, env, n.components = 1, n.cores = 8)
df <- pagoda.top.aspects(pwpca, return.table = TRUE, plot=TRUE, z.score=1.96)
saveRDS(df, 'pca.rds')
