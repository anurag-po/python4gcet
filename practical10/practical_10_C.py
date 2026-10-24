while 1:
    c=input("1.Add 2.View 3.Exit: ")
    if c=="1": open("contacts.txt","a").write(input("Name: ")+","+input("Phone: ")+"\n")
    elif c=="2": print(open("contacts.txt").read())
    else: break
