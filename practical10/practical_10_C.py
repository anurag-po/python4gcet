while 1:
    c=input("1.Add 2.View 3.Exit: ")
    if c=="1":
        x=input("Name: ")+","+input("Phone: ")+"\n"
        open("contacts.txt","a").write(x)
    elif c=="2":
        print(open("contacts.txt").read())
    else: break
