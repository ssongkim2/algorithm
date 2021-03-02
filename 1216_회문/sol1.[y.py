a = ['asdf','dfsd','fdes','wert']

for row in range(len(a)):
    for col in range(len(a)):
        for col2 in range(col,len(a)+1):
            print(a[col:col2:-1][row])