# Project 4

This README contains my thought processes before and after I began the `Mult` and `Fill` projects this week.


## `Mult.asm`

### The Plan

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

### The Result

This project went fairly smoothly. As I finished up this project, I realized I was still adjusting to placing the result value in a specific register, rather than just "returning" it as you would in C++, Python, JavaScript, etc.

When I realized that the output value was going to `R2`, I realized that I didn't need the `product` variable, and that I should instead use `@R2`.


## `Fill.asm`

### The Plan

To fill in pixels on the screen based on user input (where any input causes the screen to fill), I'll establish two "functions" using jumps that will either set each pixel to black and increase the X and Y values, or set each pixel to white and decrease the X and Y values.

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


### Adjustments for `Fill.asm`

My plan generally worked, my one oversight being that one register represents *16* pixels on the screen, not just *1*. Therefore I had two options:

1. Create nested logic where each pixel is filled in individually.
2. Fill the screen in 16 pixels at a time.

I began attempting to fill the screen in one pixel at a time, as I take instructions literally, but writing that in assembly was becoming increasingly difficult, especially with the general structure of assembly being new to me.

After reviewing the requirements for the assignment, I realized I could fill the screen in 16 pixels at a time by setting `M` equal to `-1`, rather than positive `1`.
