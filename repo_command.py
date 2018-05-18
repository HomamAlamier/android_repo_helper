#import test.py : the code added here
import os

# Welcome Message
print('Welcome to python repo script')
print('You can get some help by typing help :)')
# print('If you are done with script please type exit and did not close the terminal window')
print('Thank You!')
global isLineage
isLineage=os.path.isfile('manifests/snippets/lineage.xml')
if isLineage==True:
    print('Note : you are syncing LineageOS sources :)')
cmd1=''
cmd=''
# add command in here by putting ,'commnad here'
commands=['repo info','python ver','help','exit']
# add command comment in here by putting ,'comment here'
commands_commints=['Get downloaded files informations.','This command show the python version should run this script.','Display this :).','Exit and save data']

# Functions
def getrepoinfo(isPrinted,wasDown):
    global count
    f=open("manifests/default.xml",'r')
    lst=list()
    i=0
    # Make a list of the directorys from manifest.xml
    for lin in f:
            isstart=lin.startswith('  <project')
            if isstart:
                i=i+1
                src=lin.find("path")
                sl=lin.find('"',src)
                sl=sl+1
                st=lin.find("/",src)
                p=lin[sl:st]
                sf=lin.find('"',st)
                st=st+1
                p1=lin[sl:sf]
                p1="projects/"+p1+'.git'
                lst.append(p1)
    f.close()
    
    if isLineage==True:
            f=open("manifests/snippets/lineage.xml",'r')
            i=0
            # Make a list of the directorys from manifests/snippets/lineage.xml
            for lin in f:
                    isstart=lin.startswith('  <project')
                    if isstart:
                        i=i+1
                        src=lin.find("path")
                        sl=lin.find('"',src)
                        sl=sl+1
                        st=lin.find("/",src)
                        p=lin[sl:st]
                        sf=lin.find('"',st)
                        st=st+1
                        p1=lin[sl:sf]
                        p1="projects/"+p1+'.git'
                        lst.append(p1)
                        
                        
    m=len(lst)
    # Chack what is exist or not and print info
    count=0
    for z in lst:
            isdr=os.path.isdir(z)
            if isdr:
                count=count+1
    reman=m-count
#    return count
    if isPrinted==True:
        print("total objects :",m)
        if wasDown==0 :
            print("objects downloaded :",count)
        else:
            print("objects downloaded :",count,'(Was',wasDown+')')
        print("Remaning :",reman)

def getlastchange():
    global lastdown
    f=open("last.dat",'r')
    x=f.read()
    lastdown=x
def gethelp():
#    print('commands list')
    z=0
    for i in commands:
        print(i,'   ',commands_commints[z])
        z=z+1

def savedata():
    # save last change data
    lastchangefile=open("last.dat",'w')
    getrepoinfo(False,0)
    lastchangefile.write(str(count))
    lastchangefile.close()
    
# Main
while True:
    cmd=input('>')
    if cmd=='':
        print("please type a command. for help use command help ")
    elif cmd!='':
        found=0
        for i in commands:
            if cmd==i:
                found=1
                if cmd=='repo info':
                    getlastchange()
                    getrepoinfo(True,lastdown)
                if cmd=='python ver':
                    print("This py file runs only on python3 and newer")
                if cmd=='help':
                    gethelp()
                if cmd=='exit':
                    print('exiting...')
                    break
    if found==0:
        print(cmd,"not found")
    if cmd=='exit':
        savedata()
        break
        
        
