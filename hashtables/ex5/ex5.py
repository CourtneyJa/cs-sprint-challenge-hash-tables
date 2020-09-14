# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    hashTable = {}
    result = []
    for f in files:
        f = f.split("/")
        if f[-1] not in hashTable:
            hashTable[f[-1]] = []
        hashTable[f[-1]].append("/".join(f[:-1]))
    for q in queries:
        if q in hashTable:
            for f in hashTable[q]:
                result.append(f + "/" + q)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
