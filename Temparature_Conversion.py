def get_input():
    temparature = float(input("Enter the temparature(In Celsius):"))
    return temparature

def fahrenhit_converter(temparature):
    res = 1.8 * temparature + 32
    return res

def kelvin_converter(temparature):
    res = temparature + 273
    return res

def celsius_converter(temparature):
    return temparature

def main():
    temparature = get_input()
    print(f"Temparature in Celsius:{celsius_converter(temparature)}")
    print(f"Temparature in Fahrenhit:{fahrenhit_converter(temparature)}")
    print(f"Temparature in Kelvin:{kelvin_converter(temparature)}")

main()
