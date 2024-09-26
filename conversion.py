#def conversion_number_systeam();
print("number systeam converstion")
print("1.decimal to binary")
print("2.binary to decimal")
print("3.decimal to hexadecimal")
print("4.hexadecimal to decimal")
print("5.decmial to octal")
print("6.octal to decimal")

choice = int(input("enter your choice(1-6):"))
if choice==1:
    decimal = int(input("enter decimal number :"))
    binary = bin(decimal).replace("0b", "")
    print(f"binary representation:{binary} ")

elif choice==2:
    binary = input("enter binary number:")
    decimal = int(binary,2)
    print(f"decimal represention: {decimal}")

elif choice==3:
    decimal = int(input("enter decimal number:"))
    hexadecimal = hex(decimal).replace("0x","").upper()
    print(f"hexadecimal represention :{hexadecimal}")

elif choice==4:
     hexadecimal = input("enter hexadecimal number :")
     decimal = int(hexadecimal,16)
     print(f"decimal representation :{decimal}")

elif choice==5:
    decimal = int(input("enter decimal number:"))
    octal = oct(decimal) .replace("o0", "")
    print(f"octal represenation :{octal}")

       
elif choice==6:
    octal = input("enter octal number ")
    decimal = int(octal,8)
    print(f"decimal representation :{decimal}")

else:
    print("invalid choice")        
    
