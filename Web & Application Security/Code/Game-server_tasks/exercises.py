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
    if price_per_kwh < 0.4:
        return this_year_kwh* price_per_kwh    
    else:
        if this_year_kwh > previous_year_kwh * 0.8:
            return previous_year_kwh * 0.8 * 0.4 + (this_year_kwh - previous_year_kwh * 0.8) * price_per_kwh
        else:
            return this_year_kwh * 0.4
        

def list_of_squares(n):
    square_list = []
    [square_list.append(i**2) for i in range(1, n+1)]
    return square_list


def remaining_debt_and_paid_interest(start_amount, interest_rate, monthly_rate, months):
    if months == 0:
        return (start_amount, 0)
    else:
        interest_rate /= 100
        monthly_interest_rate = interest_rate / 12
        debt = start_amount
        total_interest_paid = 0
        for i in range(months):
            interest = debt * monthly_interest_rate
            total_interest_paid += interest
            debt -= monthly_rate - interest
            if debt < 0:
                debt = 0
                break
        if interest > monthly_rate:
            raise ValueError("Impossible to pay off")
        return round(debt, 2), round(total_interest_paid, 2)

def anagram_or_set(string_one, string_two):
    pass


def main():
    pass
    

if __name__ == '__main__':
   main()
