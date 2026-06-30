def unique_substring(ss):
    unique_string_bool = set(ss) #Он создает массив и удаляет лишние символы
    if len(ss) == len(unique_string_bool): #Если изначальное количество символов в string и unique string не отличаются то это значит что в string нет повторяющихся символов
        return True
    else:
        return False
def len_return(s):
    strings = []
    for i in range(len(s)): #Переьирает по кол-ву символов в самой строке
        for j in range(i+1,len(s)+1): #Как я понял данный слайсер должен каждый раз разбивать на слайсы все больше и больше(Отсчет как очевидно начинается с нуля). i - начало, j - конец
            ss = s[i:j] #Обрезок для проверки в будующем
            if unique_substring(ss):
                strings.append(ss)
    return len(max(strings, key=len)) #ВНИМАНИЕ key=len УЖЕ ПОЛУЧАЕТ САМЫЙ ДЛИННЫЙ
print(len_return("baacab"))

# Оптимизированный вариант, мне помог дип сик

def unique_substring(ss):
    return len(ss) == len(set(ss))

def len_return(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            ss = s[i:j]
            if unique_substring(ss):
                if len(ss) > max_length:
                    max_length = len(ss)
    return max_length

print(len_return("baacab"))  # 3 ("bac" или "acb")
    