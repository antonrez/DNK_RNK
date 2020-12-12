"""
Нужно написать функцию, которая получает цепь ДНК а возвращает ее РНК-комплемент (РНК транскрипцию).
И ДНК, и РНК представляют собой последовательность нуклеотидов.
Четыре нуклеотида, обнаруженные в ДНК, - это аденин (A), цитозин (C), гуанин (G) и тимин (T).
Четыре нуклеотида, обнаруженные в РНК, - это аденин (A), цитозин (C), гуанин (G) и урацил (U).
Учитывая цепь ДНК, ее транскрибируемая цепь РНК образуется путем замены каждого нуклеотида его комплементом:
G -> C
C -> G
T -> A
A -> U

Пример преобразований
G -> C
C -> G
T -> A
A -> U
ACGTGGTCTTAA -> UGCACCAGAAUU
"""


def rnk(dnk):
    dnk_list = {'G': "C", 'C': "G", 'T': "A", 'A': "U"}
    rnk_list = ""
    for s in dnk:
        rnk_list += dnk_list.setdefault(s, "_")
    return rnk_list


def rnk_str(dnk):
    rnk_if = ""
    for s in dnk:
        if s == "G":
            rnk_if += "C"
        elif s == "C":
            rnk_if += "G"
        elif s == "T":
            rnk_if += "A"
        elif s == "A":
            rnk_if += "U"
        else:
            rnk_if += "_"
    return rnk_if


print(rnk("ACGTGGTCTTAA"))
print(rnk_str("ACGTGGTCTTAA"))
