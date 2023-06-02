def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']  
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    total_days = sum(month[:a-1])  # 주어진 월 이전까지의 일 수를 더합니다.
    total_days += b - 1  # 주어진 일을 더하고 1을 뺍니다. (인덱스는 0부터 시작하므로)
    answer = date[total_days % 7]  # 요일 리스트에서 해당 날짜의 요일을 구합니다.
    
    return answer  # 결과값 요일을 반환합니다.


## 복습 필요