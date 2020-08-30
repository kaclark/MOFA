library(biomaRt)
library(EnsDb.Mmusculus.v79)

ensemblgenes <- as.character(unlist(read.delim("./data/rna/ensembl.txt")))

mart <- useDataset("mmusculus_gene_ensembl", useMart("ensembl"))
attributes <- listAttributes(mart) #lets you see all possible attributes


genes <- getBM(filters= "ensembl_gene_id", 
                attributes= c("ensembl_gene_id","external_gene_name"),
                values=ensemblgenes, mart= mart)

dupgenes <- genes$external_gene_name[duplicated(genes$external_gene_name)]

genes <- genes[!duplicated(genes$external_gene_name), ]
