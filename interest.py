def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    return si
if __name__ == "__main__":
    p=20000
    r=2
    t=3
    result=simple_interest(p,t,r)
    print("Simple interest:",simple_interest(principal,rate,time))
