def yosephus(n, k):
    people = list(range(1, n+1)) # [1 2 3 4 5 6 7],   7
    result =  [] 
    index = k-1
    while people :
        result.append(people.pop(index)) #result = [3,6,2,7,5]  , [1,4]
        if people : ## 리스트가 비어있지않으면
            index = (index +(k-1)) % len(people)  # [4,1,3,2,0,0]

    return result

n, k = map(int, input().split())  #


print("<" + ", ".join(map(str, yosephus(n,k))) + ">") # join 으로 문자열로 바꾸면 리스트가 없어짐

##  print(list(map(int, yosephus(n,k))))  ## 문자열 

