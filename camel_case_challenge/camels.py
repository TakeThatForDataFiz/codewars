sample1 = "helloWorld"
sample2 = "helloworld"
sample3 = "helloWorldWorld"
sample4 = "HelloWorldWorld"

def solution(input_string):
    output_string = input_string
    chars_added = 0
    for i, char in enumerate(input_string):
        if char.isupper() and i > 0:
            output_string = output_string[:i+chars_added] + " " + output_string[i+chars_added:]
            chars_added += 1
    return output_string

print(solution(sample4))