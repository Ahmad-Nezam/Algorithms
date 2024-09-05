def flex(low , high ,mult):
    for i in range (high , low - 1 , -1):
        if i % mult == 0 :
            print(i)

flex(4,12,2) 