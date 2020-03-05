#AMR Probability Quiz #3: Combinations and Permutations
#Python Genearated Quiz 3

############################################################
#### Code ##################################################
############################################################

import random
import itertools

class WorksheetClass:
    questionsList = []
    answersList = []
    problemOrder = []
    problemTotal = 0
    problemIndex = 0
    shuffleIndex = 0
    title = ""

    def __init__(self, S=""):
        self.questionsList = []
        self.answersList = []
        self.problemOrder = []
        self.problemTotal = 0
        self.problemIndex = 0
        self.shuffleIndex = 0
        self.title = S
        
    def pushQ(self, S=""):
        self.questionsList.append(S)
        self.problemOrder.append(self.problemTotal)
        self.problemTotal += 1
        while len(self.answersList)+1 < len(self.questionsList):
            self.answersList.append("")
    
    def pushA(self, S=""):
        self.answersList.append(S)
        
    def shuffleOrder(self, a="", b=""):
        if a == "":
            a = self.shuffleIndex+1
        if b == "":
            b = self.problemTotal
            self.shuffleIndex = self.problemTotal
        temp = self.problemOrder[:]
        temp0 = temp[a-1:b]
        random.shuffle(temp0)
        temp[a-1:b] = temp0
        self.problemOrder = temp[:]
        
    def printQuestions(self, a=1, b=""):
        if b == "":
            b = self.problemTotal
        for x in range(a-1,b): 
            self.problemIndex += 1
            p  = str(self.problemIndex) + ")   "
            p += str(self.questionsList[self.problemOrder[x]])
            print p + "\n"
    
    def printAnswers(self):
        while len(self.answersList) < len(self.questionsList):
            self.answersList.append("")
        p = ""
        for x in range(len(self.answersList)):
            p += str(x+1) + ") " 
            p += str(self.answersList[self.problemOrder[x]]) + ",   "
        print p[:-4] #crops out the last ",   "
            

    def printTitle(self):
        print "Name: __________________________________________ "
        print "Date: _______________    Per: __________________ "
        print
        print self.title
        print 

def simpFrac(F):
    if len(F) == 2:
        N = F[0]
        D = F[1]
    if len(F) == 1:
        N = F[0]
        D = 1
    x=2
    while x <= min(N,D):
        if N%x== 0 and D%x == 0:
            N = N/x
            D = D/x
            x = 1 #becomes 2
        x += 1
    return [N,D]        

def factoral(n):
    if n <= 0: return 0
    returnNumber = 1
    for x in range(1,n+1):
        returnNumber *= x
    return returnNumber

def shuffleString(passS):
    S = passS
    returnString = ""
    while len(S) > 0:
        i = random.randrange(len(S))
        returnString += S[i]
        S = S[:i]+S[i+1:]
    return returnString

def sortString(passS):
    S = passS
    return ''.join(sorted(S))

#SimpleAlphabet = "abcdefghijklmnoprstuvwxyz"
#Alphabet = "abcdefghijklmnopqrstuvwxyz"

############################################################
#### Worksheet #############################################
############################################################

worksheet = WorksheetClass("Probability Quiz #4: Combinations \
and Permutations")



for c_o_u_n_t in range(2):
    #Question 1
    A = "abcdefghijklmnopqrstuvwxyz"
    A = shuffleString(A)
    B = str(random.randint(7,12))
    C = str(random.randint(3,5))
    A = A[:int(B)]
    question  = "How many ways are there to make "+C+" letter arrangements "
    question += "of the letters '"+A[:int(B)]+"'? So, for example, '"+A[:int(C)]+"' "
    question += "is a "+C+" letter arrangement."
    worksheet.pushQ(question)
    aN = 1 #fast factoral
    for x in range(int(B), int(B)-int(C), -1):
        aN *= x
    answer = str(aN)
    worksheet.pushA(answer)

    #Question 2
    A = "abcdefghijklmnopqrstuvwxyz"
    A = shuffleString(A)
    L = random.randint(8,12) #string length
    nB = random.randint(1,3)
    nC = []
    for x in range(nB):
        nC.append(random.randint(2,3))
    tC = sum(nC)
    L = max(nB + tC,L)   
    A = A[:L-tC]
    for x in range(len(nC)):
        A += A[x]*nC[x]
    #A = shuffleString(A)
    A = sortString(A)
    question  = "How many distinct ways are there to rearrange the "
    question += str(L)+" letters '"+A+"'?"
    worksheet.pushQ(question)
    aN = factoral(L)
    for x in range(len(nC)):
        aN = aN/factoral(nC[x]+1)
    answer = str(aN)
    worksheet.pushA(answer)

    #Question 3
    A = str(random.randint(3,7))
    question  = "How many different "+A+" card hands can you make from a "
    question += "standard deck of playing cards? A standard deck has 52 "
    question += "distinct cards."
    worksheet.pushQ(question)
    aN = 1
    for x in range(52,52-int(A),-1):
        aN = aN*x
    aN = aN/factoral(int(A))
    answer = str(aN)
    worksheet.pushA(answer)

    #Question 4
    A = str(random.randint(10,20))
    B = str(random.randint(3,7))
    question  = "Tickets are placed in a hat numbered 1 through "+A+" "
    question += "You reach in and grab "+B+" tickets. What is "
    question += "the probability that you have grabbed tickets that "
    question += "are numbered 1 through "+B+"?"
    worksheet.pushQ(question)
    aD = 1
    for x in range(int(A),int(A)-int(B),-1):
        aD = aD*x
    aD = aD/factoral(int(B))
    aN = 1
    aF = simpFrac([aN,aD])
    aP = str(round(100*float(aF[0])/float(aF[1]),2))
    answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
    worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder(1,4)
worksheet.shuffleOrder(5,8)
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
