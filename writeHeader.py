LINE_LENGTH = 39

header = input('Header: ')

filler = LINE_LENGTH - len(header) - 4
left = filler // 2
right = left + (1 if filler % 2 else 0)

print('#', '-'*left, header, '-'*right)