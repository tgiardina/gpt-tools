# Given a roman numeral, converts it to an integer. This script has one input, which is the roman numeral.
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            integer += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            integer += roman[s[i]]
    return integer

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(roman_to_int(sys.argv[1]))
    else:
        print("No Roman numeral provided for conversion.")