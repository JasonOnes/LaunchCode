def factors(number):
    factor_list = []
    for i in range(1, number+1):
        if number % i == 0:
            factor_list.append(i)
    return factor_list

def factor_dict(number):
    fact_dict = {}
    for num in range(1, number+1):
        fact_dict[num] = factors(num)
    return fact_dict 

def factor_dict2(number):
    fact_dict = {num : factors(num) for num in range(1, number+1)}
    return fact_dict 
 
def reverse_dict(dict_name):
    reverse_dict = {tuple(v):k for k, v in dict_name.items()}
    return reverse_dict

print(factor_dict(15))
print(factor_dict2(15))
print(reverse_dict(factor_dict(15))) 