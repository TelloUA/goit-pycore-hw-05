import re


def generator_numbers(text: str):
    """
    Finds numbers in text and returns them as a generator.

    :param text: string with numbers
    :return: generator that yield numbers
    """
    all_numbers = re.findall(r'\d+\.\d+', text)
    for item in all_numbers:
        yield item

def sum_profit(text: str, function: callable):
    """
    Calculates the total profit from the text using the given function.

    :param text: string to analyze
    :param function: function that generates numbers from text
    :return: total profit
    """
    summa = 0
    generator = function(text)

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
