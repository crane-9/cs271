@offset
M=0

// keeps track of where to return to.
@fill_return
M=0


(LOOP)
    //check keyboard input
    @KBD
    D=M

    // act based on keyboard input
    @BLANK
    D;JLE // if no input: BLANK

    @FILL // else, fill
    0;JMP 


(FILL)
    @SCREEN
    D=A

    @offset
    D=D+M

    // back to the loop if the offset is too big
    @KBD
    D=A-D

    @LOOP
    D;JLE

    // get current pixel
    @SCREEN
    D=A

    @offset
    D=D+M
    M=M+1

    // fill in next pixel
    A=D
    M=-1

    // always hop back to the start of the loop
    @LOOP
    0;JMP

(BLANK)
     // ensure in range
    @offset
    D=M
    
    @LOOP // jump if offset is less than 0
    D;JLT
    
    @SCREEN
    D=A

    @offset
    D=D+M
    M=M-1


    // goto next address and set to 0
    A=D
    M=0

    @LOOP
    0;JMP
