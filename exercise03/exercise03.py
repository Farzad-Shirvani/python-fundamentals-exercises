second_passed = int(input())

hour = second_passed // 3600
remaining = second_passed % 3600
minute = remaining // 60
second = remaining % 60

print(f"{hour} : {minute} : {second}")