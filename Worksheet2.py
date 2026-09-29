

courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

print(courses)
sorted_courses = sorted(courses)

print("\nCourses in alphabetical order:")
print(sorted_courses)

reverse_sorted_courses = sorted(courses, reverse=True)

print("\nCourses in reverse alphabetical order:")
print(reverse_sorted_courses)

courses.reverse()

print("\nCourses after using reverse():")
print(courses)

courses.reverse()

print("\nCourses after using reverse() again:")
print(courses)
courses.sort()

print("\nCourses after using sort() alphabetically:")
print(courses)

courses.sort(reverse=True)

print("\nCourses after using sort() in reverse alphabetical order:")
print(courses)
courses.sort()

print("\nThe following courses are available for expression of interest if the students meet the prerequisites:")

for course in courses:
    print(course)
withdrawn_course = "Physics I"
new_course = "Calculus II"

index = courses.index(withdrawn_course)
courses[index] = new_course

print("\nCourse Update:")
print(withdrawn_course, "has been withdrawn.")
print(new_course, "has been added as the replacement.")

print("\nUpdated courses:")
for course in courses:
    print(course)

courses.insert(0, "Physics I")

middle = len(courses) // 2
courses.insert(middle, "Chemistry I")

courses.append("Biology I")

print("\nCourses after adding three courses:")

for course in courses:
    print(course)
print("\nDue to technical and room availability issues, the following courses are unavailable:")

removed1 = courses.pop()
print(removed1, "has been withdrawn.")

removed2 = courses.pop()
print(removed2, "has been withdrawn.")

removed3 = courses.pop()
print(removed3, "has been withdrawn.")

removed4 = courses.pop()
print(removed4, "has been withdrawn.")

print("\nCourses still available:")

for course in courses:
    print(course)
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

course_information = []

for course_id, course_name in course_tuples:
    course_information.append((course_id, course_name))

print("\nCourse Information:")

for course in course_information:
    print("Course ID:", course[0], "- Course Name:", course[1])
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]
while True:

    user_input = input("\nEnter a Course ID (1-15), or enter quit to exit: ")

    if user_input.lower() == "quit":
        print("The value quit has been used to exit.")
        break

    if user_input == "0":
        print("Course ID is out of range (1-15), try again.")
        continue

    try:
        course_id = int(user_input)
        found = False

        for course in departments:
            if course[0] == course_id:
                print("Course ID", course_id, "is in the", course[1], "department.")
                found = True
                break

        if not found:
            print("Course ID not found.")

    except ValueError:
        print("Please enter a valid Course ID.")
        
while True:

    user_input = input("\nEnter a Course ID (1-15), or enter quit to exit: ")

    if user_input.lower() == "quit":
        print("The value quit has been used to exit.")
        break

    if user_input == "0":
        print("Course ID is out of range (1-15), try again.")
        continue

    try:
        course_id = int(user_input)
        found = False

        for course in departments:
            if course[0] == course_id:
                print("Course ID", course_id, "is in the", course[1], "department.")
                found = True
                break

        if not found:
            print("Course ID not found.")

    except ValueError:
        print("Please enter a valid Course ID.")
course_data = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]
try:
    search_id = int(input("\nEnter a Course ID to retrieve course information: "))

    found = False

    for course in course_data:
        if course[0] == search_id:

            print("\nCourse Information")
            print("Course ID:", course[0])
            print("Course Name:", course[1])
            print("Department:", course[2])
            print("Prerequisites:", course[3])

            found = True
            break

    if not found:
        print("Error: Course ID not found.")

except ValueError:
    print("Error: Please enter a valid number.")