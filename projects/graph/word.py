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

# def get_neighbors(word):





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
        
