# Asssembler code

# READ
A = x7fff
D = *A

# ACTION
A = 0b100000000
D = D&A
A = 10
D; JGT
A = 0b100
D = A
A = 12
JMP
A = 0b1000
D = A

# MOVE USING MASK ON D
A = x7fff
D = D | *A
*A = D

# JMP TO READ AFTER DONE MOVING
A = 0b10000000000
D = A
A = x7fff
D = D & *A
A = 15
D; JGT
A = 0b1000000000
D = A
A = x7fff
D = D & *A
A = 21
D; JGT
A = 0
JMP