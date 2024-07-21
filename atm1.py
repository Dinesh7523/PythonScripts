
def atm(d):
    if(d==0):
        print('account blocked')
        return
    pword=input("enter password:")
    if(pword==password[c]):
        while(1):
            print("1.withdraw\n2.deposit\n3.balance check\n4.pin change")
            choice=int(input("enter your choice:"))
            if choice in [1,2,3,4]:
                break
            else:
                print("enter valid choice")
        if choice==1:
            print(withdraw())
        elif choice==2:
            print(deposit())
        elif choice==3:
            print(balance_check())
        else:
            print(pin_change())
    else:
        print(d-1,"attempts left")
        atm(d-1)
def withdraw():
    amt=int(input("enter your amount:"))
    p=input("enter your pin:")
    if(p==pin[c]):
        if(amt<=balance[c]):
            balance[c]-=amt
            return "collect your amount"
        else:
            return "insufficient balance"
    else:
        return "wrong pin"
def deposit():
    amt=int(input("enter your amount:"))
    p=input("enter your pin:")
    if(p==pin[c]):
        balance[c]+=amt
        return "deposit successful"
    else:
        return "wrong pin"
def balance_check():
    p=input("enter your pin:")
    if(p==pin[c]):
        return balance[c]
    else:
        return "wrong pin"
def pin_change():
    p=input("enter your current pin:")
    if(p==pin[c]):
        n1=input("enter new pin:")
        n2=input("reenter to confirm:")
        if(n1==n2):
            pin[c]==n1
            return "pin updated successfully"
        else:
            return "pins not matched"
    else:
        return "wrong pin"
user=['abd','vk','maxi','dhoni']
password=['abd999','vk18','maxi111','dhoni7']
pin=['360','50100','2023','2011']
balance=[20000,30000,40000,500000]
n=input("enter user name:")
if(n in user):
    c=user.index(n)
    atm(3)
else:
    print("invalid user")
    exit
