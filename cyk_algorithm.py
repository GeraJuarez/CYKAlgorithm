
# Initialize data structures
CFG = {}    # Context Free Grammar
CYK = []    # CYK Matrix

def print_matrix( cyk ):
    for row in cyk:
        print " ".join( row )

def populate_matrix( cyk ):
    word = raw_input("Insert string to verify whether it belongs to the CFG: ")
    for i in range( len(word) ):
        cyk.append( ["-"] * len(word) )

def print_grammar( cfg ):
    print "==========\n"
    for k in cfg.keys():
        print k + " -> " + "|".join (cfg[k] )
    print "\n=========="

n = raw_input("Insert number of Non-terminal Symbols of the CFG: ")
print
for i in range ( int(n) ):
    print "---Symbol %s---\n" % str(i + 1)
    x = raw_input('Insert Initial symbol ( >[X]< -> Y ): ')
    y = raw_input('\nInsert the productions of that symbol ( X -> >[Y1]|[Y2]< ): ')
    y.replace(" ", "")
    CFG[x] = y.split("|")

print_grammar( CFG )
populate_matrix( CYK )
print_matrix( CYK )

