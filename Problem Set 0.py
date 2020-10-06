import random
import numpy as np
import matplotlib.pyplot as plt

#Globals
global fairHeads,biasedHeads,fairCoinProb,biasedCoinProb
fairHeads = 0.5
biasedHeads = 0.25
fairCoinProb = 0.75
biasedCoinProb = 0.25
maxIndRuns = 5
coinFlipTypes_4a = ["fair","fair","fair","fair","fair","biased","biased","biased","biased","biased"]
coinFlipNums_4a = 40
coinFlipType_4c = "fair"
coinFlipType_4d = "biased"
coinFlipNums_4c_and_4d = 100
probOfBeingBiasedCoin_4c = np.zeros((5,100))
probOfBeingBiasedCoin_4d = np.zeros((5,100))


def flipCoin_4(coinType,numFlip):
    global fairHeads,biasedHeads,fairCoinProb,biasedCoinProb
    flipResult = ""
    flipNum = 0
    probIfFair = 1
    probIfBiased = 1

    if(numFlip < 1):
        return "Not a valid number of coin flips"

    if(coinType == "fair"):
        heads = fairHeads
    elif(coinType == "biased"):
        heads = biasedHeads
    else:
        return "Not a valid coin type"

    for flipNum in range(numFlip):
        randNum = random.randrange(0,100,1)
        if(randNum <= heads*100):
            flipResult += "H"
            probIfFair *= fairHeads
            probIfBiased *= biasedHeads
        else:
            flipResult += "T"
            probIfFair *= (1-fairHeads)
            probIfBiased *= (1-biasedHeads)
        flipNum += 1
    
    probOfBeingBiasedCoin = probIfBiased*biasedCoinProb/(probIfBiased*biasedCoinProb+probIfFair*fairCoinProb)
    return [flipResult,probIfFair,probIfBiased,probOfBeingBiasedCoin]

print("4.1(a/b)")
print()
for coinType in coinFlipTypes_4a:
    [sequence,probIfFair,probIfBiased,probOfBeingBiasedCoin] = flipCoin_4(coinType,coinFlipNums_4a)
    print(str(coinFlipNums_4a),"Flips on",coinType,"-",sequence)
    print("Probability of Sequence if Fair Coin:",probIfFair)
    print("Probability of Sequence if Biased Coin:",probIfBiased)
    print("Probability of Coin Being Biased Based on Sequence:",probOfBeingBiasedCoin)
    print()

print("_____________________________________________________________________________")
print("4.1(c)")
print()
independentRun = 0
coinFlip = 0
for independentRun in range (maxIndRuns):
    for coinFlip in range (coinFlipNums_4c_and_4d):
        [sequence,probIfFair,probIfBiased,probOfBeingBiasedCoin] = flipCoin_4(coinFlipType_4c,coinFlipNums_4c_and_4d)
        print(str(coinFlipNums_4c_and_4d),"Flips on",coinFlipType_4c,"-",sequence)
        print("Probability of Sequence if Fair Coin:",probIfFair)
        print("Probability of Sequence if Biased Coin:",probIfBiased)
        print("Probability of Coin Being Biased Based on Sequence:",probOfBeingBiasedCoin)
        probOfBeingBiasedCoin_4c[independentRun][coinFlip] = probOfBeingBiasedCoin*100
        coinFlip += 1
        print("Coin Flip Number:",coinFlip)
        print()
    independentRun += 1
    print("Independent Run Number:",independentRun,"completed.")
    print()

print("_____________________________________________________________________________")
print("4.1(d)")
print()
independentRun = 0
coinFlip = 0
for independentRun in range (maxIndRuns):
    for coinFlip in range (coinFlipNums_4c_and_4d):
        [sequence,probIfFair,probIfBiased,probOfBeingBiasedCoin] = flipCoin_4(coinFlipType_4d,coinFlipNums_4c_and_4d)
        print(str(coinFlipNums_4c_and_4d),"Flips on",coinFlipType_4d,"-",sequence)
        print("Probability of Sequence if Fair Coin:",probIfFair)
        print("Probability of Sequence if Biased Coin:",probIfBiased)
        print("Probability of Coin Being Biased Based on Sequence:",probOfBeingBiasedCoin)
        probOfBeingBiasedCoin_4d[independentRun][coinFlip] = probOfBeingBiasedCoin*100
        coinFlip += 1
        print("Coin Flip Number:",coinFlip)
        print()
    independentRun += 1
    print("Independent Run Number:",independentRun,"completed.")
    print()

print(probOfBeingBiasedCoin_4c)
print(probOfBeingBiasedCoin_4d)

plt.subplot(1,2,1)
plt.plot(probOfBeingBiasedCoin_4c[0],'r',probOfBeingBiasedCoin_4c[1],'b',probOfBeingBiasedCoin_4c[2],'k',probOfBeingBiasedCoin_4c[3],'y',probOfBeingBiasedCoin_4c[4],'g')
plt.axis([0,100,0,100])
plt.title("Fair Coin Flipped")
plt.xlabel("Trial Number")
plt.ylabel("Probability that Coin is Biased")

plt.subplot(1,2,2)
plt.plot(probOfBeingBiasedCoin_4d[0],'r',probOfBeingBiasedCoin_4d[1],'b',probOfBeingBiasedCoin_4d[2],'k',probOfBeingBiasedCoin_4d[3],'y',probOfBeingBiasedCoin_4d[4],'g')
plt.axis([0,100,0,100])
plt.title("Biased Coin Flipped")
plt.xlabel("Trial Number")
plt.ylabel("Probability that Coin is Biased")
plt.show()