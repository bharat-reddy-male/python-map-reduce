

# open returns a file object
with open("payment-type.txt", "r") as input:
  with open("bonus-mapper-output.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("    ")
      if (len(datalist) == 2) : 
        amount, paymentType = datalist

        # output intermediate key-value pairs
        output.write(paymentType + "\t" + amount + "\n")

        # display to console (not required - just for the user)
        print(paymentType + "\t" + amount + "\n")

