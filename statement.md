# Guess the number

Guess the number I am thinking of!

You know that the number `x` I am thinking of is between `a` and `b`, i.e., `a <= x <= b`.
You can try to guess a number `c`. If `c == x`, you win. Otherwise, I will tell you whether `x > c` or `x < c`, and you can try again.
Find the number `x` with as few guesses as possible!

## Interface

<description for="guess">

Write a function `guess` which takes in input the two numbers `a` and `b`,
and can invoke a callback `answer` to try to guess a number `c`.

If `c == x`, `answer` will not return, and you win.
Otherwise, `answer` will return `+1` if `x > c` and `-1` if `x < c`.

</description>

The function `guess` will be called exactly once.

## Scoring

Your solution will be tested with the following assumptions:

* `a = 1`
* `b <= 10^9`

### Goals

* `easy`: your program guesses correctly with at most `b` trials (assuming `b <= 10^3`).
* `hard`: your program guesses correctly with at most 30 trials.

### Limits

Standard time/memory limits apply.
