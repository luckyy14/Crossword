from nltk.corpus import wordnet
import sys, copy

class Coordinates: #output "(x,y)"
    def __init__(self,x_initial,y_initial):  # init is a constructor.
        self.x = x_initial
        self.y = y_initial

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

class Space:  #output "Space(dir,size,(x,y))"
    def __init__(self,dir_init,length_init,point_init):
        self.dir = dir_init
        self.length = length_init
        self.start_point = point_init
    def __repr__(self):
        return "".join(["Space(", str(self.dir), ",", str(self.length),",", str(self.start_point), ")"])

def printCross(crossword):
    print("")
    print("\t\t\t***************Solved crossword*****************\n")
    for row in crossword:
        print("\t\t\t\t\t"+row)
    print("")
    print("\t\t\t************************************************\n")
def calculateHorizontal(crossword,crossword_size):
    horizontal_space_list = []
    for i in range(crossword_size):
        space_len = 0
        start_point = Coordinates(0,0)
        for j in range(crossword_size):
            if crossword[i][j] == '-':
                if space_len == 0:
                    start_point = Coordinates(i,j)
                    #print(start_point)
                space_len += 1
            elif crossword[i][j] =='=':
                if space_len > 1:
                    horizontal_space = Space('horizontal', space_len, start_point)
                    horizontal_space_list.append(horizontal_space)
                    #print(horizontal_space_list)
                space_len = 0  
        if space_len > 1:
            horizontal_space = Space('horizontal', space_len, start_point)
            horizontal_space_list.append(horizontal_space)
            #print(horizontal_space_list)
    return horizontal_space_list
       
def fillHorizontal(crossword,space,word):
    # Fill the - (empty spaces) with word in horizontal position
    temp_crossword = copy.deepcopy(crossword) 		#deep copy doesnt change original copies of crossword
    temp_crossword[space.start_point.x] = crossword[space.start_point.x][:space.start_point.y]+ word + crossword[space.start_point.x][space.start_point.y+len(word):]
    return temp_crossword

def calculateVertical(crossword,crossword_size):
    vertical_space_list = []
    for j in range(crossword_size):
        space_len = 0
        start_point = Coordinates(0,0)
        for i in range(crossword_size):
            if crossword[i][j] == '-':
                if space_len == 0:
                    start_point = Coordinates(i,j)
                    #print(start_point)
                space_len += 1
            elif crossword[i][j] =='=':
                if space_len > 1:
                    # Create Object Space containing information of fillable spaces in the crossword
                    vertical_space = Space('vertical', space_len, start_point)
                    vertical_space_list.append(vertical_space)
                    #print(vertical_space_list)
                space_len = 0
        if space_len > 1:
            vertical_space = Space('vertical', space_len, start_point)
            vertical_space_list.append(vertical_space)
            #print(vertical_space_list)
    return vertical_space_list 

def fillVertical(crossword,space,word):
    # Fill the - (empty spaces) with word in vertical position
    temp_crossword = copy.deepcopy(crossword)
    for k in range(len(word)):
        temp_crossword[space.start_point.x+k]=crossword[space.start_point.x+k][:space.start_point.y]+word[k]+crossword[space.start_point.x+k][space.start_point.y+1:]
    return temp_crossword
    
def generateSpaces(crossword,crossword_size):
    available_spaces = calculateHorizontal(crossword,crossword_size) + calculateVertical(crossword,crossword_size)
    #Sort All Object of Variable Spaces by length property
    available_spaces.sort(key=lambda x:x.length,reverse=True)
    return available_spaces

def verifySpaces(crossword,space,word):  #verify dir of space, 1 word all spaces available
    if(len(word) == space.length):
        for k in range(len(word)):
            if(space.dir=='horizontal'):
                if not crossword[space.start_point.x][space.start_point.y+k] in [word[k],'-']:
                    return None
            elif(space.dir=='vertical'):
                if not crossword[space.start_point.x+k][space.start_point.y] in [word[k],'-']:
                    return None

        return space.dir
    else:
        return None

def isFull(crossword,crossword_size):
    # returns false if the crossword does not have any (-)'s.
    for i in range(crossword_size):
        for j in range(crossword_size):
            if crossword[i][j]=='-':
                return False
    return True

def solveCrossword(crossword,crossword_size,available_space,available_word):
    # Crossword solver
    if available_word==[]:
        if isFull(crossword,crossword_size):
            printCross(crossword)
            return True
        else:
            return False
    else:
        #print(available_word)
        word = available_word[0]
        for space in available_space:
            dir = verifySpaces(crossword,space,word)
            if dir == 'horizontal':
                temp_crossword = fillHorizontal(crossword,space,word)
                #printCross(temp_crossword)
                if(solveCrossword(temp_crossword,crossword_size,available_space,available_word[1:])):
                    return True
            if(dir == 'vertical'):
                temp_crossword = fillVertical(crossword,space,word)
                #recursive call
                #printCross(temp_crossword)
                if(solveCrossword(temp_crossword,crossword_size,available_space,available_word[1:])):
                    return True
        return False
#Find synonym of word with given size
def synonym(answer,size):
    syns = wordnet.synsets(answer)
    #print(syns)
    answer_set=set()
    for words in syns:
        answer_set.add(words.lemmas()[0].name().encode('ascii','ignore'))   #takes word part of synset and converts it(nonetype) to ascii
    #	print(answer_set)
    for words in answer_set:
        if(len(words)==size):
            return words
            break

if __name__== '__main__':
    main_board=[]
    available_word=[]
    answer_list=[]
    print("\nEnter size of crossword (nxn) :")
    crossword_size=int(raw_input())			#crossword size n x n
    print("\nEnter empty crossword: (where - is  empty space and = is a block)") 
    for row in range(crossword_size):
        main_board.append(raw_input())			#board
    print("\nEnter list of clues (Must be synonyms from Dictionary.py)\n\t\t\t***************See readme for more**************")
    answer=raw_input().split(";")			#clue list
    print("\nEnter respective size of answers to be filled :")
    size=raw_input().split(";")				#size of result needed
    for i in range(len(answer)):
        answer_list.append(synonym(answer[i],int(size[i])))
    answer_list.sort(key=lambda item:(-len(item),item))	   # sorting length in descorder and words in alphabeticalorder.
    #print(answer_list)
    spaces = generateSpaces(main_board,crossword_size)	#generade spaces
    if not (solveCrossword(main_board,crossword_size,spaces,answer_list)):
        print("\nNo solutions found. Please try a new crossword. :) ")
        
    print("\nThe Crossword_Solver is Copyright (c) 2019 by Lakshay Baheti, Saurabh Mohata, Keshav Garg")
