


FnameCSV = "symmetries.csv"
FnameASP = "symmetries.asp"
UpperBoundInputs = 10
UpperBoundGates  = 6
GateTypes = [{"LowerBoundPos":0,"UpperBoundPos":2,
              "LowerBoundNeg":0,"UpperBoundNeg":0,
              "UpperBoundOcc":2},
             {"LowerBoundPos":0,"UpperBoundPos":0,
              "LowerBoundNeg":0,"UpperBoundNeg":2,
              "UpperBoundOcc":4}]
EfficiencyConstraint = True
OptimizationStrategy = 2
BreakSymmetries = True


import sys
sys.path = ["../"] + sys.path
import classifier

if __name__=="__main__":
    if 1 :
        classifier.csv2asp(
            FnameCSV,
            FnameASP,
            UpperBoundInputs,
            UpperBoundGates,
            GateTypes,
            EfficiencyConstraint,
            OptimizationStrategy,
            BreakSymmetries)
            
    if 0 :
        GateInputs = "gate_input(1,negative,g1)"
        classifier.check_classifier(FnameCSV, GateInputs)

    if 0 :
        GateInputs = "gate_input(2,positive,g2) gate_input(1,negative,g1)"
        FnamePDF = "toy_classifier.pdf"
        classifier.gateinputs2pdf(FnamePDF, GateInputs)
        
    if 0 : 
    	  FnameMAT = "casestudy01.mat"
    	  Threshold = 250
    	  classifier.mat2csv(FnameMAT, Threshold)

    
