#regular expression

import re
text = "Welcome to StepIn"
x = re.findall("[e-m]", text)
print(x)

y = re.search("Step", text)
print(y)
