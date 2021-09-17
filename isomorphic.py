def isisomorphic(s, t):
    s_dic = {}
    token = set()
    for a, b in zip(s, t):
        if a not in s_dic:
            if b in token:
                print(False)
            token.add(b)
            s_dic[a] = b
        if s_dic[a] != b:
            print(False)
    print(True)


def main():
    isisomorphic("egg", "add")
    isisomorphic("foo", "bar")
    isisomorphic("paper", "title")
    isisomorphic("abd", "qsd")


if __name__ == "__main__":
    main()
