class Solution:
    def fractionAddition(self, expression: str) -> str:
        denominator, numerator = 0, 1
        i, n = 0, len(expression)
        while i < n:
            denominator_next, sign = 0, 1
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator_next = denominator_next * 10 + int(expression[i])
                i += 1
            denominator_next = sign * denominator_next

            i += 1  # '/'

            numerator_next = 0
            while i < n and expression[i].isdigit():
                numerator_next = numerator_next * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator_next + denominator_next * numerator
            numerator *= numerator_next

        if denominator == 0:
            return "0/1"

        greatestCommonDivisor = gcd(abs(denominator), numerator)
        return f"{denominator // greatestCommonDivisor}/{numerator // greatestCommonDivisor}"
