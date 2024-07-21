import re

def generator_numbers(text: str):
    # find numbers in text
    all_numbers = re.findall(r'\d+\.\d+', text)
    # generator that yeild next value
    for item in all_numbers:
        yield item

def sum_profit(text: str, function: callable):
    summa = 0
    generator = function(text)

    # loop with addition next value 
    while True:
        try:
            value = next(generator)
            print(value)
            summa += float(value)
        except StopIteration:
            break

    return summa

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
