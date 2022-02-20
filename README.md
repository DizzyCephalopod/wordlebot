# Dizzy Cephalopod's Woordle Bot

This is a wordle bot. 

## Setup

This can run in github codespaces. It's also a standard python environment with a requirements.txt that can be run locally.

## Overview
This uses the following method:
1. Determine the popularity of words, under the assumption that more popular words are more likely to be answers. 
2. Make a guess. The score of a guess is the sum of the scores of the words eliminated by that guess. 
   1. The guess with the highest score will be chosen. 
3. Repeat until found

## Scoring
The unscored in `words.txt` are used as a base. These should be *the full set* of possible guesses.
The application can then be run in scoring mode (todo). This will dump a set of scored words into `lexicon.txt`. 
The `lexicon.txt` file is used for playing the wordle game. 

## Usage
Currently only supports interactive mode. 

Example usage:

```
/workspaces/wordlebot (main) $ /usr/local/bin/python /workspaces/wordlebot/app.py
Enter result: aeros/ybbby
Adding result: AEROS/YBBBY
[Y] The word has "A" somewhere.
[Y] The word does not have "A" in the first position.
[B] The word does not have "E" anywhere.
[B] The word does not have "R" anywhere.
[B] The word does not have "O" anywhere.
[Y] The word has "S" somewhere.
[Y] The word does not have "S" in the fifth position.
--------
--------
BALSA|10379
BASIC|10841
BASIL|11432
BLASH|11435
BLAST|11582
CANST|11602
CLASH|11705
CLAST|11852
HASTY|11865
PLASH|11874
PLAST|12021
SAITH|12052
SALTY|12059
SHALT|12249
Most Yellows: SHALT
BALSA|4054.771607950519
BASSY|4405.396734558855
MASSA|4509.379825738976
SABAL|5525.520720509329
SADLY|5888.22976116956
SAIGA|5901.692587890564
SAIST|6202.693273705492
SALSA|6794.213190304411
SASSY|7144.838316912737
Best Positionally: SASSY
Best pure guesses: SHALT, BASIC, BASAL
Enter result: unity/bgbbb
Adding result: UNITY/BGBBB
[Y] The word has "A" somewhere.
[Y] The word does not have "A" in the first position.
[B] The word does not have "E" anywhere.
[B] The word does not have "R" anywhere.
[B] The word does not have "O" anywhere.
[Y] The word has "S" somewhere.
[Y] The word does not have "S" in the fifth position.
[B] The word does not have "U" anywhere.
[G] The word has "N" in the second position.
[B] The word does not have "I" anywhere.
[B] The word does not have "T" anywhere.
[B] The word does not have "Y" anywhere.
--------
--------
GNASH|184
Most Yellows: GNASH
GNASH|167.56086700319062
SNACK|168.01536309886504
SNASH|179.51706244933482
Best Positionally: SNASH
Best pure guesses: SNACK, GNASH, UNKNOWN
Enter result: snack/ggggg
Adding result: SNACK/GGGGG
[Y] The word has "A" somewhere.
[Y] The word does not have "A" in the first position.
[G] The word has "A" in the third position.
[B] The word does not have "E" anywhere.
[B] The word does not have "R" anywhere.
[B] The word does not have "O" anywhere.
[Y] The word has "S" somewhere.
[Y] The word does not have "S" in the fifth position.
[G] The word has "S" in the first position.
[B] The word does not have "U" anywhere.
[G] The word has "N" in the second position.
[G] The word has "N" in the second position.
[B] The word does not have "I" anywhere.
[B] The word does not have "T" anywhere.
[B] The word does not have "Y" anywhere.
[G] The word has "C" in the fourth position.
[G] The word has "K" in the fifth position.
--------
--------
SNACK|105
Most Yellows: SNACK
SNACK|105.47152941978977
Best Positionally: SNACK
Best pure guesses: SNACK, UNKNOWN, UNKNOWN
Enter result: q
```