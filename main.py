# 211RDB475 Kristofers Zellītis 9.grupa
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            found = False
            for contact in contacts:
                if contact.number == cur_query.number:
                    result.append(contact.name)
                    found = True
                    break
            if not found:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
