## original code from code.py
# #def function1(a):
#    b = dict()
#    for c in a:
#        if c not in b:
#            b[c] = 1
#        else:
#            b[c] += 1
#    return b

#def function2(a):
#    print('freqs')
#    total = float(sum([a[b] for b in a.keys()]))
#    for b in a.keys():
#        print(b + ':' + str(a[b]/total))

#function2(function1('ATCTGACGCGCGCCGC'))

## codes from chatgpt
from collections import Counter

def function1(a):
    return Counter(a)

def function2(a):
    print('Frequencies:')
    total = sum(a.values())  # No need for float conversion as we're doing division
    for b, count in a.items():
        print(f"{b}: {count/total:.2%}")

function2(function1('ATCTGACGCGCGCCGC'))
