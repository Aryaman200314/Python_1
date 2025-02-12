def calculate(instnace, use):
    instnace_types = ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]
    if usage<0 or usage > 100:
        return "Usage out of bound"

    if instnace not in instnace_types:
        return "Please give an valid instance type"
    
    index = -1
    for x in range(len(instnace_types)):
        if instnace_types[x] == instnace:
            index = x
            break
    
    if usage<20:
        return f"Instance in under utilized you can use: {instnace_types[index-1]}"
    elif usage>80:
        return f"Instance in over utilized you can use: {instnace_types[index+1]}"
    else:
        return "you are using the correct one"
    

isntance_input = input("Enter your instance type: ")
usage = int(input("Enter currnet usage: "))

print(calculate(isntance_input, usage))