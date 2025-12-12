def to_decimal(number_string, original_base):
    total_value = 0
    power = 0
    for char in number_string:
        reversed_string = number_string[::-1]
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in reversed_string:
            char_upper = char.upper()
        char_value = 0
        for i in range(len(digits)):
            if digits[i] == char_upper:
                char_value = i
        intedorigionalbase = int(original_base)
        total_value += (char_value * (intedorigionalbase ** power))
        power += 1
        return total_value
    
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    result_string = ""
    while decimal_number > 0:
        inteddeciamlnumber = int(decimal_number)
        intedtargetbase = int(target_base)
        remainder = inteddeciamlnumber % intedtargetbase
        decimal_number = inteddeciamlnumber / intedtargetbase
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
        floatoftarget = float(target_base)
        decimal_number / floatoftarget
        inteddeciamlv2 = int(decimal_number)
        char_to_also_add = digits[inteddeciamlv2]
        result_string = char_to_also_add + char_to_add
        return result_string


    


print("welcome to the hexorcist prepared to get a hexorcisim")
user_string = input("What is your number string: ")
original_base = input("what is the original base: ")
target_base = input("what is the base you are trying to get to: ")
print("your hexed number in base-10 is: ")
print(to_decimal(user_string, original_base))
print("the hex you wanted converted is: ")
print(from_decimal(to_decimal(user_string, original_base), target_base))