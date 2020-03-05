# -*- coding: cp1252 -*-
#AMR 1st Semester Final

import random
Q = [] #q = ["question","possible answers","correct answer"]

Q.append([]) #1
Q[-1].append("A die is rolled and a coin is flipped simultaneously. The number rolled on the die and whether the coin lands heads or tails is recorded. How many outcomes are possible?")
Q[-1].append("    A)  8    B)  6    C)  10    D)  12")
Q[-1].append("D")

Q.append([]) #2
Q[-1].append("Two coins are flipped at the same time and it is recorded whether each coin lands heads or tails.  The possible outcomes for this are:")
Q[-1].append("    A)  {H, T}.    B)  {HH, HT, TT}.    C)  {HH, HT, TH, TT}.    D)  {H, H, T, T}.")
Q[-1].append("C")

Q.append([]) #3
Q[-1].append("A spinner numbered 1 through 10 is spun and one die is tossed simultaneously.  The number spun and the number rolled are recorded.  How many outcomes are possible?")
Q[-1].append("    A)  60    B)  16    C)  10    D)  6")
Q[-1].append("A")

Q.append([]) #4
Q[-1].append("A spinner numbered 1 through 10 is spun and one die is rolled simultaneously.  The sum of the number spun and the number rolled is recorded.  How many outcomes are possible?")
Q[-1].append("    A)  60    B)  16    C)  15    D)  10")  
Q[-1].append("C")

Q.append([]) #5
Q[-1].append("Three dice are tossed.  The number rolled on each die is recorded.  How many different outcomes are possible?")
Q[-1].append("    A)  18    B)  72    C)  216    D)  42")
Q[-1].append("C")

Q.append([]) #6
Q[-1].append("Three dice are tossed.  The sum of the numbers rolled is recorded.  How many outcomes are possible?")
Q[-1].append("    A)  18    B)  12    C)  16    D)  72") 
Q[-1].append("C")

Q.append([]) #7
Q[-1].append("Three dice are rolled and the number rolled on each die is recorded.  The outcomes in the possible outcomes are all equally likely.")
Q[-1].append("    A)  True    B)  False")
Q[-1].append("A")

Q.append([]) #8
Q[-1].append("Three dice are rolled and the sum of the numbers rolled is recorded.  The outcomes in the possible outcomes are all equally likely.") 
Q[-1].append("    A)  True    B)  False")
Q[-1].append("B")

Q.append([]) #9
Q[-1].append("Two coins are flipped and the number that landed on heads is recorded.  The outcomes in the possible outcomes are all equally likely.")
Q[-1].append("    A)  True    B)  False")
Q[-1].append("B")

Q.append([]) #10
Q[-1].append("Two coins are flipped and whether each one landed heads or tails is recorded.  The outcomes  in the possible outcomes are all equally likely.")
Q[-1].append("    A)  True    B)  False")
Q[-1].append("A")

Q.append([]) #11
Q[-1].append("There are seven blue and six black socks in a drawer. One is pulled out at random. Find the probability that it is black.")
Q[-1].append("    A)  6/13    B)  6/7    C)  1/2    D)  1/6")
Q[-1].append("A")

Q.append([]) #12
Q[-1].append("Two fair dice are rolled and the sum rolled is recorded.  Find the probability that the sum is 4.")
Q[-1].append("    A)  1/3    B)  1/12    C)  4/11    D)  1/9")
Q[-1].append("B")

Q.append([]) #13
Q[-1].append("A fair coin is tossed three times.  Find the probability of getting exactly two heads.")
Q[-1].append("    A)  1/2    B)  1/3    C)  2/3    D)  3/8")
Q[-1].append("D")

Q.append([]) #14
Q[-1].append("If a fair die is rolled once, what is the probability of getting a number less than five?")
Q[-1].append("    A)  1/6    B)  1/2    C)  2/3    D)  5/6")
Q[-1].append("C")

Q.append([]) #15
Q[-1].append("A computer is programmed to randomly print two letters in a row without repeating a letter.  What is the probability that the first combination printed is the word \"DO\"?")
Q[-1].append("    A)  1/650    B)  1/325    C)  2/325    D)  1/26")
Q[-1].append("A")

Q.append([]) #21
Q[-1].append("Either Terry, Chris, or Kim will attend a party.  The probability Terry attends is 0.31 and the probability Chris attends is 0.5.  What is the probability that Kim attends?")
Q[-1].append("    A)  0.33    B)  0.5    C)  0.81    D)  0.19")
Q[-1].append("D")

Q.append([]) #22
Q[-1].append("If there is a 0.8 probability of rain today, what is the probability it will not rain?")
Q[-1].append("    A)  0.8    B)  0.5    C)  0.2    D)  0.1")
Q[-1].append("C")

Q.append([]) #23
Q[-1].append("A possible outcomes has three outcomes, A, B, and C.  The probability of outcome A is 0.39 and the probability of outcome B is 0.25.  What is the probability of outcome C?")
Q[-1].append("    A)  0.36    B)  0.33    C)  0.5    D)  0.64")
Q[-1].append("A")

Q.append([]) #26
Q[-1].append("A raffle ticket costs $5.  First and second prize winners will be drawn at random.  The probability of winning the $100 first prize is 1/40 and the probability of winning the $25 second prize is 1/20.  What is the expected value for one play, taking into account the $5 cost of the ticket?")
Q[-1].append("    A)  –1.25    B)  –0.875    C)  3.375    D)  3.75")
Q[-1].append("A")

Q.append([]) #27
Q[-1].append("Suppose a game has three outcomes, A, B, and C with probabilities P(A) = 0.2, P(B) = 0.3, and P(C) = 0 .5.  A player will receive $3 when outcome A occurs, $4 when outcome B occurs, and will have to pay $2 when outcome C occurs.  What is the expected value of one trial of the game?")
Q[-1].append("    A)  0.80    B)  1.66    C)  1.00    D)  5.00")
Q[-1].append("A")

Q.append([]) #29
Q[-1].append("A fair die is rolled.  If a number 1 or 2 appears, you will receive $5.  If any other number appears, you will pay $2.  What is the expected value of one trial of this game?")
Q[-1].append("    A)  $1/3    B)  $3    C)  $3/2    D)  –$3")
Q[-1].append("A")

Q.append([]) #52
Q[-1].append("You are told that an event is nearly impossible; it will occur only once in a long sequence of trials. Which of the following probabilities could describe this event?")
Q[-1].append("    A)  0    B)  .02    C)  .98    D)  1")
Q[-1].append("B")

Q.append([]) #53
Q[-1].append("A game is played with a pair of tetrahedral (four-sided) dice. Each die has faces numbered 1, 2, 3, and 4. To play, roll the two dice and record the sum of the values on the down faces. What is the probability of rolling a sum of 6?")
Q[-1].append("    A)  1/2    B)  1/8    C)  3/8    D)  3/16")
Q[-1].append("D")

Q.append([]) #56
Q[-1].append("A game consists of rolling a regular die. You pay $5 to play the game, and the $5 is not returned. If you roll a 1 or 2, you win $6. If you roll a 3, 4, 5, or 6, you win nothing. What is the expected value for this game, taking into account the $5 cost of the game?")
Q[-1].append("    A)  –$5    B)  –$3    C)  $1    D)  $3")
Q[-1].append("B")

def r(q):
    # Shuffles Answers
    aNames = ["","A","B","C","D","E","F","G"]
    # Splits old answers.
    T = q[1].split(")")
    for n in range(len(T)-1):
        T[n] = T[n][:-1]
    T[-1] = T[-1]+"   "
    # Gets correct answer.
    ca = T[aNames.index(q[2])]
    # Shuffles old answers and puts them back together
    a = T.pop(0)
    random.shuffle(T)
    for n in range(len(T)):
        a += aNames[n+1]+")"+T[n]
    return [a,ca]

random.shuffle(Q)
K = []
for x in range(len(Q)):
    print str(x+1)+".    ",
    print Q[x][0]
    print ""
    t = r(Q[x])
    print t[0]
    K.append(t[1])
    print ""

print "Answer Key:"
for x in range(len(Q)):
    print str(x+1) + ")  " + K[x] + ",",
