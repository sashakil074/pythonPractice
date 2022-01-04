""""

1. Do the following tasks
a. Create a module "employee_status"
This module should have a function that specify if an employee is a full-time or
part-time "em_st", and function to compute the bonus an employee deserves
‘bonus’
b. Create a module with the name "status_test"
c. Import the module "employee_status" in different ways and use the available
functions
d. Move the "employee_status" into a package of the name status, do the required
corrections
e. Create a new module inside status package, and give us some info about your
package using a documentation string, module name "info"

"""


from status import employee_status

employee_status.em_st('Asif',8)

from status.employee_status import bonus
bonus("Asif",5,100000)

from status import info as i
print(help(i))