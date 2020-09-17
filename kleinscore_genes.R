library(dplyr)
library(Seurat)
library(patchwork)
library(biomaRt)
library(EnsDb.Mmusculus.v79)
library(ineq)
ensemblgenes <- as.character(unlist(read.delim("./data/rna/ensembl.txt")))

mart <- useDataset("mmusculus_gene_ensembl", useMart("ensembl"))
attributes <- listAttributes(mart)

genes <- getBM(filters="ensembl_gene_id", attributes= c("ensembl_gene_id", "external_gene_name"), values=ensemblgenes, mart=mart)

dupgenes <- genes$external_gene_name[duplicated(genes$external_gene_name)]
genes <- genes[!duplicated(genes$external_gene_name), ]
symb <- genes$external_gene_name
ensembl <- genes$ensembl_gene_id
names(symb) <- ensembl

#load rna raw count data
rna_data = read.csv('./data/rna/qc_counts.txt', row.names=1, header=TRUE, sep='\t')
#reomve genes that don't have conversions
del_list <- setdiff(rownames(rna_data), ensembl)
rna_data <- rna_data[-which(rownames(rna_data) %in% del_list),]
#replace ensembl ids with gene symbols
#keeps throwing error
rownames(rna_data) <- replace(rownames(rna_data), match(names(symb), rownames(rna_data), symb))

counts <- CreateSeuratObject(counts = rna_data, project = 'mRNA', min.cells = 1, min.features = 2)
#saveRDS(counts, 'data/rna/rna_sobj.rds')
counts[["percent.mt"]] <- PercentageFeatureSet(counts, pattern = "^mt-")
counts <- subset(percent.mt < 5)
counts <- NormalizeData(counts, normalization.method = "LogNormalize", scale.factor = 10000)
norm_data <- GetAssayData(counts)

runKlein <- function(data, noise){
  pergene.avgread = rowMeans(data)
  percell.totalreads = colSums(data)
  allcell.totalreads = sum(percell.totalreads)
  avgcell.totalreads = colSums(data)
  percell.normalization = avgcell.totalreads / percell.totalreads
  data.normalized = (t(t(data) * percell.normalization))
  
  pergene.countvariance = apply(data.normalized, 1, var)
  pergene.countaverage = rowMeans(data.normalized)
  pergene.COV2 = pergene.countvariance / (pergene.countaverage ^ 2)
  allcell.countvariance = var(percell.totalreads)
  allcell.countaverage = mean(percell.totalreads)
  allcell.COV2 = allcell.countvariance / (allcell.countaverage ^ 2)
  noise2 = noise ^ 2
  
  stats = pergene.COV2 / ((1 + allcell.COV2)*(1 + noise2)/pergene.countaverage + noise2)
  statsdf = data.frame(stats)
  
  statsdf = statsdf[order(-statsdf$stats), , drop = FALSE]
  return(statsdf)
}

wtnorm_klein = runKlein(norm_data, 0.25)
