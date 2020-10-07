# Case 2 - Mapper using standard input and output
# Easy to test locally with Bash



import sys 


# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("    ")
  if (len(datalist) == 6) : 
    date, time,store, department, cost, paymentType = datalist

    # print intermediate key-value pairs to standard output
    print(paymentType + "\t" + cost + "\n")

