from util import Stack, Queue  # These may come in handy
'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None

build our graph
words are nodes, one letter apart is edges
do a bfs from start word to end word
'''

#load word list

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

print(len(word_set))

def get_neighbors(word):
    '''
    return al words from word list that are 1 letter different

    change one letter to another letter in the alphabet incrementally
    seatch the graph for that
    then repeat for each letter in the word
    '''
    neighbors = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z']
    #for each letter in the word,
    for i in range(len(word)):
    #   for each letter in the alphabet
        for letter in alphabet:
            #change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            if w != word and w in word_set:
                neighbors.append(w)
            #if the new word is in the word set
                  #add it to neighbors
    return neighbors



def find_ladders(begin_word, end_word):
    '''
    do  bfs
    create a queue
    enqueue a path to the starting world 
    create a visitied set
    while the queue is not empty
        dequeue the next path
        grab the last word from the path
        check if the word is our end word, if so return path 
        if its not been visited
        mark it as visited 
        enqueue a apth to each neighbor
    '''
    q = Queue()
    q.enqueue([begin_word])
    visited = set()
    while  q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == end_word:
                return path
            visited.add(v)
            for neighbor in get_neighbors(v):
                new_path = path.copy()
                new_path.appennd(neighbor)
                q.enqueue(new_path)
        
