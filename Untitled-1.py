def fungsi_1():
    for baris in range(7):
        print("*" * 7)

def fungsi_2():
    for baris in range(7):
        if baris >= 1 and baris <= 5:
            print("*" + " " * 5 + "*")
        else:
            print("*" * 7)

def fungsi_3():
    for baris in range(7):
        if baris == 1 or baris == 2 or baris == 4 or baris == 5:
            print("*" + " " * 2 + "*" + " " * 2 + "*")
        else:
            print("*" * 7)

def fungsi_4():
    for baris in range(7):
        if baris == 1 or baris == 2 or baris == 4 or baris == 5:
            print("*" + " " * 5 + "*")
        elif baris == 3:
            print("*" + " " * 2 + "*" + " " * 2 + "*")
        else:
            print("*" * 7)

pilihan = int(input("Pilih fungsi = "))

if pilihan == 1:
    fungsi_1()
elif pilihan == 2:
    fungsi_2()
elif pilihan == 3:
    fungsi_3()
elif pilihan == 4:
    fungsi_4()
else:
    print("Pilihan tidak valid. Pilih antara 1, 2, 3, atau 4.")
