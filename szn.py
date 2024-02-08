x = "i Go to school By bus.she Go to school by bycicle.he go to school by train.she Go to school by train."


ans2 = [i.capitalize() + "." for i in x.split(".") if i]

print(ans2)