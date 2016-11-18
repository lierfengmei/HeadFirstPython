import  os
#os.chdir("E:\PythonLearning\HeadFirstPython\chapter7\webapp\cgi-bin")
#print(os.getcwd())
import  yate
import athletemodel
import glob


data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response)
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list ot work with!"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete",athletes[each_athlete].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))
