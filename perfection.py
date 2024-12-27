#Проверка на совершенное число 


def perfect(n, i=1, sum_divisors=0):#вызываем функцию  
    
    if i == n:# если текущий делитель равен n
        return sum_divisors == n#функция возвращает True
    
    if n % i == 0:#если n делится на i без остатка
        sum_divisors += i#прибавляем в переменную этот делитель 
    return perfect(n, i + 1, sum_divisors)#вызываем функцию ещё раз, с делителем больше на 1
def main():

    num = int(input("Введите число для проверки: "))#вводим число с клавиатуры
    if perfect(num):#задаём условие, если число является совершенным
        print("True")#выводим True
    else:#если нет
        print("False")#выводим False
        main()

if __name__=="__main__":
    main()     
