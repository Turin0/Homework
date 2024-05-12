from pprint import pprint

file_name = 'Poem.txt'
file = open(file_name, mode='w', encoding='utf8')
file_content = ("# -*- coding: utf-8 -*- \nMy soul is dark - Oh! quickly string \nThe harp I yet can brook to hear; \n"
                "And let thy gentle fingers fling \nIts melting murmurs o'er mine ear. \n"
                "If in this heart a hope be dear, \nThat sound shall charm it forth again: \n"
                "If in these eyes there lurk a tear, \n'Twill flow, and cease to burn my brain. \n"
                "\nBut bid the strain be wild and deep, \nNor let thy notes of joy be first: \n"
                "I tell thee, minstrel, I must weep, \nOr else this heavy heart will burst; \n"
                "For it hath been by sorrow nursed, \nAnd ached in sleepless silence, long; \n"
                "And now 'tis doomed to know the worst, \nAnd break at once - or yield to song.")
file.write(file_content)
file.close()
pprint(file_content)