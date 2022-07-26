def build_table():
  t = [0] * 13
  for item in medals:
     total = sum(item[1:])
     t[total/3] += 1
  return t
     
def plot_table(t):
    for i in range(13):
        print str(3*i) + "~" + str(3*i +2) + ":\t"  + "*" *  t[i]

def sum(n_medals):
    return int(n_medals[0]) + int(n_medals[1]) + int(n_medals[2])

def create_list():
    mfile = open("medals.txt", "r")
    for item in mfile:
        line = item.rstrip()
        line = line.split(" ")
        if len(line) == 5:
            nation = line[0] + " " + line[1]
            line.pop(0)
            line[0] = nation
        medals.append(line)
    mfile.close()

def plot_list():
    table = build_table()
    plot_table(table)
    
   
medals = list()
create_list()
plot_list()
