def process_command(command_input):
    # Convert to lowercase, strip whitespace, and slice to separate command and parameter
    command_input = command_input.lower().strip()
    cmd, para = command_input.split(',')
    cmd = cmd.strip()
    para = para.strip()
    
    # Show results based on command
    if cmd == 'on':
        print(f"cmd = {cmd}")
        print(f"para = {para}")
        print(f"Run On => {para}")
    elif cmd == 'off':
        print(f"cmd = {cmd}")
        print(f"para = {para}")
        print(f"Run Off => {para}")
    else:
        print("Unknown command")
        print(f"cmd = {cmd}")
        print(f"para = {para}")

# Example usage
input_str1 = input("Command (3), paramitor (2) : ")
process_command(input_str1)

input_str2 = input("Command (3), paramitor (2) : ")
process_command(input_str2)
