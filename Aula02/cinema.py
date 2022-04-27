import json
from operator import itemgetter
cinema = []

def createDictForCinema():
    f = open("cinemaATP.json", "r")
    cinema = json.load(f)
    f.close()
    return cinema

def getMovieByTitle(title):
    for value in range(0, len(cinema)):
        if(cinema[value]["title"] == title):
            return cinema[value]
    return "undefined"

def getMoviesWithWordOnTitle(word):
    ans = []
    for value in range(0, len(cinema)):
        if(word in cinema[value]["title"]):
            ans.append(cinema[value]["title"])
    return ans

def partitionAlphabetic(arr, low, high):
    i = low - 1
    pivot = arr[high]["title"].lower()

    for j in range(low, high):
        if arr[j]["title"].lower() <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickAlphabetic(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partitionAlphabetic(arr, low, high)
        quickAlphabetic(arr, low, pi - 1)
        quickAlphabetic(arr, pi + 1, high)

def quickAlphabeticOrder():
    ans = cinema
    quickAlphabetic(ans, 0, len(ans) - 1)
    return ans

def moviesFromGenre(genre):
    ans = []
    for j in range(0, len(cinema) - 1):
        genres = cinema[j]["genres"]
        if(len(genres) > 0):
            for k in range(0, len(genres)):
                if genres[k].lower() == genre.lower():
                    ans.append(cinema[j]["title"])
    return ans

def moviesWithActor(actor):
    ans = []
    for j in range(0, len(cinema) - 1):
        cast = cinema[j]["cast"]
        if(len(cast) > 0):
            for k in range(0, len(cast)):
                if cast[k].lower() == actor.lower():
                    ans.append(cinema[j]["title"])
    return ans

def totalMovies():
    return len(cinema)

def moviesByGenre():
    genresOnDB = {}
    for j in range(0, len(cinema) - 1):
        genres = cinema[j]["genres"]
        if(len(genres) > 0):
            for k in range(0, len(genres)):
                if genres[k] in genresOnDB.keys():
                    genresOnDB[genres[k]] += 1
                else:
                    genresOnDB[genres[k]] = 1
    return genresOnDB

def getOrderedArrayFromDictionary(dictionary):
    maxA = 0
    actor = ""
    for val in dictionary.keys():
        if dictionary[val] > maxA:
            actor = val
            maxA = dictionary[val]
    dictionary.pop(actor)
    return actor

def moviesByActor(nElems):
    castOnDB = {}
    ans = []
    for j in range(0, len(cinema) - 1):
        cast = cinema[j]["cast"]
        if(len(cast) > 0):
            for k in range(0, len(cast)):
                if cast[k] in castOnDB.keys():
                    castOnDB[cast[k]] += 1
                else:
                    castOnDB[cast[k]] = 1
    counter = 1
    for k, v in sorted(castOnDB.items(), key=lambda kv: kv[1], reverse=True):
        if counter == nElems:
            break
        elif k == "and" or k == "(voice)":
            pass
        else:
            ans.append(k)
            counter += 1
    return ans
