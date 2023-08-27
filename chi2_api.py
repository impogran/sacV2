from scipy.stats import chi2_contingency

file = open("data.txt","r")
lines = file.read().split(",")
lines = lines[:-1]
for i in range(len(lines)):
    lines[i] = int(lines[i])
    lines[i] += 1
file.close()

cols = 65 # this is a length of a single range[] element

data = [lines[x+1:x+cols] for x in range(0, len(lines),cols)]
data = data[:-1]
    
# print(data)

# for i in data:
#     print(len(i))

stat,p,dof,expected = chi2_contingency(data)

# print(expected)
print(stat, p, dof)

# alpha = 0.05
print("p-value:", p)