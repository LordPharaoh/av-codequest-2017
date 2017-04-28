
with open("Prob02.in.txt") as f:
    arr = f.readlines()
    f.close()
i = int(arr[0])
vals = [.25, .10, .05, .01]
for i in range(1, i+1):
    amounts = [0, 0, 0, 0]
    amt = float(arr[i].strip("$"))
    total = 0
    for j in range(0, 4):
        while total + vals[j] <= amt:
            total+=vals[j]
            amounts[j]+=1
    with open("Prob02.out.txt", 'a') as w:
        w.write("$%.2f" % total +'\n')
        w.write("Quarters=" + str(amounts[0]) + '\n')
        w.write("Dimes=" + str(amounts[1])+ '\n')
        w.write("Nickels=" + str(amounts[2])+ '\n')
        w.write("Pennies=" + str(amounts[3])+ '\n')
        w.close()






