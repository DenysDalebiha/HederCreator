import ModulTable as M

readTable = open(r"data.csv", "r")                                           # it's own date for fiscal
writeTable = open(r"OutData.txt", "w")


def createScript(pos):
    line = pos.pop(0).replace(" ","").replace("AT","АТ").replace("CП","СП")
    length: int = M.size(line)
    writeTable.write('%Oper($$Data,"'+line+'",10,$$Flag)\n')                 # generate string for the writing ZN
    writeTable.write('%If ($$Flag == 1)\n%Then\n')
    writeTable.write('%Set $$FN = "'+pos.pop(0).replace('?', '')+'"\n')      # generate string for the writing FN
    line= None
    count: int = 0 
    while pos:                                                               # It's main loop for creating the recipt header
        if M.checkMarkers(pos[0]):
            if line == None:
                line = pos.pop(0).lstrip().center(length)#
            else:
                line = line.center(length)
        else:                                                                # this or previous string don't have the markers
            if line == None:
                line = pos.pop(0).lstrip()
            elif len(line)+len(pos[0]) < length:
                line += ' ' + pos.pop(0).lstrip()
            elif len(line)+len(pos[0]) >= length:
                line = line.center(length)
        if len(pos) == 0:
            print("last line")
            line = line.center(length)
        print(str(len(line)) + ' VS ' + str(length))
        print(str(len(line))+':' +line)
        if len(line) == length:                                              # writing the header in to the file
            writeTable.write('22000000;'+str(count)+';'+line.rstrip()+';0;\n')
            print("write table")
            count += 1
            line = None

for data in readTable:
    print("data in file")
    t = data.replace('"""', '"').replace('""', '"').replace('«', '"').replace('»', '"').replace('’', '\'').replace('\n', '')  
    t = t.replace(',', ',roz').replace(';;', 'roz').replace(';;', 'roz').replace(';"', 'roz').replace(' ";','roz').replace(';', 'roz')
    t = t.split('roz')                                                       # convert and split date 
    createScript(t)
    writeTable.write('%Else\n%EndIf\n\n')

readTable.close()
writeTable.close()

