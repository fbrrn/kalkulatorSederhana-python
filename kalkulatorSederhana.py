print("Kalkulator sederhana")
 
def tambah (a, b) :
    return a + b
def kurang (a, b) :
    return a - b
def kali (a, b) :
    return a * b
def bagi(a, b) :
    return a / b

while True :
    a = float(input("\nMasukkan bilangan pertama \t:"))      
    b = float(input("Masukkan bilangan kedua \t:"))
    operator = input("Pilih operator (+, -, *, /) \t:")
    
    try :
        if operator == "+" :
            hasil1 = a + b
            print("\n%.2f + %.2f = %.2f" % (a, b, hasil1))
            
        elif operator == "-" :
            hasil2 = a - b
            print("\n%.2f - %.2f = %.2f" % (a, b, hasil2))
            
        elif operator == "*" :
            hasil3 = a * b
            print("\n%.2f * %.2f = %.2f" % (a, b, hasil3))
        
        elif operator == "/" :
            hasil4 = a / b
            print("\n%.2f / %.2f = %.2f" % (a, b, hasil4))
        
        else :
            print("\nOperator tidak dikenali oleh sistem.")
            
    except ZeroDivisionError:
        print("\n%2.f / %2.f = Tak Hingga" % (a, b,))
        
    reset = input("\nApakah Anda akan menghitung lagi? (Ya/Tidak)")
    if reset == "Tidak" :
        print("Terima kasih. Semoga harimu menyenangkan")
        break