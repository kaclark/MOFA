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
rownames(rna_data) <- replace(rownames(rna_data), match(names(symb), rownames(rna_data), symb))

counts <- CreateSeuratObject(counts = rna_data, project = 'mRNA', min.cells = 3, min.features = 200)
#saveRDS(counts, 'data/rna/rna_sobj.rds')
counts[["percent.mt"]] <- PercentageFeatureSet(counts, pattern = "^mt-")
counts <- subset(percent.mt < 5)
counts <- NormalizeData(counts, normalization.method = "LogNormalize", scale.factor = 10000)
norm_data <- GetAssayData(counts)
gini <- apply(x <- norm_data, 1, function(x) ineq(x, type="Gini"))
#saveRDS(counts, 'data/rna/normalized_rna_data.rds')
mean_data <- read.csv('./data/rna/pagoda_mean_expression_sorted.csv', row.names=1, header=TRUE, sep=',')
rownames(mean_data) <- replace(rownames(mean_data), match(names(symb), rownames(mean_data)), symb)
sym_del_list <- setdiff(names(gini), rownames(mean_data))
gini_cor_mean <- lapply(x <- match(rownames(mean_data), names(gini)), function(x) gini[x])

png(file = "Gini_mean_expression.png")
plot(x=unlist(mean_data),y=unlist(gini_cor_mean),xlab="Mean Gene Expression",ylab="Gini Coefficent", main="Mean Gene Expression vs Gini Coefficent")
dev.off()

png(file = "Gini_mean_expression_log10.png")
plot(x=log10(unlist(mean_data)),y=unlist(gini_cor_mean),xlab="Mean Gene Expression log10",ylab="Gini Coefficent", main="Mean Gene Expression vs Gini Coefficent")
dev.off()
