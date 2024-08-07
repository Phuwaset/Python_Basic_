import math

def cal_check(x, y, z):
    rs1 = ((x >> 8) + y) ** z
    rs2 = (x & y) % z          
    rs3 = round(x / y) >> z    
    rs4 = math.ceil((2 + x) / y) | z  

    results = [
        f"Cal ((x >> 8) + y) ** z = {rs1:.2f} ({int(rs1)})",
        f"Cal (x & y) % z = {rs2} ({int(rs2)})",
        f"Cal round(x / y) >> z = {rs3} ({int(rs3)})",
        f"Cal ((2 + x) / y) | z = {rs4} ({int(rs4)})",
    ]
    conditions = {
        "Check not ( x=y ) or (y<z)": not (x == y) | (y < z),
        "Check x != y << z": x != (y << z)
    }

    for result in results:
        print(result)

    for cond, is_true in conditions.items():
        print(f"{cond} = {is_true}")

values = [int(input(f"input {var}: ")) for var in ['x', 'y', 'z']]

cal_check(*values)
