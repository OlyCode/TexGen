# TexGen.py
# TeX Worksheet Generator
# Copyright 2020, Olympia Code LLC
# Author: Joseph Mortillaro
# Version 0.3.2.20
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from decimal import *
import sys
import random
import math


############################################################
####   Latex Header    #####################################
############################################################

latexHeader = """
\\documentclass[12pt]{article} 
\\usepackage[utf8]{inputenc} % set input encoding

%%% Examples of Article customizations
% These packages are optional, depending whether you want the features 
% they provide.
% See the LaTeX Companion or other references for full information.

%%% PAGE DIMENSIONS
\\usepackage{geometry} % to change the page dimensions
 \\geometry{letterpaper} % or letterpaper (US) or a5paper or....
 \\geometry{margin=1in} % change the margins to 1 inch all round
 \\geometry{portrait} % set up the page for landscape

\\setlength\parindent{0pt}

%\\usepackage{graphicx} % support the \includegraphics command and options
% \\usepackage[parfill]{parskip} % Activate to begin paragraphs with an 
% empty line rather than an indent

%%% PACKAGES
%\\usepackage{booktabs} % for much better looking tables
%\\usepackage{array} % for better arrays (eg matrices) in maths
%\\usepackage{paralist} % very flexible & customisable lists 
%                     %(eg. enumerate/itemize, etc.)
%\\usepackage{verbatim} % adds environment for commenting out blocks 
%                     % of text & for better verbatim
%\\usepackage{subfig} % make it possible to include more than one captioned 
%                   % figure/table
% These packages are all incorporated in the memoir class to one degree 
% or another...

\\begin{document}
%\\section{First section}
%\\subsection{A subsection}

\\begin{flushright}
Name: \\underline{\\hspace{2.5 in}}
\\end{flushright}
\\begin{flushright}
Worksheet ID: \\tgID{}
\\end{flushright}
\section*{"""



############################################################
####   Math Functions   ####################################
############################################################

def reduce(a):
#reduce the fraction
    x = 2
    while x <= a[0] or x <= a[1]:
        if a[0] % x == 0 and a[1] % x == 0:
            a[0] = a[0]/x
            a[1] = a[1]/x
            x=2
        x += 1
    return(a)

############################################################
####   Global Variables   ##################################
############################################################

g_addLatexHeader = False
#g_shuffleQuestions = False


############################################################
####   tex_gen Functions   #################################
############################################################

def findClose(a, b, s):
#string = findClose(open_sign, closing_sign, string)
#note: it leaves off the closing symbol
    x = 1
    for y in range(len(s)):
        if s[y] == a: x += 1
        if s[y] == b: x -= 1
        if x <= 0: 
            return s[:y]
    print "Error: Unclosed Section"
    return 0


############################################################
####   tex_gen Sections   ##################################
############################################################

def setup_function(inString):
    pass

def ID_function(inString, genCount):
# Takes care of \tgID{}
    outString = ""
    x = 0
    tString = "\\tgID{}"
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            outString += str(genCount)
            x += len(tString)
            continue
        else: 
            outString += inString[x]
            x += 1
    return outString

def loop_function(inString):
# Takes care of \lgLoop[times]{strig}
    outString = ""
    x = 0
    tString = "\\tgLoop["
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            temp1 = findClose('[',']',inString[x+len(tString):])
            temp2 = findClose('{','}', \
                        inString[x + len(tString) + len(temp1) + 2:])
            for y in range(int(temp1)):
                outString += temp2
            x += (len(tString) + len(temp1) + len(temp2) + 3)
        else: 
            outString += inString[x]
            x += 1
    return outString

def rand_function(inString):
# Takes care of \tgRand[type]{low,high}
    outString = ""
    x = 0
    tString = "\\tgRand["
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            temp1 = findClose('[',']',inString[x+len(tString):])
            temp2 = findClose('{','}', \
                        inString[x + len(tString) + len(temp1) + 2:])
            splitTemp = temp2.split(',')
            rStart = int(splitTemp[0])
            rEnd = int(splitTemp[1])
            if temp1 == 'n':
                outString += str(random.randint(rStart, rEnd))
            if temp1 == 'npm':
                rNum = random.randint(rStart, rEnd) * random.choice([-1,1])
                outString += str(rNum)
            x += (len(tString) + len(temp1) + len(temp2) + 3)
        else: 
            outString += inString[x]
            x += 1
    return outString

def var_function(inString):
    # Takes care of \tgSet[name]{value} and \tgV{name}
    varDict = dict()
    outString = ""
    x = 0
    sString = "\\tgSet["
    vString = "\\tgV{"
    while x < len(inString):
        #Test for sString   
        if inString[x:x+len(sString)] == sString:
            x0 = x
            temp1 = findClose('[',']',inString[x+len(sString):])
            temp2 = findClose('{','}', \
                    inString[x + len(sString) + len(temp1) + 2:])
            if '.' in temp2:
                varDict[temp1] = float(temp2)
            else:
                varDict[temp1] = int(temp2)
            x += (len(sString) + len(temp1) + len(temp2) + 3)
            if inString[x] == '\n' and inString[x0-1] == '\n':
                x += 1
            continue
        #Test for vString   
        if inString[x:x+len(vString)] == vString:
            temp = findClose('{','}', inString[x+len(vString):])
            outString += str(varDict[temp])
            x += (len(vString) + len(temp) + 1)
            continue
        else: 
            outString += inString[x]
            x += 1
    return outString

def keymaker_function(inString):
# answerKey = keymaker_function(inString)
# Takes care of \tgQ{} and \tgA{string}
    answerCount = 0
    answerKey = "\\vspace{1 in}Answer Key: \\\\"
    outString = ""
    x = 0
    qString = "\\tgQ{}"
    aString = "\\tgA{"
    while x < len(inString):
        #Test for qString   
        if inString[x:x+len(qString)] == qString:
            answerCount += 1
            outString += str(answerCount)
            x += len(qString)
            continue
        #Test for aString   
        elif inString[x:x+len(aString)] == aString:
            x0 = x
            temp = findClose('{','}', inString[x+len(aString):])
            answerKey += str(answerCount) + ')~' + temp + "\\\\"
            x += (len(aString) + len(temp) + 1)
            if inString[x] == '\n' and inString[x0-1] == '\n':
                x += 1
            continue
        else: 
            outString += inString[x]
            x += 1
    return [outString, answerKey[:]]

def shuffleQuestions_function(inString):
    # \tgShuffleQuestions starts the questions
    outString = ""
    tString = inString
    printAnswerKey = False
    if tString.find("\\tgShuffleQuestions{}") >= 0:
        if tString.find("\\tgKey{}") >= 0:
            printAnswerKey = True
            tString = tString.replace("\\tgKey{}", "")
        tList = tString.split("\\tgShuffleQuestions{}", 1)
        tList[1] = "\n" + tList[1] # ensures there is at least one newline
        qList = tList[1].split("\\tgQ{}")
        qList.pop(0) # gets rid of the newlines between \shuffle and \tgQ
        outString = tList[0]
        random.shuffle(qList)
        for x in qList:
            outString += "\\tgQ{}"
            outString += x
        if printAnswerKey:
            outString += "\n\\tgKey{}"
        return outString
    else:
        return inString

def printKey_function(inString, answerKey):
    outString = ""
    x = 0
    while x < len(inString):
        tString = "\\tgKey{}"
        if inString[x:x+len(tString)] == tString:
            outString += answerKey
            x += len(tString)
        else: 
            outString += inString[x]
            x += 1
    return outString

def printHeader_function(inString):
    global g_addLatexHeader
    x = 0
    outString = ""
    tString = "\\tgLatexHeader{"
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            outString += latexHeader
            g_addLatexHeader = True
            x += len(tString)
        else: 
            outString += inString[x]
            x += 1
    return outString

def early_eval_function(inString):
# Takes care of \tgEval{string}
    outString = ""
    x = 0
    tString = "\\tgEarlyEval{"
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            temp = findClose('{','}',inString[x+len(tString):])
            outString += str(eval(temp))
            x += (len(tString) + len(temp) + 1)
            continue
        else: 
            outString += inString[x]
            x += 1
    return outString

def eval_function(inString):
# Takes care of \tgEval{string}
    outString = ""
    x = 0
    tString = "\\tgEval{"
    while x < len(inString):
        if inString[x:x+len(tString)] == tString:
            temp = findClose('{','}',inString[x+len(tString):])
            outString += str(eval(temp))
            x += (len(tString) + len(temp) + 1)
            continue
        else: 
            outString += inString[x]
            x += 1
    return outString

def cleanup_function(inString):
    
    outString = inString.replace("+  -", "-")
    outString = outString.replace("+ -", "-")
    outString = outString.replace("+-", "-")
    outString = outString.replace("-  -", "+")
    outString = outString.replace("- -", "+")
    outString = outString.replace("--", "+")
    outString = outString.replace("+~~-", "-")
    outString = outString.replace("+~-", "-")
    outString = outString.replace("-~~-", "+")
    outString = outString.replace("-~-", "+")    
    outString = outString.replace("-  +", "-")
    outString = outString.replace("- +", "-")
    outString = outString.replace("-+", "-")
    outString = outString.replace("-~~+", "-")
    outString = outString.replace("-~+", "+")
    
    #for x in range(20):
    #    outString = outString.replace("\n  \n", "\n")
    #    outString = outString.replace("\n \n", "\n")
    ##    outString = outString.replace("\n\n", "\n")
    #    outString = outString.replace("\r\n  \r\n", "\r\n")
    #    outString = outString.replace("\r\n \r\n", "\r\n")
    #    outString = outString.replace("\r\n\r\n", "\r\n")
    return outString

def generate(inString, genCount):
    global g_addLatexHeader
    global g_shuffleQuestions
    
    answerKey = ""
    outString = ""
    
    outString = printHeader_function(inString)
    outString = ID_function(outString, genCount)
    outString = loop_function(outString)
    
    ##### Keeps questions together #####################
    #tString = "\\end{minipage}\\begin{minipage}{\\textwidth}\\tgQ{}"
    #outString = outString.replace("\\tgQ{}", tString)
    #outString = outString.replace(tString, "\\begin{minipage}{\\textwidth}\\tgQ{}", 1)
    #if outString.find("\\tgKey{}") >= 0:
    #    outString = outString.replace("\\tgKey{}", "\\end{minipage}\\tgKey{}")
    #else:
    #    outString =+ "\\end{minipage}"
    #####################################################
    
    outString = rand_function(outString)
    outString = var_function(outString)
    outString = early_eval_function(outString)
    outString = shuffleQuestions_function(outString)    
    [outString, answerKey] = keymaker_function(outString)
    outString = printKey_function(outString, answerKey)
    outString = eval_function(outString)
    outString = cleanup_function(outString)
    
    if g_addLatexHeader:
        outString += "\n\\end{document}"
    
    return outString

def main():
# "tex_gen.py" shoud generate help text
# "tex_gen.py -h" and "tex_gen.py -help"  shold generate help text.
# tex_gen.py [inputFilename] shoud parse inputFilename and send the 
#    processed text to the screen
# tex_gen.py inputFilename output Filename should parse inputshoud 
#    generate help text
# tex_gen.py shoud generate help text

    if len(sys.argv) <= 2: 
        print "Syntax: tex_gen.py [input filename] [output filename]"\
                + "[optional: number of versions]"
        return 0
    try:
        f = open(str(sys.argv[1]),'r')
    except IOError:
        return 0
    genCount = 1
    if len(sys.argv) > 3:
        genCount = int(sys.argv[3])
    startString = f.read()
    f.close()
    for x in range(1, genCount+1):
        textString = startString
        inName = str(sys.argv[1])
        outName = str(sys.argv[2])
        outNameDot = outName.rfind('.')
        if genCount == 1: 
            f = open(outName[:outNameDot] \
                + outName[outNameDot:],'w')
        else: 
            f = open(outName[:outNameDot] + "_" + str(x)\
                + outName[outNameDot:],'w')
        textString = generate(startString, x) 
        f.write(textString)
        f.close()   

main()
