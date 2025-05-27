import matplotlib.pyplot as plt
import re

text = """
Ти вже зробив домашнє завдання? Це дуже важливо. Не забудь здати його вчасно! 
А ще... Я хотів сказати щось цікаве. Чи це справді має значення? Подивись уважно!
"""

# Розділяємо текст на речення
sentences = re.findall(r'[^.!?…]+[.!?…]+', text)

# Лічильники
normal = 0         # звичайні (.)
question = 0       # питальні (?)
exclamatory = 0    # окличні (!)
ellipsis = 0       # на ... або … (три крапки/один символ)

for sentence in sentences:
    sentence = sentence.strip()
    if sentence.endswith('?'):
        question += 1
    elif sentence.endswith('!'):
        exclamatory += 1
    elif sentence.endswith('...') or sentence.endswith('…'):
        ellipsis += 1
    elif sentence.endswith('.'):
        normal += 1

# Підготовка даних для графіка
labels = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
counts = [normal, question, exclamatory, ellipsis]

# Побудова гістограми
plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color=['royalblue', 'crimson', 'gold', 'mediumseagreen'])
plt.title('Частота типів речень у тексті')
plt.ylabel('Кількість речень')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Збереження у PNG-файл
plt.savefig('images/sentence_histogram.png', dpi=300)
plt.show()
