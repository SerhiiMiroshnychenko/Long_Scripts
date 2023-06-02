# 1
"""
Disemvowel trolls
Тролі атакують твій розділ коментарів!
Поширений спосіб впоратися з цією ситуацією — видалити всі голосні літери з коментарів тролів, нейтралізуючи загрозу.
Твоє завдання – написати функцію disemvowel_trolls, яка приймає рядок і повертає новий рядок, у якому видалені всі голосні.
Примітка: у цьому завданні літера у не вважається голосною.
Приклади:
disemvowel_trolls("Delete all vowels!") == "Dlt ll vwls!"
disemvowel_trolls("QWERTY") == "QWRTY"
"""

def disemvowel_trolls(sentence: str) -> str:
  return ''.join(c for c in sentence if c.lower() not in 'euioa')

if __name__ == "__main__":
    print(disemvowel_trolls("Delete all vowels!"))
    print(disemvowel_trolls("123@#$&+&()%©®™✓[]aety"))
    assert disemvowel_trolls("Delete all vowels!") == "Dlt ll vwls!"
    assert disemvowel_trolls("QWERTY") == "QWRTY"


# 2
"""
Get order
У твоєму ресторані почали працювати нові касири. Вони вміють приймати замовлення, але не вміють писати слова з великої літери та не вміють користуватися пробілом! Усі створювані ними «замовлення» виглядають приблизно так: "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza" Але вони хочуть отримувати замовлення у вигляді красивого чистого рядка з пробілами та великими літерами, наприклад: "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
Напиши функцію get_order, яка приймає рядок order як аргумент і повертає рядок з більш чітким порядком, з пробілами та великими літерами.
Примітки:
Рядок на виході може містити дублікати, наприклад "Chicken Pizza Pizza"
Персонал кухні очікує, що страви будуть розташовані у тому самому порядку, в якому вони вказані в меню.
Пункти меню досить прості, пункт не може бути частиною іншого пункту:
Burger
Fries
Chicken
Pizza
Sandwich
Onionrings
Milkshake
Coke
Приклад:
get_order("burgersandwich") # повертає "Burger Sandwich"
get_order("cokefriessandwichpizzaburger") # повертає "Burger Fries Pizza Sandwich Coke"
get_order("pizzachickenfriesburgercokemilkshakefriessandwich") # повертає "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
"""

def get_order(order: str) -> str:
  ...


if __name__ == "__main__":
  print(get_order("burgersandwich")) # повертає "Burger Sandwich"
  print(get_order("cokefriessandwichpizzaburger")) # повертає "Burger Fries Pizza Sandwich Coke"
  print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich")) # повертає "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"

