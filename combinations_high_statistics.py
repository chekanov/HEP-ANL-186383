# Calculate unique combinations with and without boundary conditions
# If you need help to understand this code, look at
# https://learnpython.com/blog/combinatoric-iterators-in-python/
# We use combinations_with_replacement(),  similar to combinations(), 
# but it allows the items to be repeated more than once. 
# 
# S.V.Chekanov
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


import itertools
j=0

# read Pythia8 prediction 
import json
pythia8=[]
with open('pythia8.json', 'r') as f:
    pythia8=json.load(f)

# process as dic
pythiamap={}
for j in pythia8:
        pythiamap[tuple(j)]=1

j=0
nbefore=0
No=0
xdic={}
combinations=[]
for n in range(2,21):
    Nbody = itertools.combinations_with_replacement(['M','j', 'b', 'e', 'm', 't', 'p'], r=n)
    for com in Nbody:
        M=com.count("M")
        nj,nb=com.count("j"), com.count("b")                   # jets  
        ne,nm,nt=com.count("e"),com.count("m"),com.count("t") # leptons 
        np=com.count("p")                                      # photons 
        nbefore=nbefore+1
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

        # unique
        if comb in xdic:
             #print("Already seen")
             continue
        else:
             xdic[comb]=1
             combinations.append(comb)

        # find which combinations are not in Pythia8
        if comb not in pythiamap:
                    print("Not in Pythia8=",comb)
                    No=No+1 

        # print(j,com)  # extended print 
        print(j,comb)   # compact format

print("Nr of combinations before boundary conditions=",nbefore)
print("Nr of combinations after  boundary conditions=",j)
print("Nr of combinations are not in Pythia8=",No)

# now do this analytically without boundary conditions
import math
math.factorial(1000)

nn=0
n=7
for r in range(2,21):
      fac1=math.factorial(n+r-1) 
      fac2=math.factorial(n-1)*math.factorial(r)
      nn=nn+(fac1/fac2) 
print("Analytic Answer=",nn)  
