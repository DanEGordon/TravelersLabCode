# TravelersLabCode
Scripts I wrote working for the Travelers Lab at Wesleyan University, 
which uses modern data analysis techniques to analyze medieval documents

Written in Python 2

The code in praticular looks at the Cely Letter Collection, a collection of 
150 letters discussing trade from the Cely merchant family.  The lab was focused
on figuring out how temporality and distance effected the letters.  How quickly
could the message of a letter reach someone?  To answer this, the code built
an individual profile of time and travel related words for each letter, to potentially
flag them as containing useful information.  Furthermore, it collected some statistics
on the collection as a whole.

The letters are written in middle english when there was no standardised spelling,
making it difficult to find praticular words.  Edit distance was explored, but there were
too many variations and similarities to other words for it to be effective.  Thus, a few other
strategies were used.  If a spellig had a portion of the word that was unique enough (The
SEPT of september for instance), that could be looked for.  If there are words around the word
being looked for that are consistent (The __ day of ___) then that structure could be looked 
for. In the worst case, each individual spelling needed to be catalogued and tracked.  Such a
system wasn't perfect, but served for what the head of the lab wanted.

Works on a folder where each Cely letter is an individual text file
The results of the program are in the results document

Plans were made to expand the program to other, larger ketter coolections, such as the
Paston collection, but I personally didn't work on that project.
