a=input("Teks awal= ")
b=input("Pengganti= ")
for i in "aiueoAIUEO":
    a=a.replace(i,b)
print("Teks akhir=",a)