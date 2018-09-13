import env
from cours_list import getlistcourses
from diff_module import diff_module

types = []
for type in env.Moodle._TYPES:

    types.append(env.Moodle._URLMOD + type + env.Moodle._VIEWID)

print(types)
def main():

       modules = getlistcourses()
       if modules:
           for module in modules:
               n = 0
               for type in types:
                   diff_module(module, type, env.Moodle._TYPES[n])
                   n += 1

while(1):
    main()

