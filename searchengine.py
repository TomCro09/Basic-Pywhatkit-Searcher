import pywhatkit as kt
print("Hi There, this is a basic Pywhatkit command that will open your browser based on what you search")



def main():
    search = input("Search: ")
    kt.search(search)
    
while True:
    main()
    again = input("Would you like to seach again? ")
    if again == 'yes':
        main
    else:
        exit()