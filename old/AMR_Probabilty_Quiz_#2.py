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
            p += str(self.answersList[self.problemOrder[x]])
            p += ",   "
        print p[:-4] #crops out the last ",   "
            

    def printTitle(self):
        print "Name: _________________________________________"
        print
        print "Date: _______________    Per: _________________"
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
    

############################################################
#### Worksheet #############################################
############################################################

worksheet = WorksheetClass("Probability Quiz #2: Word Problems")

#Question 1
N = ["red","blue","green"]
V = [str(random.randint(1,10)),str(random.randint(1,20)),\
                                    str(random.randint(11,20))]
random.shuffle(N)
random.shuffle(V)
question  = "A glass jar contains "+V[0]+" "+N[0]+", "+V[1]+" "
question += N[1]+" and "+V[2]+" "+N[2]+" jellybeans. If a "
question += "jellybean is chosen at random from the jar, what "
question += "is the probability that it is "+N[0]+" or "+N[1]+"?"
worksheet.pushQ(question)
aN = int(V[0])+int(V[1])
aD = int(V[0])+int(V[1])+int(V[2])
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Question 2
A = str(random.randint(7,30))
B = str(random.randint(5,int(A)-1))
question = "A number from 1 to "+A+" is chosen at random.  What is "
question += "the probability that the number chosen is odd or that "
question += "the number is greater than or equal to "+B+"?"
worksheet.pushQ(question)
aN = 0
for x in range(1,int(A)+1):
    if (x+1)%2 == 0 or x >= int(B):
        aN += 1
aD = int(A)
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Question 3
A = str(random.randint(5,15))
question  = "Spin a spinner numbered 1 to "+A+", and toss a coin. "
question += "What is the probability of getting an odd number on "
question += "the spinner and a tail on the coin?"
worksheet.pushQ(question)
aN = int(1)
aD = 2*int(A)
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"

worksheet.pushA(answer)

#Question 4
nA = ["hearts", "kings","aces","jacks","spades", "clubs"]
vA = [13, 4, 4, 4, 13, 13]
B = str(random.randint(2,4))
i = random.randint(0,5)
question  = B+" cards are chosen from a standard deck of 52 "
question += "playing cards with replacement.  What is the "
question += "probability of choosing "+B+" "+nA[i]+" in a row?"
worksheet.pushQ(question)
aN = vA[i]**int(B)
aD = 52**int(B)
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Question 5 & 6 Shared Components
nL = ["Washington", "Europe", "the future","my wildest dreams",
        "New England", "a volcano lair"]
random.shuffle(nL)
nA = ["garage","roof","television","killer robot infestation",\
        "computer","backyard","giant ants"]
random.shuffle(nA)

#Question 5
L = nL.pop()
A = nA.pop()
vAB = str(random.randint(20,80))
B = nA.pop()
vB = str(random.randint(10,90))
question = "In "+L+", if a house has a "+A+", there is a "
question += vAB+"% chance that it will have a "+B+". If there is an "
question += vB+"% probability that a houses will have a "+B+", "
question += "what is the probability that a house has a "+B+" "
question += "and a "+A+"?"
worksheet.pushQ(question)
answer = str(round(float(vB)/100 * float(vAB),2))+"%"
worksheet.pushA(answer)

#Question 6
L = nL.pop()
A = nA.pop()
vA = str(random.randint(40,90))
B = nA.pop()
vAB = str(random.randint(10,int(vA)-20))
question = "In "+L+", "+vA+"% of all households have a "+A+". "
question += vAB+"% of all households have a "+A+" and a "+B+". "
question += "What is the probability that a household has a "
question += A+" given that it has a "+B+"?"
worksheet.pushQ(question)
answer = str(round(100*float(vAB)/float(vA),2))+"%"
worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder(1,6)
print 
print
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
