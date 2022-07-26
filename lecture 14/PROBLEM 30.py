import string
fp = open("emma.txt", "r")
w_file = open("words.txt", "r")

def skip_header_inf():
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def create_dictionary():
    frequency = dict()
    for word in w_file:
        word = word.strip()
        if 5 <= len(word) <= 10:
            frequency[word] = 0
    w_file.close()
    return frequency
    
def count_frequency(frequency):         
    for line in fp:
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            if word in frequency:
                frequency[word] += 1  
    fp.close()
    return frequency

def build_list(frequency):
    w_list = list()
    for word in frequency:
        w_list.append((frequency[word], word))
    return w_list
        
def sort_by_frequency(w_list):    
    w_list.sort(reverse = True)
    return w_list

def print_top_20(w_list):
    for i in range(20):
        freq, word = w_list[i]
        print word, freq

def main():
    skip_header_inf()
    frequency = create_dictionary()
    frequency = count_frequency(frequency)
    w_list = build_list(frequency)
    w_list = sort_by_frequency(w_list)
    print_top_20(w_list)

main()
    
        
 
