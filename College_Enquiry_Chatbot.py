print("===== COLLEGE ENQUIRY CHATBOT =====")
print("Welcome to our College!")

print("\n1. Courses")
print("2. Admission")
print("3. Fees")
print("4. College Timings")
print("5. Facilities")
print("6. Exit")

while True:
    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("Courses: Computer, Mechanical, Civil Engineering")

    elif choice == "2":
        print("Admission: Contact the college office.")

    elif choice == "3":
        print("Fees: Contact the college for fee details.")

    elif choice == "4":
        print("College Timings: 9 AM to 5 PM")

    elif choice == "5":
        print("Facilities: Library, Labs, Sports and Canteen")

    elif choice == "6":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")
