
#импорт всех программ в main
import Euclid as Eu
import perfection as per
import Pascal as Pas


def main():
    user_choise=input("Если вы хотите нати НОД чисел по алгоритму Евклида введите 1, если хотите проверить совершнное ли число нажмите 2, если хоите сделать треугольник паскаля нажмите 3.  ")
    if user_choise.lower()=="1":
        user_number=float(input("Введите число"))

        print("НОД чисел: ", Eu.Euclid(user_number))
    elif user_choise.lower()=="2":
        user_number=float(input("Введите число"))

        print("проверка на совершенность: ", per.Perfection(user_number))
    elif user_choise.lower()=="3":
     user_number=float(input("Введите число"))

     print("Треугольник паскаля: ", Pas.Pascal(user_number))
    
if __name__=="__main__":
        main()
    

    
