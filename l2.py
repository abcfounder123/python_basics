
users = (
{"user name" : "Mg Mg",
"password" : "1234561",
"age" : 20,
"email address" : "mgmg123@gmail.com",
"status" : "active",
"marks" : {"myn" : 36, "eng" : 30, "math" : 90},

},

{"user name" : "Ma Ma",
"password" : "1234562",
"age" : 25,
"email address" : "mama456@gmail.com",
"status" : "inactive",
"marks" : {"myn" : 60, "eng" : 90, "math" : 20}
},

{"user name" : "Hla Hla",
"password" : "1234563",
"age" : 30,
"email address" : "hlahla789@gmail.com",
"status" : "active",
"marks" : {"myn" : 50, "eng" : 95, "math" : 39}
}

)

# 2 step

fail_users = []
for user in users:
    f_sub = {}
    for sub, mark in user["marks"].items():
        if mark < 40:
            f_sub[sub] = mark# f_sub = {"math" : 39}
            # fail_users += [[user["user name"], sub]]
            # fail_users.append(user["user name"])
    if f_sub:
        fail_users += [[user["user name"], f_sub]]

print(users)
print(fail_users)
