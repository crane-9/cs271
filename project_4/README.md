# Project 4


## Plan for `Mult.asm`

To multiply two values (`R0` and `R1`), I plan to use a loop and addition.

Logic as written in C:

```c
// where `a` is R0 and `b` is R1
// `iter` being short for "current iteration"

int iter = 1;
int product = 0;

while (iter < a){
    product += b;
    iter++;
}
```


## Plan for `Fill.asm`

To fill in pixels on the screen based on user input, I'll establish two "functions" using jumps that will either set each pixel to black and increase the X and Y values, or set each pixel to white and decrease the X and Y values.

Logic in C:

```c
// where `SCREEN` is the screen.
// where `input` is a pointer to the input
// where `OFFSET_LIMIT` is an unknown limit for the screens pixel count.

int currentPixelOffset = 0;

void color() {
    SCREEN[currentPixelOffset] = 1;
    
    if (currentPixelOffset < OFFSET_LIMIT) {
        currentPixelOffset ++;
    }
}

void uncolor() {
    SCREEN[currentPixelOffset] = 0;

    if (currentPixelOffset > 0) {
        currentPixelOffset --;
    }
}

while (true) {
    if (*INPUT) {
        color();
    } else {
        uncolor();
    }
}
```

