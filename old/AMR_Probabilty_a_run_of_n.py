#AMR Probability Quiz #2
#Python Genearated Quiz 2

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
            a = self.shuffleIndex
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
            p += str(self.answersList[self.problemOrder[x]])
            p += ",   "
        print p[:-4] #crops out the last ",   "
            

    def printTitle(self):
        print "Name: __________________________________________ \n"
        print "Date: _______________    Per: __________________ \n\n"
        print self.title + "\n"

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
    

############################################################
#### Worksheet #############################################
############################################################

#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK#NEEDS WORK


worksheet = WorksheetClass("Probability Coin Flip Worksheet")

#Question 1
A = "3"
question  = "What is the probability of flipping "+A+" "
question += "coins and having a string of exactly "
question += "1, 2, 3, . . ., "+A+" heads come up?"
#tails = 0, heads = 1
t = []
for x in range(int(A)+1):
    t.append(0)

for x in itertools.product(range(0,2), repeat=int(A)):
    y = 0
    for i in range(len(x)):
        if x[i] == 1:
            y += 1
        else:
            t[y] += 1
            y = 0
    if y != 0:
        t[y] += 1
        y = 0
worksheet.pushQ(question)

aD = 2**int(A)
print t
answer = "\n"

#this fixes a bug whre t[0] is wrong
aN = 1
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer += str(0)+": "+str(aF[0])+"/"+str(aF[1])+" or "+aP+"%\n"

for i in range(1,len(t)):
    aN = t[i]
    aF = simpFrac([aN,aD])
    aP = str(round(100*float(aF[0])/float(aF[1]),2))
    answer += str(i)+": "+str(aF[0])+"/"+str(aF[1])+" or "+aP+"%\n"
worksheet.pushA(answer)

#Worksheet Layout
#worksheet.shuffleOrder(1,6)
print 
print
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
