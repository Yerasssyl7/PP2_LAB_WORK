def write_list_to_file(list_items, file_path):
    with open(file_path, mode='w') as file:
        for item in list_items:
            file.write(f"{item}\n")


write_list_to_file(["BMW", "Mercedes", "Porsche", "Ferrari"], './list_elements_cars.txt')
#qwerty