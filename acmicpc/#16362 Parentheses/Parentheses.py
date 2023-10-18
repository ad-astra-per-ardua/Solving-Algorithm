import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

def count(command, token):
    return command.count(token)

def main():
    op = {'+', '-', '*', '/', '%'}
    
    command = input().strip()
    length = len(command)
    
    if count(command, '(') != count(command, ')'):
        print("error")
        return
    
    st = []
    improper = False
    
    i = 0
    while i < length:
        while i < length and command[i] == ' ':
            i += 1
        
        if i >= length:
            break
        
        if command[i] == '(':
            if st and st[-1] == 's':
                print("error")
                return
            st.append('(')
        elif command[i] in op:
            if not st or st[-1] != 's':
                print("error")
                return
            st.append('o')
        elif command[i] == ')':
            if not st or st[-1] != 's':
                print("error")
                return
            st.pop()
            
            opTurn = True
            cnt = 0
            while st:
                if opTurn:
                    if st[-1] == 'o':
                        cnt += 1
                    elif st[-1] == '(':
                        if cnt != 1:
                            improper = True
                        break
                    opTurn = False
                else:
                    if st[-1] != 's':
                        print("error")
                        return
                    opTurn = True
                st.pop()
            
            st.pop()
            st.append('s')
        else:
            if not st or st[-1] != 's':
                st.append('s')
            else:
                print("error")
                return
        i += 1
        
    if improper:
        print("improper")
        return

    strTurn = True
    cnt = 0
    while st:
        if strTurn:
            if st[-1] != 's':
                print("error")
                return
            st.pop()
            strTurn = False
        else:
            if st[-1] != 'o':
                print("error")
                return
            st.pop()
            strTurn = True
            cnt += 1

    if cnt == 1:
        print("proper")
    else:
        print("improper")
    
if __name__ == "__main__":
    main()
