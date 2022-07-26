def  palindrom(s):
    l=''
    l=s[::-1]
    if l!=s:
        return False
    return True
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
file=open('words.txt','r')
fil=file.readlines()
for word in fil:
    word=word.strip()
    if palindrom(word):
        if len(word)==2:
            l2.append(word)
        if len(word)==3:
            l3.append(word)
        if len(word)==4:
            l4.append(word)
        if len(word)==5:
            l5.append(word)
        if len(word)==6:
            l6.append(word)
        if len(word)==7:
            l7.append(word)
             
print"Length Frequency    Palindroms"
print str(len(l2[0]))+'\t'+str(len(l2))+'\t\t'+ str(l2)+"\n"
print str(len(l3[0]))+'\t'+str(len(l3)),'\t\t'+ str(l3)+"\n\n"
print str(len(l2[0]))+'\t'+str(len(l4))+'\t\t'+ str(l4)+"\n\n"
print str(len(l2[0]))+'\t'+str(len(l5))+'\t\t'+ str(l5)+"\n\n"
print str(len(l2[0]))+'\t'+str(len(l6))+'\t\t'+ str(l6)+"\n"
print str(len(l2[0]))+'\t'+str(len(l7))+'\t\t'+ str(l7)+"\n"
