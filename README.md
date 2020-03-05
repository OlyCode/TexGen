TeX_Gen
=======

A LaTeX pre-processor for the making of math worksheets.

.tg files are compiled into multiple .tex files
by TexGen, which are then converted to .pdf by a LaTeX 
complier.


Markup Commands
---------------

* To set a value

		\tgSet[name]{value}

* To get a random number:
  types: n = integer, f = fraction, d = decimil

		\tgRand[type]{low,high}

* To get a print formated variable:
  This is for fractions.

		\tgP{name}

* To use a variable.

		\tgV{name}

* To start a quesiton (the name parameter is optional).

		\tgQ{name} 

* To record an answer that goes with a question.

		\tgA{string}

* To set up a loop.

		\tgLoop[times]{strig}

* To evaluate a string:

		\tgEval{string}

* To insert the answer key:

		\tgKey{}

* To insert the ID number:

		\tgID{}

* To inculde a Latex header:

        \tgLatexHeader{}

Examples
--------

To print a problem 10 times, then print an answer key.

	\tgLoop[10]{
	\tgSet[a]{\tgRand{10,100}}
	\tgSet[b]{\tgRand{10,100}}
	\tgQ{}. $\tgV{a} + \tgV{b}$ = ???
	\tgA{\tgEval{\tgV{a} + \tgV{b}}}
	}

	\tgKey{}
