print(__name__)

def test():
    print("in test")
    print(xyz)

#if xyz=="kkk": test()

if True: #__name__=="__main__":
    xyz="kkk"

    test()

if __name__=="__main__":
    test()
