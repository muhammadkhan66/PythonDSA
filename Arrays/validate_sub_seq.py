def validateSubSequence(array,sequence):
    seqIdx = 0
    arrIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if arrIdx == seqIdx:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(sequence)

print(validateSubSequence([1,2,3,4,5,6,7,8],[2,4,6,8]))



