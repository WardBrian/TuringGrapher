# Returns a dictionary which has keys of form (state, state) and values of form
# (input_symbols, output_symbols, direction)
def make_state_dict(filename):
    f = open(filename + '.tm', 'r')
    d = {}
    for line in f:
        seq = line.split()
        #print seq
        if (len(seq) > 0) and (seq[0][0] != '#'):

            state = int(seq[0])
            sym = seq[1]
            if sym == 'B':
                sym = "&#9633;"  # a square character
            newstate = int(seq[2])
            newsym = seq[3]
            direction = seq[4]
            if newsym == 'B':
                newsym = "&#9633;"
            k = (state, newstate)
            if k in d:
                cur = tuple(d[k])
                if (cur[0] != sym):
                    sym = cur[0] + ', ' + sym
                if not (cur[1] == newsym):
                    newsym = cur[1] + ', ' + newsym
                if not (cur[2] == direction):
                    direction = cur[2] + ', ' + direction
            d[k] = (sym, newsym, direction)
    f.close()
    return d


# Make a DOT file from the specified TM simulator file
def generate_graph(filename):
    d = make_state_dict(filename)
    f = open(filename + '.gv', 'w')
    f.write('digraph G { \n\tgraph [ dpi = 300 ];\n')

    for key in d:
        state = str(key[0])
        newstate = str(key[1])
        if newstate == '-1':
            newstate = 'Accept'
        if newstate == '-2':
            newstate = 'Reject'
        if newstate == '-3':
            newstate = 'Halt'
        val = d[key]
        sym = str(val[0])
        newsym = str(val[1])
        direction = val[2]
        comma = ', '
        if newsym == sym:
            newsym = ''
            comma = ''
        f.write('\t' + state + ' -> ' + newstate + " [label = < " + sym +
                " &#8594; " +  # rightarrow character
                newsym + comma + direction + ">]; \n")
    f.write('}')
    f.close()
