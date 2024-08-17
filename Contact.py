Contacts={
    "Khush":[7990537735,"Me"],
    "Ravikant":[9099065979,"Papa"],
    "Rekha":[9106551988,"Mummy"]
    }
def display_contact():
    print("Your Contact List:->\n")
    for name,details in Contacts.items():
        phonenumber=details[0]
        description=details[1]

        print(f"Name:- {name}")
        print(f"Phone Number:- {phonenumber}")
        print(f"Description:- {description}")
        print("--------------------------------")

def add_contact():
    Name=input("Enter the Name of Contact:")
    PhoneNumber=int(input("Enter the Phone Number of Contact:"))
    Description=input("Enter Description about Contact:")
    Contacts[Name]=[PhoneNumber,Description]
    print(f"Contact {Name} added.")
    print(f"Name:- {Name}\nPhone Number:- {PhoneNumber}\nDescription:- {Description}\n")
    display_contact()
def delete_contact():
    contact_name=input("Enter the name of contact:\n")
    if contact_name in Contacts:
        del Contacts[contact_name]
        print(f"Successfully Deleted {contact_name}.\n")
    else:
        print(f"Contact {contact_name} Doesnt Exists.")
    display_contact()
def update_contact():
    check_contact=input("Enter the Contact Name to Update:")
    if check_contact in Contacts:
        field_update=input("What do u want to Change in Contacts:").lower()
        if (field_update=="name"):
            new_Name=input(f"Write the New {field_update} for {check_contact}:")
            # Contacts[new_Name]=Contacts.pop(check_contact)
            Contacts[new_Name]=Contacts[check_contact]
            del Contacts[check_contact]
            print(f"The {field_update} of {check_contact} has been changed to {new_Name}")
            update_contact()
        elif field_update in["phone","number","phone number"]:
            new_Number=input(f"Write the New {field_update} for {check_contact}:")
            Contacts[check_contact][0]=new_Number
            print(f"The {field_update} of {check_contact} has been changed to {new_Number}")
            update_contact()
        elif (field_update=="description"):
            new_Description=input(f"Write the New {field_update} for {check_contact}:")
            Contacts[check_contact][1]=new_Description
            print(f"The {field_update} of {check_contact} has been changed to {new_Description}")
            print(f"Name:- {new_Name}\nPhone Number:- {new_Number}\nDescription:- {new_Description}")    
            update_contact()
    else:
        print(f"{check_contact} doesnt exists")
Function=["Add New Contacts(add)","Update New Contacts(update)","Delete New Contacts(delete)","Display Contacts List(display)","Exit"]
print("Functions")
for i in Function:
    print(i)
choose_fn=input("What do you want to do?\n").lower()
if (choose_fn=="add"):
    add_contact()
elif (choose_fn=="delete"):
    delete_contact()
elif (choose_fn=="update"):
    update_contact()
elif (choose_fn=="display"):
    display_contact()
elif (choose_fn=="exit"):
    exit()