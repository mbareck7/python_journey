def chapter1():
    p = (3,7)
    x,y = p
    print("x: " + str(x))

    person = ["Mohamed","Developer",(1,1,1995)]
    name,job,birth = person
    print("name: " + name)

    # star expressions
    print("********* star expressions *************")
    data = ["somename", "many", "others", "information"]
    name, *others = data
    print("name: ", name)
    print(others)

    line = "somename:x:1000:1000:mbareck,,,:/home/mbareck:/bin/bash"
    name,_,*_,shell = line.split(":")
    print("name: " + name + ", shell: " + shell)

if __name__ == '__main__':
    chapter1()