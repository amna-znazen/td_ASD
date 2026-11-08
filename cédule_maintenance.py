import random
unit=7
capacite=[20,15,35,40,15,15,10]
nbre_interv_necessaire=[2,2,1,1,1,1,1]
pui_chaque_interv=[80,90,65,70]
capacite_tot=sum(capacite)
chromosome =["0110","0011","0001","1000","0100","0010","1000"]
P_perdue=[]
res_intervention=[]
for i in range (4):
    somme=0
    for j in range (7):
        bit=int(chromosome[j][i])
        somme+=bit*capacite[j]
    print ("intervalle",i+1,"=",somme)
    P_perdue.append(somme)
    res_intervention.append(capacite_tot -pui_chaque_interv[i] - somme )
print(res_intervention)
fitnesse=min(res_intervention)
if (fitnesse<0): fitnesse=0
parent1=["0110","0011","0001","1000","0100","0010","1000"]
parent2=["1100","0110","0100","0001","0010","1000","0100"]
A=random.randint(1,7)
print(A)
enfant1 = parent1[:A] + parent2[A:]
enfant2 = parent2[:A] + parent1[A:]
print ("parent 1: ",parent1)
print("parent 2:" ,parent2)
print("enfant 1 : ",enfant1)
print("enfant 2: ",enfant2)