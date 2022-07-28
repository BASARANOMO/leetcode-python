# 592. Fraction Addition and Subtraction

## Solution

Simulation + calculating the greatest common divisor

Time complexity: `O(n + log C)` where `n` is the length of `expression` and `C` is the maximum value of the final denominator and numerator. The time complexity of calculating the greatest common divisor is `O(log C)`

Space complexity: `O(1)`
