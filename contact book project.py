
def add_contact(contacts):
    while True:
        name=input("Enter Name:").lower().strip()
        phone=input("Enter Phone:")
        email=input("Enter Email:")
        Dict={"Name":name,"Phone":phone,"Email":email}
        contacts.append(Dict)
        add_more=input("Want to add another(y/n)")
        if add_more=="y":
            continue
        elif add_more=="n":
            return contacts
        
def view_contacts(contacts):
    if not contacts:
         print("No contacts to display:")
    for dicts in contacts:
            for k,v in dicts.items():    
                print(f"{k}:{v}",end="|")
            print(" ")

def search_contact(contacts):     
     found=False
     while True:
        name=input("Enter name of contact:")
        for dicts in contacts:
                if dicts["Name"]==name:
                    found=True                   
                    present_dict=dicts
                    print("Find contact")         
        if not found:
             print("Cannot find contact of that name\n")
             break 
        for key,value in present_dict.items():
            print(f"{key}:{value}",end="|")
        break   
             
                                 
def update_contact(contacts):    
    name = input("Enter name of contact to update:").strip().lower()
    for dicts in contacts:
        if dicts["Name"] == name:
            print("Contact Found.")
            field = input("What to update (phone/email): ").strip().lower()
            if field == "phone":
                dicts["Phone"] = input("Enter new phone: ")
            elif field == "email":
                dicts["Email"] = input("Enter new email: ")
            else:
                print("Invalid field.")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):    
    name = input("Enter name to delete:").strip().lower()
    for dicts in contacts:
        if dicts["Name"] == name:
            contacts.remove(dicts)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main_menu():
    contacts=[]
    while True:
        print("\n---------------------------------------")
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice=input("Enter your CHOICE:")
        print("---------------------------------------")
        if choice=="1":

            add_contact(contacts)
        elif choice=="2":
             view_contacts(contacts)
        elif choice=="3":
            search_contact(contacts)
        elif choice=="4":
            update_contact(contacts)
        elif choice=="5":
            delete_contact(contacts)
        elif choice=="6":
            print("Good Bye") 
            break
        else:
             print("You entered wrong input:")   
print("\nWelcome to Contact Book!\n")
main_menu()