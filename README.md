# safeLevadas Project

Também pode consultar este README em português. [Click here](README-PT.md)

## Context

The safeLevadas project is developed within the context of the Programming 2 course (LTI) at the Department of Informatics of the Faculty of Sciences of Lisbon, in the academic year 2023/2024. This project aims to create an application in Python 3 called safeLevadas, designed to find the fastest routes between two points in the network of levadas in Madeira Island, improving the support and rescue of hikers.

## Description

safeLevadas is a software designed to support rescue teams in determining the fastest route between two geolocated points in the network of levadas in Madeira. This system is essential to assist in the quick response to distress calls from lost or endangered hikers.

## Features

    Input: The program receives two input files:
        inputFile1.txt: File with the network of levadas.
        inputFile2.txt: File with pairs of stations for which you want to calculate the fastest routes.

    Output: The program generates an output file with the results of the calculated routes:
        outputFile.txt: File with travel times and sequences of stations.

## How to Run

To run the software, use the following command in the command line:

```bash
python safeLevadas.py inputFile1.txt inputFile2.txt outputfile.txt
```
Make sure that the order of the input files is correct.

inputFile1.txt -> Network of levadas, in the specified format.

inputFile2.txt -> Pairs of stations for which you want to calculate the routes.
Example of Input and Output Structure

Structure of inputFile1.txt
```less
#Id, Name, Connected:
A, Seixal, [(R, 15), (M, 8), (B, 12)]
C, Pico Ruivo, [(GJ, 32), (I, 5)]
D, Queimadas, [(Z, 18), (AC, 11)]
E, Ponta do Pargo, [(DW, 13)]
```

## Structure of inputFile2.txt

```less
Cedro - Queimada
Ponta do Pargo - Calheta
Queimada - Boavista
Areeiro – Pico Ruivo
Moinho - Rabacal
```

Structure of outputfile.txt

```less

# Cedro - Queimada
76, Cedro, Queimada
83, Cedro, Rabacal, Queimada
120, Cedro, Ponta do Sol, Areeiro, Queimada
# Ponta do Pargo - Calheta
Calheta out of the network
# Queimada - Boavista
89, Queimada, Ponta do Sol, Pico Ruivo, Boavista
# Areeiro – Pico Ruivo
Areeiro and Pico Ruivo do not communicate
# Moinho - Rabacal
56, Moinho, Areeiro, Rabacal
56, Moinho, Popias, Rabacal
98, Moinho, Rabacal
```

## Software Development

The software consists of the following modules:
```less
    constants.py: Defines the necessary constants.
    dateTime.py: Contains functions to handle date and time formats and operations.
    infoFromFiles.py: Provides functions to read information from files.
    planning.py: Contains functions to determine the fastest routes.
    infoToFiles.py: Offers functions to write information to files.
    safeLevadas.py: Main program that uses the previous modules to implement the safeLevadas application.
```
