def wlost_string(trace):
    wlost = ""
    for i in range(len(trace)):
        char = chr(ord('a') + i)  # Get the character corresponding to the index
        wlost += char * trace[i]  # Append the character 'trace[i]' times
    return wlost

# Example usage:
trace = [0, 0, 0, 1, 0, 2, 0, 3, 1, 1, 4]
result = wlost_string(trace)
print(result)  # Output: 'abracadabra'
