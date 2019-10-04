import requests


class API():

    def Table(self):
        url = 'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9'
        resp = requests.get(url)
        lista = resp.json()['squares']
        a = []

        for x in range(len(lista)):
            a.append([])
            for y in str(lista[x]):
                if y.isdigit():
                    a[x].append(int(y))

        table = ["xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx",
                 "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx", "xxxxxxxxx",
                 "xxxxxxxxx"]
        for x in range(len(a)):
            row = a[x][1]
            col = a[x][0]
            table[row] = table[row][:col] + str(a[x][2]) + table[row][col+1:]

        return table
