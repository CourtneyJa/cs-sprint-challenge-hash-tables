def has_negatives(a):
    """
    YOUR CODE HERE
    """
    t = {n: False for n in a}
    result = []
    for n in a:
        if n != 0 and -n in t and not t[n] and not t[-n]:
            t[-n] = True
            t[n] = True
            #abs = absolute value
            result.append(abs(n))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
