
def add(*x):
    ans = 0
    for n in x:
        ans += int(n)
    return ans

"""
from sys import argv
# main, no script,
if __name__ == "__main__" and len(argv) == 1:
    test1 = add(1, 2) == 3
    print("test1 ---> add(1, 2) == 3 --- ", test1)


# script
if argv[1] == "mp3":
    song = ["my_fav_song.1", "my_fav_song.2", "my_fav_song.3"]
    print("select your song :")
    for i, v in enumerate(song):
        print(f"{i}. {v}")
    s = input("select your song :")
    print("opening your song", s)
    #ans = add(*argv[1:])
    #print(ans)

    #print(argv)


# test
if __name__ == "__main__" and len(argv) == 1:
    test1 = add(1, 2) == 3
    print("test1 ---> add(1, 2) == 3 --- ", test1)

"""







def add(a, b):
    return int(a) + int(b)









