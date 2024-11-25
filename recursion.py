
def sum_nested_list(nested_list):

    total = 0
    for element in nested_list:
        if isinstance(element, list): 
            total += sum_nested_list(element)  
        else:
            total += element  
    return total


def generate_permutations(s):

    if len(s) == 1:
        return [s] 

    permutations = []
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(s[i] + perm)

    return list(set(permutations))  


def calculate_directory_size(directory):
 
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict): 
            total_size += calculate_directory_size(value)
        else:
            total_size += value  
    return total_size



nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print("Task 1 - Total sum of nested list:", sum_nested_list(nested_list))  


print("Task 2 - Permutations of 'abc':", generate_permutations("abc"))
print("Task 2 - Permutations of 'aab':", generate_permutations("aab"))


directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}
print("Task 3 - Total size of the directory:", calculate_directory_size(directory_structure))
