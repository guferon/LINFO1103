#! /usr/bin/python3

def top3(mesures):
    '''
    Etant donne une sequence de mesures espacees de 10 minutes, identifie les trois mesures les plus élevées.

    pre: - mesures est un tableau (list)
         - len(mesures) >= 3
    post: renvoie un tableau t de longueur 3 tel que mesures[t[i]] correspond à la i^eme mesure la plus elevee.
    '''
    x = float('inf')
    ans = [-x,-x,-x]
    ans_index = [0,0,0]
    k=-1
    for i in range(len(mesures)):
        k+=1
        if mesures[i] > ans[2]:
            if mesures[i] > ans[1]:
                if mesures[i] > ans[0]:
                    ans.insert(0, mesures[i])
                    ans_index.insert(0, k)
                    
                else:
                    ans.insert(1, mesures[i])
                    ans_index.insert(1, k)

            else:
                ans.insert(2, mesures[i])
                ans_index.insert(2, k)
            
            #Sup le 4eme elements 
            del ans[3]
            del ans_index[3]
            
    return ans_index


         



#Exemples tests:
print(top3([47, 3, -45]))
print(top3([10, 0, 5, 10, 30, 10, 20, 30]))
print(top3([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(top3([0, 1, 2, 3]))
if not top3([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0,1,2]:
    print("Top 3 au début")

if not top3([0, 1, 2, 3]) == [3,2,1]:
    print("Top 3 à la fin")