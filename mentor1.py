def matchingStrings(strings, queries):
    # Write your code here
    ans = []
    for i in range(0,len(queries)):
        ans.append(0)
    for i in range(0,len(queries)):
        while queries[i] in strings:
            strings.remove(queries[i])
            ans[i] += 1
    return ans

print(matchingStrings(['abcde',
'sdaklfj',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf',
'na',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf'],
[
    'abcde',
'sdaklfj',
'asdjf',
'na',
'basdn'
]))