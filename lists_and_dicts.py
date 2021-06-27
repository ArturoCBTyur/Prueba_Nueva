def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Yhojan DJE","lastname": "Jara Eugenio"}

    super_list =[
        {"firstname": "Yhojan","lastname": "Jara"},
        {"firstname": "Daniel","lastname": "Eugenio"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, 0, 1, 2, 3],
        "float_nums":[2.5, 1.2, 10.7]
    }

    for key, value in super_dict.items():
        print(f"Llave: {key} ; Valor: {value}")


if __name__ == "__main__":
    main()