import re

pattern = "((?:red|blue) flag)"
txt1 = 'red flag blue flag'
txt2 = 'yellow flag red flag blue flag green flag'
txt3 = 'pink flag red flag black flag blue flag green flag red flag'
txt4 = 'blue flag red flag red flag blue flag green flag red flag'


print(re.findall(pattern, txt1), ['red flag', 'blue flag'])
print(re.findall(pattern, txt2), ['red flag', 'blue flag'])
print(re.findall(pattern, txt3), ['red flag', 'blue flag', 'red flag'])
print(re.findall(pattern, txt4), ['blue flag', 'red flag', 'red flag', 'blue flag', 'red flag'])
