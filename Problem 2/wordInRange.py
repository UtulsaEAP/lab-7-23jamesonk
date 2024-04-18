#Kai Jameson
#Thursday @ 2pm

def wordInRange():
    #Type your code here
    inputFile = input()
    start = input()
    end = input()

    with open(inputFile, 'r') as f:
        inputWords = f.readlines()
    #check which file words are in
    for i in range(len(inputWords)):
        if inputWords[i] >= start + '\n' and inputWords[i] <= end + '\n':
            inputWords[i] = inputWords[i].strip()
            print(inputWords[i] + ' - in range')
        else: 
            inputWords[i] = inputWords[i].strip()
            print(inputWords[i] + ' - not in range')
    return
if __name__ == '__main__':
    wordInRange()