import math

def cal_check(x, y, z):
    
    operations = [
        ((x >> 8) + y) ** z,  
        (x & y) % z,          
        round(x / y) >> z,    
        math.ceil((2 + x) / y) | z  
    ]

    total_sum = sum(operations)
    
    results = [f"rs {i+1}: {op}" for i, op in enumerate(operations)]
    results.append(f"Sum of all rs: {total_sum}")

    conditions = {
        "cd not ( x=y ) or (y<z)": not (x == y) | (y < z),
        "cd x != y << z": x != (y << z)
    }

    for result in results:
        print(result)

    for cond, is_true in conditions.items():
        print(f"{cond} = {is_true}")

values = [int(input(f"input {var}: ")) for var in ['x', 'y', 'z']]
cal_check(*values)