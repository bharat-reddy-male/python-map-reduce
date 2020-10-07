# Case 2 - Reducer using standard input and output
# Easy to test locally with Bash


import sys


thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    paymentType, amount = datalist

    if paymentType != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey + '\t' + str(thisValue)+'\n')

      # start over for each new key
      thisKey = paymentType 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(amount)

# output the final key-summaryvalue result outside the loop
print(thisKey + '\t' + str(thisValue)+'\n')

