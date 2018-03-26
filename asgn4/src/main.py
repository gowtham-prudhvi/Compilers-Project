class SymbolTable():
    """docstring for ClassName"""
    def __init__(self):
        self.table={}
        self.tempcount=0        

    def insert(self,varname,vartype):
        self.table[varname]=vartype

    def lookup(self,varname):
        if varname in self.table:
            return self.table[varname]
        else:
            return None

    def newtemp(self):
        tempname="t"+str(self.tempcount)
        self.table[tempname]="int"
        self.tempcount+=1
        return tempname

class SDT():
    def __init__(self):
        self.code=""
        self.place=None

class Instruction3AC:
    def __init__(self,typ,op,out,in1,in2,target):
        self.typ=typ
        self.op=op
        self.out=out
        self.in1=in1
        self.in2=in2
        self.target=target

def Print3AC(TAClist,output_location):
    fp=open(output_location,'w')
    for i in range(len(TAClist)):
        currline=[]
        lineno=str(i+1)
        currline.append(lineno)
        if TAClist[i].typ is not None:
            if TAClist[i].typ in ["ifgoto","goto"]:
                TAClist[i].target=str(TAClist[i].target+i+1)
            currline.append(TAClist[i].typ)
        if TAClist[i].op is not None:
            currline.append(TAClist[i].op)
        if TAClist[i].out is not None:
            currline.append(TAClist[i].out)
        if TAClist[i].in1 is not None:
            currline.append(TAClist[i].in1)
        if TAClist[i].in2 is not None:
            currline.append(TAClist[i].in2)
        if TAClist[i].target is not None:
            currline.append(TAClist[i].target)
        if i == len(TAClist)-1:
            fp.write(",".join(currline))
        else:
            fp.write(",".join(currline)+"\n")
    fp.close()

def getRule(p,node_name):
    pass