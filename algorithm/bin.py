dva = "1101"
diset  = 0
stepan  = 0
for i in  dva[::-1]:
    diset += int(i) * (2 ** stepan)
    stepan += 1
print(diset)
