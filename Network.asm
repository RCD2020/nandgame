# ------------- ADDRESSES -------------

# 0x4000 : DISPLAY
# 0x6001 : NETWORK
# 0x6002 : SYNC BIT

# 0x1000 : RETURN BIT
# 0x1001 : RETURN INFORMATION

# -------- SKIP OVER FUNCTIONS --------
A = 
JMP

# ------ ROUTE TO RETURN ADDRESS ------
A = 0x6003
A = *A
JMP

# ----------- READ SYNC BIT -----------
A = 0x6001
D = *A
# MASK TO GET SECOND BIT
A = 0x0002
D = D & A
# ROUTE TO RETURN
A = 2
JMP

# -------- STALL FOR SYNC BIT ---------
# GET SYNC BIT
A = 5
JMP
# TEST IF SYNC != 
# ROUTE TO RETURN
A = 2
JMP

# ------ WAIT FOR DATA BIT == 1 -------
A = 0x6001
D = *A
A = 0x0001
D = D & A
# RETURN TO BEGINNING OF FUNCTION
A = 0
D; JEQ

# ----- WAIT FOR SYNC BIT TO FLIP -----
A = 0x6001
D = *A

# ----------- READ DATA BIT -----------

# -------- WRITE BIT TO SCREEN --------