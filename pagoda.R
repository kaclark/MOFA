require(scde)
#load rna raw count data
rna_data = read.csv('./data/rna/qc_counts.txt', row.names=1, header=TRUE, sep='\t')
cd <- clean.counts(rna_data)
#clean data/filter data
saveRDS(cd, './data/rna/cd.rds')
knn <- knn.error.models(cd, k = ncol(cd)/12, n.cores = 8, min.count.threshold = 10, min.nonfailed = 10, max.model.plots = 10)
saveRDS(knn, "./data/rna/knn.rds")
varinfo <- pagoda.varnorm(knn, counts = cd, trim = 10/ncol(cd), max.adj.var = 5, n.cores = 8, plot = TRUE)
sort(varinfo$arv, decreasing = TRUE)[1:10]
varinfo <- pagoda.subtract.aspect(varinfo, colSums(cd[, rownames(knn)]>0))
saveRDS(varinfo, "./data/rna/pagoda_results.rds")

