def divisible_without_rest(x, y):
    result = x / y
    return result.is_integer()


def nearest_higher_even_number(x):
    new_number = x + 1
    if (new_number % 2) == 0:
        return new_number
    else:
        new_number += 1
        return new_number


def is_bigger(x, y):
    if x < y:
        return f"{x} is smaller than {y}"
    elif x == y:
        return f"{x} is equal to {y}"
    else:
        return f"{x} is bigger than {y}"


def celsius_to_fahrenheit(x):
    return x * 1.8 + 32


def fahrenheit_to_celsius(x):
    return (x - 32) * 5 / 9


def one_bits_in_number(hex):
    return bin(int(hex, base=16)).count("1")


def zero_bits_in_number(hex):
    return bin(int(hex, base=16))[2::].count("0")


def zinses_zins(base_amount, rate_in_percent, years):
    return base_amount * ((rate_in_percent / 100) + 1) ** years


def ascii_value(s):
    return f"The ASCII value of {s[0]} is {ord(s[0])}"


def n_nn_nnn(n):
    return int(f"{n}{n}{n}") + int(f"{n}{n}") + n


def capitalize_first(s):
    return s[0].capitalize() + s[1::]


def repeat_string(s, max):
    max_new = ""
    while len(max_new) < max:
        max_new += s
        print(max_new[:max:])
    return max_new[:max:]


def find_first_occurrence(haystack, needle):
    result = haystack.find(needle)
    if result == -1:
        return False
    else:
        return result


def lower_case_and_remove_vowels(s):
    new_string = s.lower()
    for vowel in ["a", "e", "i", "o", "u"]:
        new_string = new_string.replace(vowel, "")
    return new_string


def palindrome(s):
    s_low = s.lower()
    s_low_no_w = s_low.replace(" ", "")
    return s_low_no_w == s_low_no_w[::-1]


def energie_preis_deckel(previous_year_kwh, this_year_kwh, price_per_kwh):
    previous_year_kwh/100*80 * 0.4


def main():
    # Note: This is only for student-side debugging
    assert (energie_preis_deckel(10000, 8000, 0.60) == 3200.0)


if __name__ == '__main__':
   main()
