
""" Initialize data structures """
CFG = {}    # Context Free Grammar
CYK = []    # CYK Matrix

""" Auxiliar Methods """
def print_matrix( cyk ):
    """ Print current state of the Matrix """
    for row in cyk:
        print row
    print "=" * 20

def populate_matrix( cyk, w ):
    """ Initialize Matrix """
    for i in range( len(w) ):
        cyk.append( ["0"] * len(w) )

def print_grammar( cfg ):
    """ Visualize the Grammar defined by the user """
    print "==========\n"
    for k in cfg.keys():
        print k + " -> " + "|".join (cfg[k] )
    print "\n========= ="

def in_grammar( letter ):
    """ Check whether the letter can be obtained by a non terminal symbol """
    temp = []
    for k in CFG.keys():
        if letter in CFG[k]:
            temp.append(k)
    return temp

def cyk_algorithm_step1( word, cyk ):
    """ Check each character of the string if it can be produced by the CFG """
    i = j = 0
    for c in word:
        non_term_symbols = in_grammar(c)
        if non_term_symbols:
            cyk[i][j] = non_term_symbols
        else:
            cyk[i][j] = []
        i, j = i + 1, j + 1

def cyk_algorithm( word, cyk ):
    cyk_algorithm_step1( word, cyk )
    # Iterate over matrix
    tempList = []
    for k in range(1, len(word) ):
        print_matrix( cyk )
        i = j = 0
        tempList = []
        while j < len(word) - 1:
            if j + 1 == len(word) - 1:
                tempList = []
            if j == k + i:
                i += 1
                j = i
            for m in cyk[i][j]:
                for n in cyk[j + 1][k + i]:
                    posible_symbols = in_grammar( m + n )
                    #print "Ps: "
                    #print posible_symbols
                    tempList = list( set(tempList) | set(posible_symbols) )
                    #print "temp: "
                    #print tempList
                    #print "insert cyk"
                    if posible_symbols:
                        cyk[i][k + i] = tempList
            j += 1

""" Main """
n = raw_input("Insert number of Non-terminal Symbols of the CFG: ")
print
for i in range ( int(n) ):
    print "---Symbol %s---\n" % str(i + 1)
    x = raw_input('Insert Initial symbol ( >[X]< -> Y ): ')
    y = raw_input('\nInsert the productions of that symbol ( X -> >[Y1]|[Y2]< ): ')
    y.replace(" ", "")
    CFG[x] = y.split("|")

print_grammar( CFG )
word = raw_input("Insert string to verify whether it belongs to the CFG: ")
populate_matrix( CYK, word )
cyk_algorithm( word, CYK )
print_matrix( CYK )


