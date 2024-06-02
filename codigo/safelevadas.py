# 2023-2024 Programação 2 LTI
# Grupo 5
# 62372 Guilherme Soares
# 62211 Vitória Correia

import sys
from fileProcessing import *
from findAllStations import *
from writeMS import *
def safelevadas(inputFile1, inputFile2, outputFile):
    """
    Processes a network of levadas (irrigation channels) and pairs of stations, and writes the results to an output file.
    
    Args:
        inputFile1 (str): Path to the input file containing the network of levadas in a specific format.
        inputFile2 (str): Path to the input file containing pairs of station names, one pair per line.
        outputFile (str): Path to the output file where the results will be written.
    """
    
    dataLN = readLN(inputFile2) #reads the levada network file
    myStations = readMyStations(inputFile1) #reads the stations it'll search
    dig = buildNetwork(dataLN) #builds the nodes and edges from the inputFile2
    srcDestNodes = findSrcDestNodes(myStations, dig)

    allPaths = findAllStations(srcDestNodes, dig)

    writeMS(allPaths, myStations, srcDestNodes, outputFile)
    
    
if len(sys.argv) < 4:
    print("""
    The user should display the files in the command line in the following way:
    python safeLevadas.py myLevadasNetwork.txt myStations.txt outputFile.txt

    where:
    - safeLevadas.py: this is the software you are running;
    - myLevadasNetwork.txt: the path of the file with the levada paths;
    - myStations.txt: the path of the file with the pairs of stations in each line;
    - outputFile.txt: the path of the file where the output will be written.
    """)
else:
    safelevadas(sys.argv[1],sys.argv[2],sys.argv[3])
    