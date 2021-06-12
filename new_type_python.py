prems=input("Entrez le premier nombre (s'il s'agit de puissance (p), entrez le nombre à élever) ")
sec=input("Entrez le deuxieme nombre (s'il s'agit de puissance entrez l'exposant) ")
operations,tab,tab_,operation,resultat,retenue=['+','-','*','/','%','p'],[[]],[],'.','',0

#meme taille pour les 2 nombres
def meme_taille(prems,sec):
    if len(prems)>len(sec):
        for i in range(len(prems)-len(sec)):
            sec='0'+sec
    elif len(sec)>len(prems):
        for i in range(len(sec)-len(prems)):
            prems='0'+prems
    return prems,sec

#methode addition
def addition(prems,sec):
    resultat,retenue="",0
    prems,sec=meme_taille(prems,sec)
    for i in range(len(prems),0,-1):
        temp_result=str(int(prems[i-1])+int(sec[i-1])+retenue)
        if i!=1:
            if int(temp_result)<=9:
                resultat=temp_result+resultat
                retenue=0
            else:
                resultat=temp_result[-1]+resultat
                retenue=1
        else:
            resultat=temp_result+resultat
    return resultat

#methode soustraction
def soustraction(prems,sec):
    prems,sec=meme_taille(prems,sec)
    retenue,resultat=0,''
    for i in range(len(prems),0,-1):
        if int(prems[i-1])-int(sec[i-1])-retenue<0:
            resultat,retenue=str(int('1'+prems[i-1])-int(sec[i-1])-retenue)+resultat,1
        else:
            resultat,retenue=str(int(prems[i-1])-int(sec[i-1])-retenue)+resultat,0
    return resultat

#methode multiplication
def multiplication(prems,sec):
    tab_,tab,retenue,boucle,test=[],[],0,0,10 
    for u in range(len(sec),0,-1):
        for i_ in range(boucle):
            tab_.append(0)
        for i in range(len(prems),0,-1):
            test=int(sec[u-1])*int(prems[i-1])+retenue
            if i!=1:
                if test<=9:
                    tab_.append(test)
                    retenue=0
                else:
                    var=str(test)
                    tab_.append(int(var[-1]))
                    retenue=int(var[:len(var)-1])
            else:
                tab_.append(test)
        retenue=0
        tab_.reverse()
        tab.append(tab_)
        tab_=[]
        boucle+=1
    if len(tab)%2!=0:
        tab.append([0])
    somme=0
    for i in range(len(tab)):
        for u in range(len(tab[i])):
            tab[i][u]=str(tab[i][u])
    for i in range(0,len(tab),2):
        prems,sec=''.join(tab[i]),''.join(tab[i+1])
        somme=int(addition(str(somme),addition(prems,sec)))
    return str(somme)

#methode division
def division_1(prems,sec):
	i=0
	while int(prems)>=int(sec):
		prems,i=soustraction(prems,sec),i+1
	return str(i)

def division(prems,sec):
	resultat=''
	for i in range(len(prems)):
		if int(prems[:i+1])>=int(sec):
			ind_test,test=i,prems[:i+1]
			break
	for i in range(ind_test,len(prems)):
		resultat_div=division_1(test,sec)
		resultat+=resultat_div
		test_mul=multiplication(resultat_div,sec)
		test=soustraction(test,test_mul)
		if i+1<len(prems):
			test+=prems[i+1]
	return resultat

#methode modulo
def modulo(prems,sec):
    return soustraction( prems,str(int(division(prems,sec))*int(sec)) )  

#methode puissance
def puissance_1(prems,sec):
    i,p=0,1
    while i<int(sec):
        i=int(addition(str(i),"1"))
        p=int(multiplication(prems,str(p)))
    return str(p)

def puissance(prems,sec):
	rst=''
	if int(sec)>100:
		div=division_1(sec,'100')
		rst=modulo(sec,'100')
		ret=puissance_1(prems,"100")
		ret=multiplication(puissance_1(ret,div),puissance_1(prems,rst))
		return ret
	else:
		return puissance_1(prems,sec)

#input opération
while not operation in operations:
    operation=input("Entrez l'operation ")

#addition +
if operation=='+':
    print(int(addition(prems,sec)))
    
#soustraction -
elif operation=='-':
    print(int(soustraction(prems,sec)))
    
#multiplication *
elif operation=='*':
    print(int(multiplication(prems,sec)))

#division /
elif operation=='/':
    print(int(division(prems,sec)))

#modulo
elif operation=='%':
    print(int(modulo(prems,sec)))

#puissance
elif operation=='p':
    print(int(puissance(prems,sec)))