# LAB 8
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def merge_sort(aList, field, dir):
    """
        >>> fileSet = [['cow', 'pdf', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200],['sara', 'txt', '2021-05-12 05:35', 2500], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200],['pandas', 'exe', '2021-05-12 05:35', 2500], ['cobra', 'psd', '2021-06-12 05:29', 135700]]
        >>> merge_sort(fileSet, 0, 'A')
        [['cobra', 'psd', '2021-06-12 05:29', 135700], ['cow', 'pdf', '2021-05-12 05:35', 2500], ['pandas', 'exe', '2021-05-12 05:35', 2500], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200], ['sara', 'txt', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200]]
        >>> merge_sort(fileSet, 5, 'A')
    """
    # YOUR CODE STARTS HERE
    if field > 3:
        return None
    elif not (dir == "A" or dir == "D"):
        return None
    elif len(aList) > 1:
        left = aList[:(len(aList)//2)]
        right = aList[(len(aList)//2):]
        merge_sort(left, field, dir)
        merge_sort(right, field, dir)

        x = 0
        y = 0
        total = 0
        while x < len(left) and y < len(right):
            if dir == "A":
                if left[x][field] <= right[y][field]:
                    aList[total] = left[x]
                    x += 1
                    total += 1
                else:
                    aList[total] = right[y]
                    y += 1
                    total += 1
            else:
                if left[x][field] >= right[y][field]:
                    aList[total] = left[x]
                    x += 1
                    total += 1
                else:
                    aList[total] = right[y]
                    y += 1
                    total += 1
        while x < len(left):
            aList[total] = left[x]
            x += 1
            total += 1
        while y < len(right):
            aList[total] = right[y]
            y += 1
            total += 1
        return aList
    pass



def selection_sort(aList, field, dir):
    """
        >>> fileSet = [['cow', 'pdf', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200],['sara', 'txt', '2021-05-12 05:35', 2500], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200],['pandas', 'exe', '2021-05-12 05:35', 2500], ['cobra', 'psd', '2021-06-12 05:29', 135700]]
        >>> selection_sort(fileSet, 0, 'A')
        [['cobra', 'psd', '2021-06-12 05:29', 135700], ['cow', 'pdf', '2021-05-12 05:35', 2500], ['pandas', 'exe', '2021-05-12 05:35', 2500], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200], ['sara', 'txt', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200]]
        >>> selection_sort(fileSet, 0, 'B')
    """
    newList = aList[:]
    if field > 3:
        return None
    elif dir == "A":
        for x in range(len(newList)):
            min = x
            for y in range(x + 1, len(newList)):
                if newList[min][field] > newList[y][field]:
                    min = y
            newList[x], newList[min] = newList[min], newList[x]
        return newList
    elif dir == "D":
        for x in range(len(newList)):
            max = x
            for y in range(x + 1, len(newList)):
                if newList[max][field] < newList[y][field]:
                    max = y
            newList[x], newList[max] = newList[max], newList[x]
        return newList
    else:
        return None
    pass
   


def file_set_merger(fsDict, field, dir, algorithm):
    """
        >>> file_dict = {1 : [['cow', 'pdf', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['cobra', 'psd', '2021-06-12 05:29', 135700]],2 : [['threads', 'pdf', '2021-07-12 15:28', 7631], ['posix_doc', 'doc', '2021-09-30 17:44', 39202], ['ray_exams', 'odt', '2022-10-04 21:37', 1877]],3 : [['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200],['pandas', 'exe', '2021-05-12 05:35', 2500]]}
        >>> file_set_merger(file_dict, 0, 'A', 'S')
        [['cobra', 'psd', '2021-06-12 05:29', 135700], ['cow', 'pdf', '2021-05-12 05:35', 2500], ['pandas', 'exe', '2021-05-12 05:35', 2500], ['posix_doc', 'doc', '2021-09-30 17:44', 39202], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200], ['ray_exams', 'odt', '2022-10-04 21:37', 1877], ['snake', 'docx', '2021-06-12 05:29', 15200], ['threads', 'pdf', '2021-07-12 15:28', 7631]]
        >>> file_set_merger(file_dict, 2, 'D', 'S')
        [['ray_exams', 'odt', '2022-10-04 21:37', 1877], ['posix_doc', 'doc', '2021-09-30 17:44', 39202], ['threads', 'pdf', '2021-07-12 15:28', 7631], ['cobra', 'psd', '2021-06-12 05:29', 135700], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['snake', 'docx', '2021-06-12 05:29', 15200], ['rattler', 'msi', '2021-06-12 05:29', 5200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['cow', 'pdf', '2021-05-12 05:35', 2500], ['pandas', 'exe', '2021-05-12 05:35', 2500]]
        >>> file_set_merger(file_dict, 2, 'D', 'H')
    """
    # YOUR CODE STARTS HERE
    newList = []
    for x in fsDict:
        newList += fsDict[x]
    if field > 3:
        return None
    elif not (dir == "A" or dir == "D"):
        return None
    else:
        if algorithm == "M":
            return merge_sort(newList, field, dir)
        elif algorithm == "S":
            return selection_sort(newList, field, dir)
        else:
            return None

    pass




def binary_search(aList, item):
    """
        >>> fileSet = [['cow', 'pdf', '2021-05-12 05:35', 2500], ['snake', 'docx', '2021-06-12 05:29', 15200],['sara', 'txt', '2021-05-12 05:35', 2500], ['puff adder', 'docx', '2021-06-12 05:29', 15200], ['python3', 'exe', '2021-05-12 05:35', 2500], ['rattler', 'msi', '2021-06-12 05:29', 5200],['pandas', 'exe', '2021-05-12 05:35', 2500], ['cobra', 'psd', '2021-06-12 05:29', 135700]]
        >>> binary_search(fileSet, 'puff adder')
        ['puff adder', 'docx', '2021-06-12 05:29', 15200]
        >>> fileSet2 = [['cow', 'pdf', '2017-11-29 15:10', 6780], ['snake', 'docx', '2020-06-12 05:29', 8750],['sara', 'txt', '2020-09-14 09:22', 2], ['puff adder', 'docx', '2022-04-13 11:37', 45300], ['python3', 'exe', '2021-05-29 23:59', 4578],['rattler', 'msi', '2020-01-02 19:09', 15699],['pandas', 'exe', '2019-08-22 17:28', 5772], ['cobra', 'psd', '2021-02-03 21:49', 135700]]
        >>> binary_search(fileSet2, 'python3')
        ['python3', 'exe', '2021-05-29 23:59', 4578]
        >>> binary_search(fileSet2, 'ben')
        False
    """
    # YOUR CODE STARTS HERE
    newList = selection_sort(aList, 0, "A")
    min = 0
    max = len(newList)-1
    while max > min:
        mid = (max + min)//2
        if newList[mid][0] < item:
            min = mid + 1
        else:
            max = mid
    if newList[min][0] == item:
        return newList[min]
    elif newList[max][0] == item:
        return newList[max]
    else:
        return False
    pass




#=== EXTRA CREDIT
def itemize(num):
    '''
        >>> gen = itemize(6120025)
        >>> next(gen)
        5
        >>> next(gen)
        2
        >>> next(gen)
        0
        >>> next(gen)
        0
        >>> next(gen)
        2
        >>> next(gen)
        1
        >>> next(gen)
        6
        >>> next(gen)
        Traceback (most recent call last):
        ...
        StopIteration
        >>> list(itemize(-316798542036498))
        [8, 9, 4, 6, 3, 0, 2, 4, 5, 8, 9, 7, 6, 1, 3]
    '''
    # YOUR CODE STARTS HERE
    pass



def frange(*args):
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    # YOUR CODE STARTS HERE
    pass



def genFib(fn):
    '''
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> [next(evens) for _ in range(15)]
        [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296]
        >>> seq = genFib(lambda x: x > 20 and x % 2)
        >>> next(seq)
        21
        >>> next(seq)
        55
        >>> next(seq)
        89
        >>> next(seq)
        233
        >>> next(seq)
        377
        >>> next(seq)
        987
        >>> next(seq)
        1597
        >>> next(seq)
        4181

        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> sum([next(evens) for _ in range(50)])
        3080657373857639014791750813074
        >>> odds = genFib(lambda x: x % 2 == 1)
        >>> [next(odds) for i in range(25)]
        [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 1597, 4181, 6765, 17711, 28657, 75025, 121393, 317811, 514229, 1346269, 2178309, 5702887, 9227465, 24157817]
        >>> ends_with_5 = genFib(lambda x: x % 10 == 5)
        >>> [next(ends_with_5) for i in range(10)]
        [5, 55, 6765, 75025, 9227465, 102334155, 12586269025, 139583862445, 17167680177565, 190392490709135]

    '''
    # YOUR CODE STARTS HERE
    pass

if __name__=='__main__':
    import doctest
    #doctest.testmod()  # OR
    doctest.run_docstring_examples(binary_search, globals(), name='LAB8',verbose=False)