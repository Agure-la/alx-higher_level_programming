#!/usr/bin/python3
#Author - Agure

if __name__ == "__main__":
    """prints all names from hidden"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
