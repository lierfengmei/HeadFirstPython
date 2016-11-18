
import cgitb
cgitb.enable()

import cgi
import athletemodel
import yate


athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Athlete's timing data:"))
#print(yate.para(athlete_name+"'s time data:"))
print(yate.header("Athlete:" + athlete_name + ",DOB = " +athlete[athlete_name].dob+ '.'))
print(yate.para("The top times for this athletes are:"))
print(yate.u_list(athletes[athlete_name].top3))

print(yate.include_footer({"Home":"index.html","Choose another athlete":"generate_list.py"}))

