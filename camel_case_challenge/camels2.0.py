sample1 = "helloWorld"
sample2 = "helloworld"
sample3 = "helloWorldWorld"
sample4 = "HelloWorldWorld"

def solution(input_string):
    return input_string[0] + ''.join(' ' + char if char.isupper() else char for char in input_string[1:])

print(solution(sample4))