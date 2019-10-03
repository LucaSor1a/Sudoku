import requests

class API():

    def Table(self):
        resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9')
        lista = resp.json()['squares']
        a = []

        for x in range(len(lista)):
            a.append([])
            for y in str(lista[x]):
                if y.isdigit():
                    a[x].append(int(y))

        table = ["xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx"]
        for x in range(len(a)):
            table[a[x][1]] = table[a[x][1]][:a[x][0]] + str(a[x][2]) + table[a[x][1]][a[x][0]+1:]

        return table