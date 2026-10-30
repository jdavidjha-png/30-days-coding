def track_marks():
    # 3 sample entries ke sath dictionary initialize karna
    marks_dict = {
        "Maths": 85,
        "Physics": 78,
        "Computer Science": 92
    }
    
    # Naya subject aur uske marks add karna
    new_subject = "English"
    new_marks = 88
    marks_dict[new_subject] = new_marks
    
    # Empty case handle karne ke liye check
    if not marks_dict:
        print("No marks data available.")
        return

    marks_list = list(marks_dict.values())
    
    # Average aur highest mark calculate karna
    average_mark = sum(marks_list) / len(marks_list)
    highest_mark = max(marks_list)
    
    print("Subjects and Marks:", marks_dict)
    print(f"Average Mark: {average_mark:.2f}")
    print(f"Highest Mark: {highest_mark}")

track_marks()