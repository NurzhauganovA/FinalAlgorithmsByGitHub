import math


def postBubbleSort(post):
    for i in range(len(post)):
        for j in range(len(post) - 1):
            if len(post[j].get('like')) < len(post[j + 1].get('like')):
                temp = post[j]
                post[j] = post[j + 1]
                post[j + 1] = temp

    return post


def postQuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0
    for i in range(1, elements):
        if arr[i]['like'] <= arr[0]['like']:
            current_position += 1
            temp = arr[i]['like']
            arr[i]['like'] = arr[current_position]['like']
            arr[current_position]['like'] = temp
    temp = arr[0]['like']
    arr[0]['like'] = arr[current_position]['like']
    arr[current_position]['like'] = temp

    left = postQuickSort(arr[0:current_position])
    right = postQuickSort(arr[current_position + 1:elements])
    arr = left + [arr[current_position]] + right

    return arr


def postMergeSort(post):
    if len(post) > 1:
        mid = len(post) // 2
        L = post[:mid]
        R = post[mid:]

        postMergeSort(L)
        postMergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i]['like'] <= R[j]['like']:
                post[k] = L[i]
                i += 1
            else:
                post[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            post[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            post[k] = R[j]
            j += 1
            k += 1

    return post


def postInsertionSort(post):
    for i in range(len(post)):
        j = i - 1
        temp = post[i]
        while j >= 0 and len(post[j]['like']) < len(temp['like']):
            post[j + 1] = post[j]
            j -= 1
        post[j + 1] = temp
    return post