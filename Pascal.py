#треугольник паскаля




def combination(n, k):# Вызываем функцию 

    if k == 0 or k == n: # задаём условие, если к равно нулю или к равно n
        return 1#возвращаем в 1 
    return combination(n - 1, k - 1) + combination(n - 1, k) #возвращаем комбинацию

def pascals_triangle(rows): #функция 
    
    for row in range( rows):
        answer = ""
        for column in range( row + 1):
            answer = answer + str(combination(row, column)) + "\t"
        print(answer)

def main():
    x = int(input("Введите количество строк:" ))
    print("Треугольник Паскаля: ")
    pascals_triangle(x) # Вызов

if __name__=="__main__":
        main()