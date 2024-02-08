
from Bank import BankAccount, test

def open_db(file, db):
    with open(file) as f:
        for line in f:
            id, name, balance = line.split(", ")
            db.append(BankAccount(id, name, int(balance)))

def print_db(db):
    print("{:<5} {:<10} {:<20}".format("ID", "Name", "Balance"))
    for acc in x:
        print(acc)


def get(db, id):
    for acc in db:
        if acc.info()[0] == id:
            return acc

def add(db,id, name, balance):
    db.append(BankAccount(id, name, int(balance)))

def delete(db, id):
    for i in range(len(db)):
        if db[i].info()[0] == id:
            del db[i]
            break


def commit(db, file):
    with open(file, "w") as f:
        for acc in db:
            f.write("{}, {}, {}\n".format(*acc.info()))




x = []
open_db("data.text", x)
print_db(x)
print("-" * 20)

acc222 = get(x, "111")
acc222.deposit(500000)

print_db(x)

commit(x, "data.text")