def cal(a, b):
    return (a + (b/2))*10
    

name = input("Enter your name: ")
a, b = map(float, input("Enter values for a and b separated by a space: ").split())

result = f"{cal(a, b):,.2f}"
a_hex, b_hex = hex(int(a)).upper(), hex(int(b)).upper()

print(f'My name is: "{name}" B = {b:.2f} C = {a:.0f} \nResult: {result} from Hex (\'{a_hex}\', \'{b_hex}\')')
