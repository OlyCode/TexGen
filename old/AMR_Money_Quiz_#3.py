#AMR Probability Quiz #1
#Python Genearated Quiz Ver. 4 (12/5/2014)

############################################################
#### Code ##################################################
############################################################

import random
import itertools
import math

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

worksheet = WorksheetClass("Continuously Compounding Interest Quiz 1")

detailList = [["You invest some money. ","investment","have"],\
            ["You borrow some money. ","loan","owe"],\
            ["You take out a loan. ","loan","owe"],\
            ["You open a savings account. ","investment","have"]]
random.shuffle(detailList)

for COUNT_TEMP in range(4):

    #Question 1: Finding total.
    d = detailList.pop()
    p = str(float(random.randint(100, 1000))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(10,300)*100)
    t = str(random.randint(3,30))
    T = str(float(P)*float(math.exp(float(r)*float(t))))
    I = float(T)-float(P)

    questionSet = []
    questionSet.append("The interest is compounded continuously. ")
    questionSet.append("The initial "+d[1]+" was $"+P+". ")
    questionSet.append("The annual interest rate is "+p+"%. ")
    random.shuffle(questionSet)
    question = d[0]
    for i in questionSet:
        question += i
    question += "How much money will you "+d[2]+" "
    question += "after "+t+" years?"
    worksheet.pushQ(question)

    answer = "$"+str(T)
    answer = str(answer.split(".")[0]+"."+answer.split(".")[1][:2])
    worksheet.pushA(answer)

#Question 5: Finding total.
d = ["You buy a car. ","value"]
p = str(float(random.randint(100, 1000))/float(100))
r = str(float(p)/float(100))
P = str(random.randint(10,300)*100)
t = str(random.randint(3,30))
T = str(float(P)*float(math.exp(-float(r)*float(t))))
I = float(T)-float(P)

questionSet = []
questionSet.append("The car is losing value continuously. ")
questionSet.append("The initial "+d[1]+" was $"+P+". ")
questionSet.append("The car loses "+p+"% of its value every year. ")
random.shuffle(questionSet)
question = d[0]
for i in questionSet:
    question += i
question += "How much money will your car e worth "
question += "after "+t+" years?"
worksheet.pushQ(question)

answer = "$"+str(T)
answer = str(answer.split(".")[0]+"."+answer.split(".")[1][:2])
worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder()
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
