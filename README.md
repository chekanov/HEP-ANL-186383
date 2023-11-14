# HEP-ANL-186383
Source code and data for the preprint HEP-ANL-186383. This example demonstrates the calculations for 5 fb-1. 
First, calculated the boundary condition using Pythia8:

```
python3 py8count.py
```
This code reads text files from the directory pythia8/out/ewk (qcd)  from Pythia8 sumulation. 
Each file was made using 1M events. To reproduce Pythia8 computations, compile the code main.cxx
(make mydict; make) 
and run it as:

```
TotalEvents=1000000
# if -1, use CPU seed
UseSeed=-1
OUTPUT="out/out_pythia8_sm14tev.root"
./main.exe tev13_SM_A14_NNPDF23LO_EWK.py $OUTPUT  $TotalEvents $UseSeed
```
 

Then perform the numeric computation:

```
python3 py8count.py
python3 combinations.py
python3 kinematics.py 
```

S.V.Chekanov (ANL)
