#Write a function that determines the class of an IPv4 address (A, B, C, D, E).

# my way to remember the classes ranges numbers 
#01111111
print(int(0b00000000)  ,int(0b01111111) ) #  0 127
#10111111
print(int(0b10000000) , int(0b10111111) ) # 128 191
#110111111
print(int(0b11000000) , int(0b11011111) ) # 192 223
#11101111
print(int(0b11100000) , int(0b11101111) ) # 192 223

def determine_class(ip:str):
    first_part = list(map(int , ip.split(".")))[0]
    if 1<=first_part>=126:
        print("class A")
    elif 128 <= first_part <= 191:
        print("class B")
    elif 192 <= first_part <= 223:
        print("class C")
    else:
        print("class D")




