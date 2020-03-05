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

worksheet = WorksheetClass("Simple Interest Quiz")

for COUNT_TEMP in range(2):

    #Question 1: Finding interest.
    p = str(float(random.randint(100, 500))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(10,80)*100)
    t = str(random.randint(2,7))
    I = str(int(P)*float(r)*int(t))
    T = str(float(I)+int(P))
    question  = "A bank is offering "+p+"% simple interest on a "
    question += "savings account. If you deposit $"+P+", how much "
    question += "interest will you earn in "+t+" years?"
    worksheet.pushQ(question)
    answer = "$"+str(int(P)*float(r)*int(t))
    worksheet.pushA(answer)

    #Question 2: Finding total
    p = str(float(random.randint(500, 1000))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(80,170)*100)
    t = str(random.randint(3,5))
    I = str(int(P)*float(r)*int(t))
    T = str(float(I)+int(P))
    question  = "To buy a car, you borrow $"+P+" for "+t+" years "
    question += "at an annual simple interest rate of "+p+"%. "
    question += "If you pay the entire loan off "
    question += "at the end of "+t+" years? What is the total amount "
    question += "that you will have paid?"
    worksheet.pushQ(question)
    answer = "$"+str(int(P) + int(P)*float(r)*int(t))
    worksheet.pushA(answer)

    #Question 3: Finding time
    p = str(float(random.randint(500, 1000))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(80,170)*100)
    t = str(random.randint(2,10))
    I = str(int(P)*float(r)*int(t))
    T = str(float(I)+int(P))
    question  = "You invest $"+P+" in a bond at a yearly rate of "+p+"%. "
    question += "You earn $"+I+" in interest. How long was the money invested?"
    worksheet.pushQ(question)
    answer  = str(int(t)) +" years"
    worksheet.pushA(answer)

    #Question 4: Finding rate
    p = str(float(random.randint(500, 1000))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(80,170)*100)
    t = str(random.randint(2,10))
    I = str(int(P)*float(r)*int(t))
    T = str(float(I)+int(P))
    question  = "You borrow $"+P+" for "+t+" years to make home improvements. "
    question += "If you repaid a TOTAL amount of $"+T+", at what interest "
    question += "rate did you borrow the money?"
    worksheet.pushQ(question)
    answer  = str(float(p))+"%"
    worksheet.pushA(answer)

    #Question 5: Finding rate
    p = str(float(random.randint(500, 1000))/float(100))
    r = str(float(p)/float(100))
    P = str(random.randint(80,170)*100)
    t = str(random.randint(2,10))
    I = str(int(P)*float(r)*int(t))
    T = str(float(I)+int(P))
    question  = "You invest $"+P+" for "+t+" years. After "+t+" years "
    question += "you have made a total of $"+I+" in interst, at what interest "
    question += "rate did you invest?"
    worksheet.pushQ(question)
    answer  = str(int(t)) +"%"
    worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder()
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
