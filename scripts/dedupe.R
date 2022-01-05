library(impute)

dedup = function(data, cutoff) {
  
  i = 1
  total.dropped = 0
  vars = colnames(data)
  to.drop = numeric(0)
  
  available = seq(from = min(i, ncol(data)), to = ncol(data))
  
  next.one = available[1]
  
  repeat {
    
    available = available[!(available %in% to.drop)]
    available = available[-1]
    
    cat("looking at", vars[next.one], "with", length(available), "variables still to check.\n")
    
    correlations = cor(data[, next.one], data[, available], use = "pairwise.complete.obs")
    which.ones = which(abs(correlations) >= cutoff)
    to.drop = c(to.drop, available[which.ones])
    
    for (j in which.ones) {
      
      cat(vars[next.one], "is collinear with", colnames(correlations)[j], "dropping",
          colnames(correlations)[j], "with correlation", correlations[j], "\n")
      
    }#FOR
    
    next.one = (available[!(available %in% to.drop)])[1]
    
    if (length(available[!(available %in% to.drop)]) == 1)
      break
    if (is.na(next.one))
      break
    
  }#REPEAT
  
  return(data[, -to.drop, drop = FALSE])
  
}#DEDUP
