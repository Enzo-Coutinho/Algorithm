from collections import deque

people = {}
people["me"] = ["alice", "bob", "claire"]
people["bob"] = ["anuj", "peggy"]
people["alice"] = ["peggy"]
people["claire"] = ["thom", "jonny"]
people["anuj"] = []
people["peggy"] = []
people["thom"] = []
people["jonny"] = []

def is_vendor(nome):
    return nome[-1] == 'm'

def long_search():
    search = deque()
    search += people["me"]
    while search:
        person = search.popleft()
        if is_vendor(person):
            print(f"{person} is manga vendor")
            return True
        else:
            search += people[person]
    return True


def long_search_with_verified():
    search = deque()
    search += people["me"]
    verified = []
    while search:
        person = search.popleft()
        if not person in verified:
            if is_vendor(person):
                print(f"{person} is manga vendor")
                return True
            else:
                search += people[person]
                verified.append(person)
    return True

long_search_with_verified()