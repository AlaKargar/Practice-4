s = int(input("Please enter your seconds: "))

min = (s % 3600)//60
h = (s // 3600)
sec = (s % 3600) % 60
print(h, ":", min, ":", sec)
