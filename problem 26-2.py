
c=[(9,15,13,"USA"),(10,13,7,"GER"),(14,7,5,"CAN"),(9,8,6,"NOR"),(4,6,6,"ÄUS"),(3,5,7,"RUS"),(6,6,2,"S.KOR"),(5,2,4,"PRC"),(5,2,4,"SWED"),(2,3,6,"FRAN"),(6,0,3,"SWZE"),(4,1,3,"NED"),(2,0,4,"CZEC"),(1,3,2,"POL"),(1,1,3,"ITA"),(0,3,2,"JAP"),(0,1,4,"FIN"),(2,1,0,"AUL")]
x=[]
for m in c:
    g,s,b,n=m
    t=g+s+b
    x.append((t,n,g,s,b))
        
print "Nation\tGold\tSilver\tBronze\tTotal"
for k in x:
    t,n,g,s,b=k
    print n,"\t",g,"\t",s,"\t",b,"\t",t
    
