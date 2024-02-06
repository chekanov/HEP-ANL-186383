#  Create unique multiplicity topologies with boundary conditions. 
#  Then create tuples with 2-body kinematic variations  
#  S.V.Chekanov (ANL) 
#
#  Notations:
#  M: MET (0,1) 
#  j,b: light-flavour jets or b-jets 
#  e,m,t: electrons, muons, taus 
#  p: photons 

import sys

if ((sys.version).find("3.")<0):
         print("Need python3. Exit")
         sys.exit()

 
# return list with 2-body kinematic variations 
def getKinematics( com ):
        newlists=[]
        mlist = list(com)
        mlist.sort()
        orglist=mlist.copy() 
        print("Original=",mlist)
        for o1 in range(1,len(orglist)-1):
                 mlist=orglist.copy()
                 print("remove postion=",o1)
                 p1=orglist[o1]
                 mlist.pop(o1) # remove element  
                 print("after removal=",mlist)
                 modlist=[]
                 for o2 in range(1,len( mlist )):
                    print ("Add ",p1," at postion",o2)
                    savelist=mlist.copy()
                    savelist[o2]=p1+mlist[o2]
                    if (p1>mlist[o2]): # always sort in combinations 
                                savelist[o2]=mlist[o2]+p1
                    savelist.sort()
                    #modlist.append(savelist)
                    newlists.append(savelist)
                 #print("New modlist=",modlist)
                 #newlists.append(modlist)

        newlists.sort()

        # remove duplicates
        xdic={} 
        withoudup=[]
        for x in newlists:
              key = tuple(x)  
              print(key)
              if key in xdic:
                 print("Already seen") 
                 continue
              else:
                 xdic[key]=1
                 withoudup.append(x)

        # unwrap all configurations to a normal list
        #print("New kinematics postions=",newlists)
        print("Without dup=",withoudup)

        return withoudup; 


#com=["M","j","j","b","e"]
#com=["M","j","b","e"]
#xlist=getKinematics(com)
#print(len(xlist))
#sys.exit()




# Remove "M" since it is not relevent for merging
import itertools
j=0
xdic={}
# for n in range(2,15):
# start from 3
xlen=0
nn=0
for n in range(3,21): 
    Nbody = itertools.combinations_with_replacement(['M','j', 'b', 'e', 'm', 't', 'p'], r=n)
    for com in Nbody:
        M=com.count("M")
        nj,nb=com.count("j"), com.count("b")                   # jets  
        ne,nm,nt=com.count("e"),com.count("m"),com.count("t")  # leptons 
        np=com.count("p")                                      # photons 

        # boundary conditions for high-statistics data
        if M>1 or nj>6 or nb>4 or ne>3 or nm>3 or nt>3 or np>3: continue
        nleptons=ne+nm+nt
        if (nj+nb+nleptons+np>12):         continue
        #if (nj+np>18) or  (nb+np>8):       continue
        #if (nj+nleptons>18) or (nb+nleptons>8):     continue
        if (nj+nb>9):                      continue
        #if (nj+nleptons>20):             continue
        #if (nj+nb+np>18):                   continue
        if (nleptons>5) or (nleptons+np>5): continue
        j=j+1
        comb=(str(M)+"M",str(nj)+"j",str(nb)+"b",str(ne)+"e",str(nm)+"m",str(nt)+"t",str(np)+"p")


        j=j+1

        newlists=getKinematics(com)
        print("New kinematics postions=",newlists) 
 
        #tup=tuple(newlists)
        #if tup in xdic:
        #     print("Already seen") 
        #     continue
        #else:
        #    xdic[tup]=1
        xlen=xlen+len(newlists)
        #print(j,com) # extended print 
        #print(j,txt)   # compact format
        nn=nn+1

print("Total topologies=",nn)
print("Total kinematic combinations=",xlen) 
