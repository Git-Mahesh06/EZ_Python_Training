def tower(n,frm,to,aux):
    if n==0:
        return 
    tower(n-1,frm,aux,to)
    print(f"move {n} from {frm} to {to}")
    tower(n-1,aux,to,frm)
n=2

tower(n,'A','C','B')