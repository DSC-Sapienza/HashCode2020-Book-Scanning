from math import ceil
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Library:
    books: set
    signup_time: int
    books_per_day: int

    @staticmethod
    def read():
        (_, signup_time, books_per_day) = input().split()
        books = {int(n) for n in input().split()}
        return Library(
          books=books,
          signup_time=int(signup_time),
          books_per_day=int(books_per_day)
        )


def calculate_sum(arr, score):
    result = 0
    for elem in arr:
        result += score[elem]
    return result


(n_different_books, libraries_card, days) = [int(n) for n in input().split()]
score_of = [int(n) for n in input().split()]

libraries = [Library.read() for _ in range(libraries_card)]

result = dict()
n_libraries = len(libraries)
#     intersect = set(libraries[0].books).intersection(set(libraries[1].books))
while days > 0 and len(libraries) > 0:
    # TODO delete each library with signup time > days
    '''
    toDelete = []
    for i in range(len(libraries)):
        if libraries[i].signup_time > days:
            toDelete.append(i)
    for elem in toDelete[::-1]:
        del toDelete[elem]
    '''
    min_sig = -float("inf")
    index = -1
    sig_of_min = float("inf")
    for i in range(n_libraries):
        ## add for free each library with signup time == 0
        if i in result:
            continue
        summatory = calculate_sum(libraries[i].books, score_of)
        normalized = ceil(summatory * libraries[i].books_per_day)
        if normalized >= min_sig:
            if len(libraries[i].books) <= 0:
                continue
            if (normalized == min_sig and libraries[i].signup_time < sig_of_min) or normalized > min_sig:
                min_sig = normalized
                sig_of_min = libraries[i].signup_time
            else:
                continue
            index = i
    if index == -1:
        break
    scanned = deepcopy(libraries[index].books)
    result[index] = scanned
    days -= sig_of_min
    worked = ceil(len(libraries[index].books) / libraries[index].books_per_day)
    # del libraries[index]
    days -= worked
    # -- update

    for elem in libraries:
        elem.books.difference_update(scanned)
        elem.signup_time -= worked
        if elem.signup_time < 0:
            elem.signup_time = 0
'''
toRemove = []
for i in result.keys():
    if len(result[i]) == 0:
        toRemove.append(i)
for index in toRemove:
    del result[index]
'''
print(len(result.keys()))
for i in result.keys():
    '''
    if len(result[i]) == 0:
        continue
    '''
    print(i, len(result[i]))
    # print(result[i])
    for elem in result[i]:
        print(elem, end=' ')
    print("")










