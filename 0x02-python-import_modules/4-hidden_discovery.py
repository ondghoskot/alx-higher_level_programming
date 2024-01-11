#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namez = dir(hidden_4)
    i = 0
    while i < len(namez):
        if len(namez) < 2 or namez[i][0] != '_' or  namez[i][1] != '_':
            print(namez[i])
            i += 1
