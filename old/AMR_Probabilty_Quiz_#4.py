#AMR Probability Quiz #4: Not Probability
#Python Genearated Quiz Ver. 4 (12/4/2014)

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
        print "Name: __________________________________________ \n"
        print "Date: _______________    Per: __________________ \n\n"
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

worksheet = WorksheetClass("Probability Quiz #4: Not Probability")

#Question 1: P(~A and ~B)
N = ["red","blue","green","yellow"]
V = [str(random.randint(1,10)),str(random.randint(1,20)),\
          str(random.randint(11,20)), str(random.randint(1,7))]
random.shuffle(N)
random.shuffle(V)
question  = "A glass jar contains "+V[0]+" "+N[0]+", "+V[1]+" "
question += N[1]+" and "+V[2]+" "+N[2]+", and "+V[3]+" "+N[3]+" "
question += "jellybeans. If a jellybean is chosen at random "
question += "from the jar, what is the probability that it is "
question += "neither "+N[0]+" nor "+N[1]+"?"
worksheet.pushQ(question)
aN = int(V[2])+int(V[3])
aD = int(V[0])+int(V[1])+int(V[2])+int(V[3])
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Question 2 & 3 & 4
N = ["math","English","history","Physics","Chemistry","Biology", \
     "PE", "Drama","Health"]
random.shuffle(N)

#Question 2: P(A and ~B)
nA = N.pop()
vA = str(random.randint(30,70))
nB = N.pop()
vB = str(random.randint(30,70))
vABmin = int(vA) + int(vB) - 100
vABmax = min(int(vA),int(vB))
vAB = str(random.randint(vABmin+20, vABmax-10))
question  = vA+"% of students take "+nA+". "+vB+"% of "
question += "students take "+nB+", and "+vAB+"% of students "
question += "take both. What percentage of students take "+nA+" "
question += "but not "+nB+"?"
worksheet.pushQ(question)
answer = str(int(vA)-int(vAB))+"%"
worksheet.pushA(answer)

#Question 3: P(~A and ~B)
nA = N.pop()
vA = str(random.randint(60,90))
nB = N.pop()
vB = str(random.randint(60,90))
vABmin = int(vA) + int(vB) - 100
vABmax = min(int(vA),int(vB))
vAB = str(random.randint(vABmin, vABmax-10))
question  = vA+"% of students take "+nA+". "+vB+"% of "
question += "students take "+nB+", and "+vAB+"% of students "
question += "take both. What percentage of students take neither "
question += nA+" nor "+nB+"?"
worksheet.pushQ(question)
answer = str(100 - (int(vA)+int(vB)-int(vAB)))+"%"
worksheet.pushA(answer)

#Question 4: P(~A|B)
nA = N.pop()
vA = str(random.randint(40,90))
nB = N.pop()
vAB = str(random.randint(10,int(vA)-20))
question  = vA+"% of all students take "+nA+". "+vAB+"% of all "
question += "students take "+nA+" and "+nB+". Given that they"
question += "are in "+nA+", what is the probability that a student "
question += "is not taking "+nB+"?"
worksheet.pushQ(question)
aN = int(vA) - int(vAB)
aD = int(vA)
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Question 5(~2), 6(~3) & 7(~4)
N = ["sharks","dinosaurs","ants","ninjas","zombies", "robots",\
     "squid","kittens"]
random.shuffle(N)

#Question 5(~2): P(~A and ~B)
nA = N.pop()
vA = str(random.randint(30,70))
nB = N.pop()
vB = str(random.randint(30,70))
vABmin = int(vA) + int(vB) - 100
vABmax = min(int(vA),int(vB))
vAB = str(random.randint(vABmin+10, vABmax-10))
question  = vA+"% of people are attacked by "+nA+". "+vB+"% of "
question += "people are attacked by "+nB+". "+vAB+"% of people "
question += "are attacked by both "+nA+" and "+nB+". What "
question += "percentage of people are not attacked by "+nB+" "
question += "but are attacked by "+nA+"?"
worksheet.pushQ(question)
answer = str(int(vA)-int(vAB))+"%"
worksheet.pushA(answer)

#Question 6(~3): P(~A and ~B)
nA = N.pop()
vA = str(random.randint(60,90))
nB = N.pop()
vB = str(random.randint(60,90))
vABmin = int(vA) + int(vB) - 100
vABmax = min(int(vA),int(vB))
vAB = str(random.randint(vABmin, vABmax-10))
question  = vA+"% of people are attacked by "+nA+". "+vB+"% of "
question += "people are attacked by "+nB+", and "+vAB+"% of people "
question += "are attacked by both. What is the probability "
question += "that you will not be attacked by either "+nA+" or "+nB+"?"
worksheet.pushQ(question)
answer = str(100 - (int(vA)+int(vB)-int(vAB)))+"%"
worksheet.pushA(answer)

#Question 7(~4):  P(~A|B)
nA = N.pop()
vA = str(random.randint(40,90))
nB = N.pop()
vAB = str(random.randint(10,int(vA)-20))
question  = vA+"% of all people are attacked by "+nA+". "+vAB+"% of "
question += "people are attacked by "+nA+" and "+nB+". If someone "
question += "is being attacked by "+nA+", what is probability "
question += "that they will not be attacked by "+nB+"?"
worksheet.pushQ(question)
aN = int(vA) - int(vAB)
aD = int(vA)
aF = simpFrac([aN,aD])
aP = str(round(100*float(aF[0])/float(aF[1]),2))
answer = str(aF[0])+"/"+str(aF[1])+" or "+aP+"%"
worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder()
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
