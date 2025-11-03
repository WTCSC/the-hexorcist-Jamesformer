def to_decimal(number_string, original_base):
    total_value = 0
    power = 0
    for char in number_string:
        number_string[::-1]
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_upper = char.upper()
        int(char_upper)
        char_value = digits[char_upper]
        total_value += (char_value * (original_base ** power))
        power += 1
        return total_value
    
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    result_string = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number / target_base
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
        decimal_number / target_base
        char_to_also_add = digits[decimal_number]
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