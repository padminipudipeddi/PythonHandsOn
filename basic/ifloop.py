def say_hello_to_first_name(list_names):
    for name in list_names:
        if name == 'Padmini':
            return 'Hello ' + name + '! Welcome To Programmimg'
        else:
            pass
    return "no Padmini first name found"


if __name__ == "__main__":
    first_names = ['Sai', 'Pudipeddi', 'Prahlada', 'Meenakshi']
    result = say_hello_to_first_name(first_names)
    print(result)
