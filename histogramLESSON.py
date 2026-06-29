def historgram_create(massive,binWidth):
    max = max(massive)
    bin_num = (massive//binWidth)+1
    bins = [0]*bin_num
    for i in massive:
        index = max//bin_num
        bins[index] += 1

