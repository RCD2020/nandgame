# Assember code

# INITIALIZE STARTING ADDRESS
A = x1000
D = A
A = x0001
*A = D

# READ KEY INPUT
A = x6000
D = *A
A = 4
D; JEQ

# WRITE KEY INPUT
A = x0001
*A = *A + 1
A = *A - 1
*A = D

# WAIT UNTIL KEY IS UNPRESSED
A = x6000
D = *A
A = 4
D; JEQ
A = 12
JMP