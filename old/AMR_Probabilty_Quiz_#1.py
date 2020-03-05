#AMR Probability Quiz #1
#Python Genearated Quiz Ver. 4 (12/5/2014)

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

worksheet = WorksheetClass("Probability Quiz #1: Equations")

#Question 1: P(A), P(B), P(A&B)=0, Find P(A or B)
A = str(random.randint(5, 49))
B = str(random.randint(5, 49))
Q  = []
Q.append(str("P(A) = "+A+"%. "))
Q.append(str("P(B) = "+B+"%. "))
Q.append(str("A and B are mutually exclusive events. "))
random.shuffle(Q)
question = ""
for i in Q:
    question += i
question += "What is the value of P(A or B)? "
worksheet.pushQ(question)
answer = str(int(A)+int(B))+"%"
worksheet.pushA(answer)

#Question 2: P(A), P(B), P(A&B)!=0, Find P(A or B)
AB = str(random.randint(5,40))
A = str(random.randint(5, 49)+int(AB))
B = str(random.randint(5, 49))
Q  = []
Q.append(str("P(A) = "+A+"%. "))
Q.append(str("P(B) = "+B+"%. "))
Q.append(str("P(A & B) = "+AB+". "))
random.shuffle(Q)
question = ""
for i in Q:
    question += i
question += "What is the value of P(A or B)? "
worksheet.pushQ(question)
answer = str(int(A)+int(B)-int(AB))+"%"
worksheet.pushA(answer)

#Question 3: P(A), P(B), P(A or B), Find P(A&B)
AB = str(random.randint(5,40))
A = str(random.randint(5, 49)+int(AB))
B = str(random.randint(5, 49))
Q  = []
Q.append(str("P(A) = "+A+"%. "))
Q.append(str("P(B) = "+B+"%. "))
Q.append(str("P(A or B) = "+AB+". "))
random.shuffle(Q)
question = ""
for i in Q:
    question += i
question += "What is the value of P(A & B)? "
worksheet.pushQ(question)
answer = str(int(A)+int(B)-int(AB))+"%"
worksheet.pushA(answer)

#Question 4: P(A), P(B), A & B are independnt, Find P(A&B)
A = str(random.randint(5, 95))
B = str(random.randint(5, 95))
Q  = []
Q.append(str("P(A) = "+A+"%. "))
Q.append(str("P(B) = "+B+"%. "))
Q.append(str("A and B are independent events. "))
question = ""
random.shuffle(Q)
for i in Q:
    question += i
question += "What is the value of P(A & B)? "
worksheet.pushQ(question)
answer = str(int(A)+int(B)-int(AB))+"%"
worksheet.pushA(answer)

#Question 5: P(A|B), P(B), Find P(A & B)
B = str(random.randint(20,90))
A = str(random.randint(5,int(B)-10))
AB = str(random.randint(20,80))
Q  = []
Q.append(str("P(A|B) = "+AB+"%. "))
Q.append(str("P(A) = "+A+"%. "))
Q.append(str("P(B) = "+B+"%. "))
random.shuffle(Q)
question = ""
for i in Q:
    question += i
question += "What is the value of P(A & B)? "
worksheet.pushQ(question)
answer = str(round(float(B)/100 * float(AB),2))+"%"
worksheet.pushA(answer)

#Question 6: P(A&B), P(B), Find P(A|B)
B = str(random.randint(40,90))
AB = str(random.randint(10,int(B)-20))
Q  = []
Q.append(str("P(B) = "+B+"%. "))
Q.append(str("P(A & B) = "+AB+"%. "))
random.shuffle(Q)
question = ""
for i in Q:
    question += i
question += "What is the value of P(A | B)? "
worksheet.pushQ(question)
answer = str(round(100*float(AB)/float(B),2))+"%"
worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder()
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
