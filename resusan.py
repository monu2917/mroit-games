# def fact(n):
#     if n ==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))





# a=input("enetr a string")
# out=''
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         out+=a[i]
#     i+=1
# print(out)

# def uper(a,out='',i=0):
#     if i>=len(a):
#         return out
#     if 'A'<=a[i]<='Z':
#         out+=a[i]
#     return uper(a,out,i+1)
# print(uper('aBcD'))
# def ent(a,out=[],i=0):
    
#    if i>=len(a):
#        return out
#    if type(a[i])==int:
#      out+=[a[i]]
#    return ent(a,out,i+1)
# print(ent([10,20,30,"monu","salim"]))