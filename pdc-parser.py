#!/bin/python
import sys

def toHex(content):
    print(' '.join(hex(x) for x in content))

filename=sys.argv[1]
print("File:\t\t%s" %sys.argv[1])
content = open(filename,'rb').read()

magicWord=content[0:4].decode('utf-8')
print("Magic Word:\t%s" %magicWord)
if magicWord!='PDCI':
    print('not a pdc file')
    exit(1)
content=content[4:]

sequenceSize=int.from_bytes(content[0:4],byteorder='little')
content=content[4:]
if sequenceSize!=len(content):
    print('file size doesn\'t match')
    exit(1)

version=content[0]
content=content[1:]
print('Version:\t%d' %version)

reserved=content[0]
content=content[1:]
print('Reserved field:\t%d' %reserved)
if reserved!=0:
    print('no reserved field')

width=int.from_bytes(content[0:2],byteorder='little')
content=content[2:]
print('Width:\t%d' %width)

height=int.from_bytes(content[0:2],byteorder='little')
content=content[2:]
print('Height:\t%d' %height)

numberOfCommands=int.from_bytes(content[0:2],byteorder='little')
content=content[2:]
print('Number of commands:\t%d' %numberOfCommands)

for i in range(0,numberOfCommands):
    print("Command %d" %i)
    drawCommandType=content[0]
    content=content[1:]
    print("\tType:\t%d" %drawCommandType)
    if drawCommandType>3:
        print('invaild type')
        exit(0)

    flags=content[0]
    content=content[1:]
    print("\tFlags:\t%s" %bin(flags))
    print("\tHidden:\t%r" %(flags>>7==1))

    strokeColor=content[0]
    content=content[1:]
    print("\tStroke color:\t%s" %bin(strokeColor))

    strokeWidth=content[0]
    content=content[1:]
    print("\tStroke width:\t%d" %strokeWidth)

    fillColor=content[0]
    content=content[1:]
    print("\tFill color:\t%s" %bin(fillColor))

    if drawCommandType==1 or drawCommandType==3:
        pathOpen=int.from_bytes(content[0:2],byteorder='little')
        content=content[2:]
        print("\tPath open:\t%r" %(pathOpen>>7==1))
    elif drawCommandType==2:
        radius=int.from_bytes(content[0:2],byteorder='little')
        content=content[2:]
        print("\tRadius:\t%d" %radius)
    numberOfPoints=int.from_bytes(content[0:2],byteorder='little')
    content=content[2:]
    print("\tNumber of points:\t%d" %numberOfPoints)
    for j in range(0,numberOfPoints):
        print("\t\tPoint:\t%d %d %d %d" %(content[0],content[1],content[2],content[3]))
        content=content[4:]
