# -------------------------/1/-------------------------------

# Una reconocida productora de contenidos audiovisuales está en busca de nuevas ideas para su próximo proyecto, que promete cautivar al público.

# Las posibles temáticas para explorar son las siguientes:
# • Comedia
# • Ciencia ficción
# • Drama

# Para ello, la empresa ha decidido realizar una encuesta entre sus empleados para recopilar información valiosa. Los datos para recopilar por cada empleado son los siguientes:

# A) Información a ingresar por cada empleado encuestado:
# • Nombre del empleado
# • Edad (debe ser mayor o igual a 18)
# • Género (Masculino - Femenino)
# • Temática de interés (Comedia, Ciencia ficción, Drama)

# B) Se deben cargar 10 encuestas a través de la terminal.

# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor edad.

accumulator_Science_Drama = 0
accumulator_NoComedia = 0
flag = 0
flag_2 = 0
old = 0

for i in range(10):
    while True:
        name = input("name of the employee: ")
        if name.isdigit() or len(name) < 3:
            print("Ups!, you must enter a real name")
        else:
            break

    while True:
        age = input("Enter your age: ")
        if age.isalpha():
            print("must contain numbers")
        if int(age) < 18:
            print("You must be of legal age")
        if old < int(age):
            old = int(age)
            flag_2 = 1
            break
        else:
            break

    while True:
        gender = input("you must enter your gender: ")
        if gender.isdigit():
            print("you must enter male or female")
        if gender.lower() == "male" or gender.lower() == "female":
            if gender.lower() == "male":
                flag = 1
                break
            else:
                break
        print("you must enter male or female")

    while True:
        theme = input("you must place (Comedy, Science fiction, Drama): ")
        theme = theme.lower()
        if theme == "science fiction" or theme == "drama":
            if flag_2:
                theme_old = theme

            if flag and (int(age) >= 25 and int(age) <= 50):
                accumulator_Science_Drama += 1
                flag = 0
                break
            elif flag and (int(age) < 30 or int(age) > 40):
                accumulator_NoComedia += 1
                flag = 0
                break
            else:
                break
        if theme == "comedy":
            if flag_2:
                theme_old = theme
                flag_2 = 0
                break
            else:
                break   
        else:
            print("It must be one of these (Comedy, Science fiction, Drama)")

print(f"number of employees who voted (Science fiction, Drama): {accumulator_Science_Drama}")
print(f"The percentage of employees who did not vote for Comedy: {int(accumulator_NoComedia/10 * 100)}")
print(f"The name and topic of interest voted on by the oldest male employee, theme: {theme_old} and old: {old}")