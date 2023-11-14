# Process all Pythia8 outputs and create list of topologies 
# Use this script to create boundary conditions
# S.V.Chekanov (ANL)

import glob
import sys

if ((sys.version).find("3.")<0):
         print("Need python3. Exit")
         sys.exit()

XDIR="pythia8/**/*.txt"
xfiles=glob.glob(XDIR,recursive=True)

aMET=[]
aj=[]
ab=[]
ae=[]
am=[]
ap=[]
at=[]

leptons=[]
jets=[]
jetsphotons=[]
jetsleptons=[]
leptonsphotons=[]
jetsphotons=[]
allobjects=[]
Ljetsphotons=[]
Ljetsleptons=[]
Bjetsphotons=[]
Bjetsleptons=[]

# 14 TeV
# Lumi1Mfb=2.575e+02*0.001
# 13 TeV
Lumi1Mfb=2.915e+02*0.001


combinations=[]  
xdic={}
nf=0
for j in xfiles:
    if (j.find("process")>-1): continue # no process files
    #if (j.find("ewk")>-1):     continue # only QCD multijet
    file1 = open(j, 'r')
    Lines = file1.readlines()
    file1.close()
    print(j)
    nf=nf+1
    for xl in Lines:
             xl=xl.strip('\n')
             xchu=xl.split("=")
             xline=xchu[0]
             xline=xline.strip()
             s1=xline.split(" ")
             comb=(s1[0]+"M",s1[1]+"j",s1[2]+"b",s1[3]+"e",s1[4]+"m",s1[6]+"t",s1[5]+"p")

             # unique
             if comb in xdic:
                 #print("Already seen")
                 continue
             else:
                 xdic[comb]=1
                 combinations.append(comb) 
 
             MET=int(s1[0])
             nj=int(s1[1])
             nb=int(s1[2])
             ne=int(s1[3])
             nm=int(s1[4])
             np=int(s1[5])
             nt=int(s1[6])

             leptons.append( ne+nm+nt)
             jets.append( nj+nb )
             jetsphotons.append(nj+nb+np)
             jetsleptons.append(nj+nb+ne+nm+nt)
             leptonsphotons.append(ne+nm+nt+np)
             Ljetsleptons.append(nj+ne+nm+nt)
             Ljetsphotons.append(nj+np)
             Bjetsleptons.append(nb+ne+nm+nt)
             Bjetsphotons.append(nb+np)

             allobjects.append( nj+nb+ne+nm+np+nt)
             if (nj+nb+ne+nm+np+nt ==20): print("Large multiplicity=",comb);
             if (nj>16): print("Large jet multiplicity=",comb);

             aMET.append(MET)
             aj.append(nj)
             ab.append(nb)
             ae.append(ne)
             am.append(nm)
             ap.append(np)
             at.append(nt)

print("Total files=", nf, " total lumi=",Lumi1Mfb*nf," fb");
print("Total combinations=",len(combinations));
print("Max objects seen =",max(allobjects));
print("Max all leptons=",max(leptons));
print("Max all jets=",max(jets));
print("Max all jets+photons=",max(jetsphotons));
print("Max all jets+leptons=",max(jetsleptons)); 
print("Max Ljets+photons=",max(Ljetsphotons));
print("Max Ljets+leptons=",max(Ljetsleptons));
print("Max Bjets+photons=",max(Bjetsphotons));
print("Max Bjets+leptons=",max(Bjetsleptons));
print("Max leptons+photons=",max(leptonsphotons));
print("Max Ljets=",max(aj))
print("Max Bjets=",max(ab))
print("Max elec=",max(ae))
print("Max muon=",max(am))
print("Max photon=",max(ap))
print("Max tau=",max(at))

out='pythia8.json' 
print("Write=",out)
import json
result = json.dumps(combinations, indent=2)
with open(out, 'w') as f:
    json.dump(combinations, f) 
