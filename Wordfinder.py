fn=input("Enter the File Name u want to add:")
with open(f'{fn}','r') as file:
    r=file.read()
    # print(r)
    rf=r.replace(',','').replace('.','')
    # print(rf)
    f=rf.lower().split()
    # print(f)
fw=(input("Enter the Word you want to find: "))
cw=f.count(fw)
print("Do you want to 'Find & Count(fc)' the word or 'Find & Replace(fr)' it.")
useri=input("Enter the Command: ").lower()
if(useri=="fc"):
    if(cw>0):
        print(f"The Word: '{fw}', is present {cw} times in paragraph.")
    else:
        print("The Word: '{fw}', isnt present in the paragraph.")    
elif(useri=="fr"):
    rw=input(f"Enter the word u want to replace '{fw}' with: ")
    # inp=input("Do you want to replace a single(s) word or multiple(m): ")
    # if(inp=="m"):
    replace=r.replace(fw,rw)
    print(replace)
    file.close()
    # elif(inp=="s"):
else:
    print("The Function specified doesnt Exists, Use valid functions.")

