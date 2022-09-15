f = open("email.txt", "r")
f2 = open("new_email.txt", "w")

for line in f:
    email = line.split("new ResultPair(\"")[1].split("\", ")[0]
    print(line.split("new ResultPair(\"")[1].split("\", ")[1])
    if line.split("new ResultPair(\"")[1].split("\", ")[1] == "true),\n":
        f2.writelines("        null                     | 'email'                  | " + "'" + email  + "'\n")

    else:
        f2.writelines("        \'matches\'              | 'email'                  | " + "'" + email  + "'\n")
f.close()
f2.close()
