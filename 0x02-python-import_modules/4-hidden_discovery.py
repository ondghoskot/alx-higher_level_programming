#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namez = dir(hidden_4)
    i = 0
    while i < len(namez):
        if not (len(namez) > 2 and namez[i][0] == '_' and namez[i][1] == '_'):
            print(namez[i])
