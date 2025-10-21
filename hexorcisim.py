def to_decimal(number_string, original_base):
    total_value = 0
    power = 0
    for char in number_string:
        number_string[::-1]
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_number_string = number_string.upper()
        char_value = digits.index(upper_number_string)
        total_value += (char_value * (original_base ** power))
        power += 1
        return total_value
    
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    result_string = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
        12 // 16
        char_to_add = digits[12]
        result_string = 'c' + '7'
        return result_string
    


print("welcome to the hexorcist prepared to get a hexorcisim")
user_string = input("What is your number string")
