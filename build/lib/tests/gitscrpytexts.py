from gitscrpy import getgit

def tests():
    a=getgit.gitinit("fredysomy")
    assert len(a.getrepo(2)) == 2
    assert len(a.getrepo(3)) == 3
    assert a.getuser("u_name") == "fredysomy"

if __name__=="__main__":
    tests()
    print("All tests have passed")
