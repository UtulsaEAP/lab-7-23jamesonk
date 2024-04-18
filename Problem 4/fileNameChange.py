#Kai Jameson
#Thursday @ 2pm

def fileNameChange():
    #type your code here
    fileName = input().strip()
    with open(fileName, 'r') as file:
        for line in file:
            modFile = line.strip().replace('_photo.jpg', '_info.txt')
            print(modFile)
    return

if __name__ == '__main__':
    fileNameChange()