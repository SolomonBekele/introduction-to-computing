def create_list():
    countries = ["United States", "Germany", "Canada", "Norway", "Austria",
                 "Russia", "South Korea", "China", "Sweden", "France",
                 "Switzerland", "Netherland", "Chech Republic", "Poland",
                 "Italy", "Japan", "Finland", "Australia", "Belarus",
                 "Slovakia", "Croatia", "Slovenia", "Latvia", "Great Britain",
                 "Estonia", "Kazahstan"]
    golds = [9, 10, 14, 9, 4, 3, 6, 5, 5, 2, 6, 4, 2, 1, 1, 0,
             0, 2, 1, 1, 0, 0, 0, 1, 0, 0]
    silvers = [15, 13, 7, 8, 6, 5, 6, 2, 2, 3, 0, 1, 0, 3, 1, 3,
               1, 1, 1, 1, 2, 2, 2, 0, 1, 1]
    bronzes =[13, 7, 5, 6, 6, 7, 2, 4, 4, 6, 3, 3, 4, 2, 3, 2,
              4, 0, 1, 1, 1, 1, 0, 0, 0, 0]

    med_list = list()
    for i in range(len(countries)):
        med_list.append((countries[i], golds[i], silvers[i], bronzes[i]))
    return med_list  
medal_list = create_list()
print "_-------------------  list by reading from a file -----------------------------------------"
print "rank  country name     golds   silvers   bronzes   "
print "_------------------------------------------------------------------------------------------"
for i in range(10):
   print " %3d   %-15s    %3d    %3d       %3d"  % ( i+1, medal_list[i][0],   medal_list[i][1],  medal_list[i][2],  medal_list[i][3]  )
#####################################################
def create_list_2():
    mfile = open("medals.txt", "r")
    med_list = []
    for item in mfile:
        line = item.rstrip()
        line = line.split(" ")
        if len(line) == 5:
            nation = line[0] + " " + line[1]
#           print "nation 1 = ", nation
            line.pop(0)
#           print "line 1 = ", line
            line[0] = nation
#            print "line 2 = ", line
        med_list.append(line)
    mfile.close()
    return med_test
def print_list(medals):
    for i in range(15):
          print " %3d   %-15s    %3d    %3d       %3d"  % ( i+1, medal_list[i][0],   int (medal_list[i][1]), int(medal_list[i][2]), int(medal_list[i][3])  )

####################prob26-2

    
