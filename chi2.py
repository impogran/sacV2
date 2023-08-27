import matplotlib.pyplot as plt

OBJ = list()
total = 0
pairs = dict()
with open("dane.txt", "r") as f:
    for row in f:
        row = row.strip()
        number = int(row.split(":")[0])
        times = int(row.split(":")[1])
        total += int(times)
        pairs[number] = times

sumT = 0
keys = list(pairs.keys())
values = list(pairs.values())
for key in pairs:
    for i in range(0, pairs[key]):
        OBJ.append(key)
    val = pairs[key] / total * 100
    sumT += val
    print(str(key) + ": " + "%.4f" % (val) + "% " + str(pairs[key]))

fig = plt.figure(figsize=(10, 65))

# creating the bar plot
plt.bar(keys, values)

# plt.xlabel("No. of changed bits")
# plt.ylabel("No. of ciphers")
# plt.title("Ciphers with changed bits (TinyJambu)")
plt.xlabel("No. of outputs")
plt.ylabel("No. of rank")
plt.show()

avg = sum(OBJ) / len(OBJ)
E = 32

power = (avg - E) ** 2
chi2 = power / E

print("Wartość chi kwadrat wynosi: " + "%.4f" % chi2)
