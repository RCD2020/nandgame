# ------------- ADDRESSES -------------

# 0x4000 : DISPLAY
# 0x6001 : NETWORK
# 0x6002 : SYNC BIT
# 0x6003 : DATA BIT
# 0x6004 : DATA BIT COUNT

# 0x1000 : RETURN ADDRESS
# 0x1001 : PREVIOUS RETURN ADDRESS
# 0x1002 : RETURN INFORMATION

# -------- SKIP OVER FUNCTIONS --------
A = 35
JMP

# ------ ROUTE TO RETURN ADDRESS ------
A = 0x1000
A = *A
JMP

# ----------- READ SYNC BIT -----------
A = 0x6001
D = *A
# MASK TO GET SECOND BIT
A = 0x0002
D = D & A
A = 0x1002
*A = D
# ROUTE TO RETURN
A = 2
JMP

# -------- STALL FOR SYNC BIT ---------
# TEST IF SYNC BIT != 0x6002
# SET UP RETURN
A = 0x1000
D = *A
A = 0x1001
*A = D
A = 23
D = A
A = 0x1000
*A = D
# CALL READ SYNC FUNCTION
A = 5
JMP
# RETURNED HERE, SHIFT PREVIOUS ADDRESS
A = 0x1001
D = *A
A = 0x1000
*A = D
# COMPARE 0x1002 TO 0x6002
A = 0x1002
D = *A
A = 0x6002
D = D - *A
A = 13
D; JEQ
# ROUTE TO RETURN
A = 2
JMP

# ------ WAIT FOR DATA BIT == 1 -------
A = 0x6001
D = *A
A = 0x0001
D = D & A
# RETURN TO BEGINNING OF FUNCTION
A = 35
D; JEQ

# ----- WAIT FOR SYNC BIT TO FLIP -----
A = 47
D = A
A = 0x1000
*A = D
A = 13
JMP
A = 0x7fff

# ----------- READ DATA BIT -----------

# -------- WRITE BIT TO SCREEN --------