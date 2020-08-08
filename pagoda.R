require(scde)
#load rna raw count data
rna_data = read.csv('./data/rna/qc_counts.txt', row.names=1, header=TRUE, sep='\t')
cd <- clean.counts(rna_data)
#clean data/filter data
knn <- knn.error.models(cd, k = ncol(cd)/12, n.cores = detectCores(), min.count.threshold = 10, min.nonfailed = 10, max.model.plots = 10)
varinfo <- pagoda.varnorm(knn, counts = cd, trim = 10/ncol(cd), max.adj.var = 5, n.cores = detectCores(), plot = TRUE)
sort(varinfo$arv, decreasing = TRUE)[1:10]
write.table(varinfo, file = "./data/rna/pagoda_results.txt", row.names=TRUE, col.names=TRUE, sep="\t", quote = FALSE)
