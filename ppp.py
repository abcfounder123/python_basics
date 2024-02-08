

x = "i Go to school By bus.she go to school by bycicle.he go to school by train.she Go to school by train."
l = x.split(".")
print(x)

ans = ""
for i in l:
    if i:
        ans += i.capitalize() + "."

print(ans)
