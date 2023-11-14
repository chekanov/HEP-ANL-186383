# https://learnpython.com/blog/combinatoric-iterators-in-python/
# Notations:
#  M: MET (0,1)
#  j: light-flavour jets
#  b: b-jets
#  e: electrons
#  m: muons
#  t: tau
#  p: photons 
import itertools

j=0
for n in range(2,15):
    Nbody = itertools.combinations_with_replacement(['M','j', 'b', 'e', 'm', 't', 'p'], r=n)
    for com in Nbody:
        M=com.count("M")
        nj=com.count("j")
        nb=com.count("b")
        ne=com.count("e") 
        nm=com.count("mu")
        nt=com.count("t")
        np=com.count("p")
        # boundary conditions are below
        if M>1: continue
        if nj>9: continue
        if nb>6: continue
        if ne>4: continue
        if nm>4: continue
        if nt>4: continue
        if np>4: continue
        if ne+nm+nt>4: continue
        if ne+nm+nt+np>5: continue
        j=j+1
        txt=str(M)+" "+str(nj)+" "+str(nb)+" "+str(ne)+" "+str(nm)+" "+str(np)+" "+str(nt)
        # print(j,com) # extended print 
        print(j,txt)   # compact format 
