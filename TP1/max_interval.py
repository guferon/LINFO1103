#! /usr/bin/python3

def max_interval(mesures):
    '''
    Etant donne une sequence de mesures espacees de 10 minutes, determine l'intervalle d'une heure durant lequel le niveau d'eau est le plus eleve en moyenne.

    pre: - mesures est un tableau (list)
         - len(mesures) >= 7
    post: renvoie l'indice du tableau mesures auquel commence le premier sous-tableau de longueur 7 de plus forte moyenne.
    '''
    k = 0
    count = 0
    ans = 0
    while k <=len(mesures):
        sum = 0
        for i in range(7):
            sum += mesures[i+k]
        if count == 0:
            count = sum/7
        elif sum/7 > count:
            count = sum/7
            ans = k

        if len(mesures)-k <= 7:
            return ans 
        k+=1
    return ans



#Exemples tests:
print(max_interval([-31, -44, -4, -46, -7, -29, -20, -15]))

#if not max_interval([60, 0, 5, 10, 30, 10, 20, 30]) == 0:
    #print("Plus longue serie au debut")

#if not max_interval([10, 0, 5, 10, 30, 10, 20, 30]) == 1:
    #print("Plus longue serie a la fin")