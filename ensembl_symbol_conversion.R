require(httr)
require(jsonlite)

url = "https://biotools.fr/mouse/ensembl_symbol_converter/"
raw <- scan("./data/rna/ensembl.txt", character())
print(raw)
ids_json <- toJSON(raw)
print("Ids loaded")
body <- list(api=1, ids=ids_json)
r <- POST(url, body = body)

output = fromJSON( content(r, "text"), flatten=TRUE)
df <- as.data.frame(output)
print(df)
write.table(df,file="./data/rna/symbols.txt",row.names=TRUE)
