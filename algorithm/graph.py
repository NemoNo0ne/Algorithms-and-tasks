from collections import deque

graph = {
    "you": ["adam", "james"],
    "adam": ["bob"],
    "james": ["charlie"],
    "bob": ["mango_seller1"],  # bob имеет друга, который продавец манго
    "charlie": ["dean"],
    "dean": ["ben"],
    "mango_seller1": ["mango_seller2"],  # Продавец манго без друзей
    "mango_seller2": [],
    "ben": []#продавец манго без друзей
}
def person_is_seller(name):
    return "mango" in name.lower()

def search(name): #Все начинается с создания двусторонней очереди(дека), где используется функция deque
    search_queue = deque()
    search_queue += graph[name] #создание новой очереди, все соседи добаваляются в очередь поиска
    searched = [] #Этот массив используется для отслеживания уже проверенных людей
    while search_queue:
        person  = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")