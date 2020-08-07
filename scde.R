require(scde)
#load rna raw count data
rna_data = read.csv('./data/rna/qc_counts.txt', row.names=1, header=TRUE, sep='\t')
#clean data/filter data
rna_data <- clean.counts(rna_data, min.lib.size=1000, min.reads = 1, min.detected=1)
#generate error model
err <- scde.error.models(counts = rna_data, n.cores = 4, threshold.segmentation = TRUE, save.crossfit.plots = FALSE, save.model.plots = FALSE, verbose = 1)
#filter poor fits
valid.cells <- err$corr.a > 0
err <- err[valid.cells,]
o.prior <- scde.expression.prior(models = err, counts = rna_data, length.out = 400, show.plot = False)
#get differential data
ediff <- scde.expression.difference(err, rna_data, o.prior, n.randomizations = 100, n.cores = 4, verbose = 1)
head(ediff[order(ediff$Z, decreasing = TRUE), ])
#export data
write.table(ediff[order(abs(ediff$Z), decreasing = TRUE), ], file = "./data/rna/scde_results.txt", row.names=TRUE, col.names=TRUE, sep="\t", quote = FALSE)
