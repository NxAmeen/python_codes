# import re

# txt = "learn python"
# pattern = '[ler]'
# x = re.findall(pattern, txt)  

# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")



# import re

# txt = "learn python"
# pattern = '^l'
# x = re.findall(pattern, txt)  

# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")



# import re

# txt = "learn python"
# pattern = 'n$'
# x = re.findall(pattern, txt)  

# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")



# import re

# txt = "learn python"
# pattern = '\s'
# x = re.split(pattern, txt)  

# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")



import re

txt = "learn python"
pattern = '\s'
x = re.sub(pattern, " Java ", txt)  
print(x)