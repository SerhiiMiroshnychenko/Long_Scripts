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


