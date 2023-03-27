# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID(UoW): w1912864

# Student ID(IIT): 20210239

# Date: 17th April 2022

def get_all_in_one():
# This function is used to store all other functions in it to refrain from using global variables
    pass_mark = 0
    defer_mark = 0
    fail_mark = 0
    progress = []
    pro_trailer = []
    mod_retriever = []
    exclude = []
    lists = []
    credit = [0, 20, 40, 60, 80, 100, 120]

    def get_inputs():
    # This function is used to get user inputs
        while True:
            try:
                pass_mark = int(input("Please enter your credit at pass  : "))

            except ValueError:
                print("Integer required.")
                print()

            else:
                if pass_mark not in credit:
                    print("Out of range.")
                    print()
                elif pass_mark in credit:
                    break

        while True:
            try:
                defer_mark = int(input("Please enter your credit at defer : "))

            except ValueError:
                print("Integer required.")
                print()

            else:
                if defer_mark not in credit:
                    print("Out of range.")
                    print()
                elif defer_mark in credit:
                    break

        while True:
            try:
                fail_mark = int(input("Please enter your credit at fail  : "))

            except ValueError:
                print("Integer required.")
                print()

            else:
                if fail_mark not in credit:
                    print("Out of range.")
                    print()
                elif fail_mark in credit:
                    break

        while True:
            total = pass_mark + defer_mark + fail_mark
            if total != 120:
                print("Total incorrect.")
                print()
                get_inputs()
                break
            else:
                get_progression(pass_mark, defer_mark, fail_mark)
                break

    def get_progression(pass_mark, defer_mark, fail_mark):
    # This function is used to validate the inputs
        if pass_mark == 120:
            lists = [pass_mark , defer_mark, fail_mark]
            progress.append(lists)
            print("Progress")
            print()
        elif pass_mark == 100:
            lists = [pass_mark , defer_mark, fail_mark]
            pro_trailer.append(lists)
            print("Progress (module trailer)")
            print()
        elif pass_mark == 80 or \
             pass_mark == 60 or \
             (pass_mark == 40 and defer_mark > 0) or \
             (pass_mark == 20 and defer_mark >= 40) or \
             (pass_mark == 0 and defer_mark >= 60):
            lists = [pass_mark , defer_mark, fail_mark]
            mod_retriever.append(lists)
            print("Module retriever")
            print()
        elif fail_mark >= 80:
            lists = [pass_mark , defer_mark, fail_mark]
            exclude.append(lists)
            print("Exclude")
            print()

    def get_horizontal_histogram():
    # This function is used to print the horizontal histogram
        get_progression(pass_mark, defer_mark, fail_mark)
        print(22*"-", "Horizontal Histogram", 22*"-")
        print()
        print("Progress ", len(progress), ":", "*" * len(progress))
        print("Trailer  ", len(pro_trailer), ":", "*" * len(pro_trailer))
        print("Retriever", len(mod_retriever), ":", "*" * len(mod_retriever))
        print("Excluded ", len(exclude), ":", "*" * len(exclude))
        print()
        outcomes = len(progress) + len(pro_trailer) + len(mod_retriever) + len(exclude)
        if outcomes == 1:
            print("Only one outcome in total.")
        else:
            print (outcomes, "outcomes in total.")
        print()

    def get_vertical_histogram():
    # This function is used to print the vertical histogram
    # https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
        print(23*"-", "Vertical Histogram", 23*"-")
        print()
        header = ["Progress", "      Trailing", "      Retriever", "      Excluded"]
        print(" ".join(header))
        for x in range(max(len(progress), len(pro_trailer), len(mod_retriever), len(exclude))):
            print("   {0}              {1}               {2}              {3}".format(
                  "*" if x < len(progress) else " ",
                  "*" if x < len(pro_trailer) else " ",
                  "*" if x < len(mod_retriever) else " ",
                  "*" if x < len(exclude) else " "))
        print()
        outcomes = len(progress) + len(pro_trailer) + len(mod_retriever) + len(exclude)
        if outcomes == 1:
            print("Only one outcome in total.")
        else:
            print (outcomes, "outcomes in total.")
        print()

    def get_rounds(menu_option):
    # This function is used to loop the staff version
        while True:
            print("Would you like to enter another set of data?")
            option = input("Enter 'y' for yes or 'q' to quit and view results : ").lower()
            print()
            if option == "y":
                get_inputs()
            elif option == "q":
                if menu_option == "2":
                    get_horizontal_histogram()
                elif menu_option == "3":
                    get_vertical_histogram()
                    print()
                elif menu_option == "4":
                    get_lists(progress, pro_trailer, mod_retriever, exclude)
                break

    def get_lists(progress, pro_trailer, mod_retriever, exclude):
    # This function is used to print the list view
    # https://www.delftstack.com/howto/python/list-without-brackets-python/
        print(28*"-", "List View", 27*"-")
        print()
        for i in progress:
            print("Progress                  -", (str(i)[1:-1]))
        for j in pro_trailer:
            print("Progress (module trailer) -", (str(j)[1:-1]))
        for k in mod_retriever:
            print("Module retriever          -", (str(k)[1:-1]))
        for l in exclude:
            print("Exclude                   -", (str(l)[1:-1]))
        print()

    def get_text_file(progress, pro_trailer, mod_retriever, exclude):
    # This function is used to write to a text file and read from it
        print(25*"-", "Text File View", 25*"-")
        print()
        file = open("progression_outcome.txt", "w")

        for i in progress:
            file.write("Progress                  - " + (str(i)[1:-1]) + "\n")
        for j in pro_trailer:
            file.write("Progress (module trailer) - " + (str(j)[1:-1]) + "\n")
        for k in mod_retriever:
            file.write("Module retriever          - " + (str(k)[1:-1]) + "\n")
        for l in exclude:
            file.write("Exclude                   - " + (str(l)[1:-1]) + "\n")
        file.close()

        file = open("progression_outcome.txt", "r")
        data = file.read()
        print(data)
        file.close()

    def get_menu_options():
    # This function is used to print out the menu and for user to choose the option
        while True:
            print(30*"-","Menu", 30*"-")
            print()
            print("             1. Student version")
            print("             2. Staff version with horizontal histogram")
            print("             3. Staff version with vertical histogram")
            print("             4. Staff version with list view")
            print("             5. Staff version with text file")
            print("             6. Exit")
            print()
            menu_option = input("Enter your option : ")
            print()

            if menu_option == "1":
                print(24*"-", "Student Version", 25*"-")
                print()
                get_inputs()
            elif menu_option == "2":
                print(26*"-", "Staff Version", 25*"-")
                print()
                get_inputs()
                get_rounds(menu_option)
            elif menu_option == "3":
                print(26*"-", "Staff Version", 25*"-")
                print()
                get_inputs()
                get_rounds(menu_option)
            elif menu_option == "4":
                print(26*"-", "Staff Version", 25*"-")
                print()
                get_inputs()
                get_rounds(menu_option)
            elif menu_option == "5":
                print(26*"-", "Staff Version", 25*"-")
                print()
                get_inputs()
                get_rounds(menu_option)
                get_text_file(progress, pro_trailer, mod_retriever, exclude)
            elif menu_option == "6":
                print("Exited!")
                break
            else:
                print("Invalid option. Choose an option from the menu to proceed.\n")
            lists.clear(), progress.clear(), pro_trailer.clear(), mod_retriever.clear(), exclude.clear()
    get_menu_options() # Call the "get_menu_options" function 
get_all_in_one() # Call the "get_all_in_one" function
