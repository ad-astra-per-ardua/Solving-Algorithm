import math,sys
input = sys.stdin.readline

numerator_a, denominator_a = map(int,input().split())
numerator_b, denominator_b = map(int,input().split())

fin_denominator = denominator_a * denominator_b
fin_numerator = numerator_a * denominator_b + numerator_b * denominator_a

gcd = math.gcd(fin_numerator,fin_denominator)
fin_numerator //= gcd
fin_denominator //= gcd
print(fin_numerator, fin_denominator)
