# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    
    fulltext = request.GET['fulltext']
    
    worddictionary = {}
    wordlist = fulltext.split()
    for word in wordlist:
        if word in worddictionary:
            #Increase the  count
            worddictionary[word]+=1
        else:
            #add to the dictionary
            worddictionary[word] = 1
            
    worddictionary = dict(sorted(worddictionary.items(), key = operator.itemgetter(1),
                            reverse = True))
            
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),
                                          'worddictionary':worddictionary.items()})
