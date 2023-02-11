import sys 

def rot13(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char)- 65 + 13) % 26 + 65)
            else : result += chr((ord(char)- 97 + 13) % 26 + 97)

        else : 
            result += char # 알파벳 확인안하면 그대로

    return result        

print(rot13(input()))

# isalpha() : 알파벳 확인하는 함수
# isupper() : 대문자인지 확인하는 함수
# a : 97
# A : 65
# m, M  = 26개의 중간
# % 로 나누면 = 나눈 나머지 값이 저장