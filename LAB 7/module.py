import matplotlib.pyplot as plt
from collections import Counter

text = """
Це приклад тексту, у якому потрібно порахувати, як часто зустрічаються ті чи інші літери.
"""

text = text.lower()
ukrainian_letters = 'абвгґдеєжзииіїйклмнопрстуфхцчшщьюя'
letters = [ch for ch in text if ch in ukrainian_letters]
counter = Counter(letters)

sorted_letters = sorted(counter)
frequencies = [counter[char] for char in sorted_letters]

plt.figure(figsize=(10, 5))
plt.bar(sorted_letters, frequencies, color='teal')
plt.title('Частота появи літер у тексті')
plt.xlabel('Літера')
plt.ylabel('Кількість')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.savefig('images/histogram.png', dpi=300)
plt.show()
