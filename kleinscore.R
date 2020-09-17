
setwd("/Volumes/sharp/sofiahu/E12-182KO/E12-182KO/tables")
wtnorm = read.table("WT2502_WT4085_seurat-normdata.txt", row.names = 1, header = T)

# Klein
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

wtnorm_klein = runKlein(wtnorm, 0.25)
