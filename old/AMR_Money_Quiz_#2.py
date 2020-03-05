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
        print p[:-4] # crops out the last ",   "
            

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

worksheet = WorksheetClass("Exponential Growth & Decay Quiz")

def worldPop(t):  # y = t + 1950
    t = tim


1. In 2009, the world population was 6.8 billion. The exponential growth rate was 1.13%
per year. Estimate the population of the world in 2012 and 2020, and find when the
world population will be 8 billion.
2. U.S. Exports increased from $12 billion in 1950 to $1550 billion (1.55 trillion) in 2009.
Assuming the export growth rate is an exponential function, find the growth rate, and
use it to estimate the value of exports in 1972 and 2015.
3. The number of farms in the U.S. has decreased exponentially since 1950. In 1950 there
were 5.6 million farms, and in 2008 that number was 2.2 million. At this decay rate,
when will there be only 1 million farms in the U.S.?

#Question Set 1-4: Finding toal.
for COUNT_TEMP0 in range(2):
    timeList = [["daily",365], ["yearly",1], ["annually",1], ["monthly",12]]
    random.shuffle(timeList)
    temp = [["You invest some money. ","investment","have"],\
            ["You take out a loan. ","loan","owe"],\
            ["You take out a loan. ","loan","owe"],\
            ["You open a savings account. ","investment","have"]]
    for COUNT_TEMP in range(4):
        c = COUNT_TEMP
        p = str(float(random.randint(100, 1000))/float(100))
        r = str(float(p)/float(100))
        P = str(random.randint(10,18)*100)
        y = str(random.randint(19000,18)*100)
        t = str(random.randint(3,10))
        I = str(int(P)*float(r)*int(t))
        T = str(float(I)+int(P))
        nName = timeList[c][0]

        questionSet = []
        questionSet.append("The annual interest rate is "+p+"%. ")
        questionSet.append("The interest is compound "+nName+". ")
        questionSet.append("The initial "+temp[c][1]+" was $"+P+". ")
        random.shuffle(questionSet)

        question = temp[c][0]
        for i in questionSet:
            question += i
        question += "How much money will you "+temp[c][2]+" "
        question += "after "+t+" years?"
        worksheet.pushQ(question)
                           
        answer = "$"+str(int(P)*(1+float(r)/int(n))**(int(t)*int(n)))
        worksheet.pushA(answer)

#Worksheet Layout
worksheet.shuffleOrder()
worksheet.printTitle()
worksheet.printQuestions()
print "KEY:"
worksheet.printAnswers()
