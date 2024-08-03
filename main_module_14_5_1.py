import json

def employees_rewrite(sort_type):
    if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
        raise ValueError('Bad key for sorting')

    with open('employees.json') as f:
        data = json.load(f)
        sorted_data = {"employees": sorted(data["employees"], key=lambda x: x[sort_type], reverse=sort_type=='salary')}

    with open(f'employees_{sort_type}_sorted.json', 'w') as outfile:
        json.dump(sorted_data, outfile, indent=4)

# Example usage
employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')
