"""
Disemvowel Trolls
"""
def disemvowel_trolls(sentence: str) -> str:
  return ''.join(c for c in sentence if c.lower() not in 'euioa')

if __name__ == "__main__":
    print(disemvowel_trolls("Delete all vowels!"))
    print(disemvowel_trolls("123@#$&+&()%©®™✓[]aety"))
    assert disemvowel_trolls("Delete all vowels!") == "Dlt ll vwls!"
    assert disemvowel_trolls("QWERTY") == "QWRTY"
