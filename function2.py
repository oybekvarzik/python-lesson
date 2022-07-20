def format_name(f_name, l_name):
    if f_name==" " or l_name==" ":
      return "you didn't provide valid name."
    f_f_name=f_name.title()
    l_l_name=l_name.title()
    return f" Result: {f_f_name} {l_l_name}"

formating_string=format_name(input("what is your first name?"), input("what is your last name?"))
print(formating_string)
