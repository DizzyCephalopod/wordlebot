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

## Misc. 
Work in progress...