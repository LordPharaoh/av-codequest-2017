with open("Prob05.in.txt") as f:
    arr = f.readlines()
    f.close()
cases = int(arr[0])
for i in range(1, cases + 1):
    amt = float(arr[i].strip("$"))
    print(amt)
    with open("Prob05.out.txt", 'a+') as w:
        w.write("Total of the bill: $%.2f" % amt + '\n')
        w.write("15%% = $%.2f" % (amt * .15) + '\n')
        w.write("18%% = $%.2f" % (amt * .18) + '\n')
        w.write("20%% = $%.2f" % (amt * .2) + '\n')
        w.close()

