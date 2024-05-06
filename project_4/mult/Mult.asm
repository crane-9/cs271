
// initialize iteration counter.
@iter
M=0

// initialize product
@R2
M=0

(LOOP)
    // if iter - R0 >= 0, end
    @iter
    D=M // d = iter

    @R0
    D=M-D // d = R0 - iter

    @END
    D;JLE // jump if 0 iterations remain.

    // increase product by R1
    @R1
    D=M // d = R1's value

    @R2
    M=M+D // product = product + R1's value

    @iter
    M=M+1 // increase count
    
    @LOOP
    0;JMP


(END)
    @END
    0;JMP

