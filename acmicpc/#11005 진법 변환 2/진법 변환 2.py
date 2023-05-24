def convert_to_base(n, b):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while n > 0:
        result = chars[n % b] + result
        n = n // b
        
    return result

n, b = map(int, input().split())
print(convert_to_base(n, b))
