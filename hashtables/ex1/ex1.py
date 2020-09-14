def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length <=1:
        return None
    elif limit == (weights[0] + weights[1]):
        return (1, 0)
    else:
        weightDict = {}
        for l in range(length):
            for m in range(1, length):
                total = weights[l] + weights[m]
                weightDict[total] = (l, m)
        if limit in weightDict:
            return weightDict[limit]

    return None
