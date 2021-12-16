def random_stu(age,last_name, first_name,gpa, passing):
    next_year = age +1
    full_name = first_name+" , " + last_name
    new_gpa = gpa + 1
    if passing == False:
        redo_grade = True
    else:
        redo_grade = False
    return next_year,full_name,new_gpa,redo_grade