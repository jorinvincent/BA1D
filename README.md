The first - https://www.gradescope.com/courses/358896/assignments/1796869 (Links to an external site.) - asks you to find a short string within a longer string.  The input file is called "input" (no .txt following the name, and you can assume it's found in the same folder where the program is executed, i.e., "./input").

The input file will contain the string you are searching (the query) on the first line, then the following lines contain the "text" you are searching against.  You must find the starting point of all locations in the text where the query matches exactly. The numbering starts at 0.

If the input is:

ATAT

ATATCAGT

the output should be 0 as the query matches at the beginning of the text.

If the input is:

ATAT

GATATCTATATG

the output should be "1 7" as the query matches at positions 1 and 7.

For more details, please see problem 1D in the textbook and http://rosalind.info/problems/ba1d/ (Links to an external site.) .

IMPORTANT: For this assignment you may not use programming language constructs that match strings (such as regular expressions String.find(), .match(), etc.). You must compare the strings character by character.  This is important as it prepares you for next week's material.
