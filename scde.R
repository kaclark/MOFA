require(scde)
rna_data = read.table('./data/rna/qc_counts.txt', sep='\t')
rna_data<-apply(rna_data,2,function(x) {storage.mode(x) <- 'integer'; x})
err <- scde.error.models(counts = rna_data, n.cores = 1, min.size.entries = 2000, threshold.segmentation = TRUE, save.crossfit.plots = FALSE, save.model.plots = FALSE, verbose = 1)
valid.cells <- err$corr.a > 0
err <- err[valid.cells,]
o.prior <- scde.expression.prior(models = err, counts = data, length.out = 400, show.plot = False)
ediff <- scde.expression.difference(err, cd, o.prior, n.randomizations = 100, n.cores = 1, verbose = 1)
head(ediff[order(ediff$Z, decreasing = TRUE), ])
write.table(ediff[order(abs(ediff$Z), decreasing = TRUE), ], file = "./data/rna/scde_results.txt", row.names=TRUE, col.names=TRUE, sep="\t", quote = FALSE)
