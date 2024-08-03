
import json


def employees_rewrite(sort_type):
    valid_sort_types = ['firstName', 'lastName', 'department', 'salary']

    # Преобразование sort_type к нижнему регистру
    sort_type_lower = sort_type.lower()

    if sort_type_lower not in [x.lower() for x in valid_sort_types]:
        raise ValueError('Bad key for sorting')

    try:
        with open('employees.json') as f:
            data = json.load(f)
            # Преобразование всех ключей к нижнему регистру
            data["employees"] = [{k.lower(): v for k, v in employee.items()} for employee in data["employees"]]
    except FileNotFoundError:
        print("File 'employees.json' not found.")
        return

    sorted_data = {
        "employees": sorted(data["employees"], key=lambda x: x[sort_type_lower], reverse=(sort_type_lower == 'salary'))
    }

    with open(f'employees_{sort_type_lower}_sorted.json', 'w') as outfile:
        json.dump(sorted_data, outfile, indent=4)


# Пример использования с разными буквами
employees_rewrite('FirstName')
employees_rewrite('LASTNAME')
employees_rewrite('Department')
employees_rewrite('SALARY')