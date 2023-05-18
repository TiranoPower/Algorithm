def solution(phone_number):
    
    length = len(phone_number) # 길이 추출

    mask = '*' * (length - 4) # 마지막 끝자리를 제외한 * 추출
    
    hidden_mask = mask + phone_number[-4:] # 마지막끝자리 제외 * +  마지막끝 4자리 번호 추출

    
    return hidden_mask 
        