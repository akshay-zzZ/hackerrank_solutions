s = input()
import itertools
s = ''.join(ch for ch,k in itertools.groupby(s))
print(s)