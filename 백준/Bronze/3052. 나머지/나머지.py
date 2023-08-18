remain = []
diff = []

for i in range(10):
    n = int(input())
    remain.append(n%42)
    
print(len(set(remain)))     # set -> 중복 제거