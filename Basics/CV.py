
no_of_projects = int(input("Enter the total number of projects: "))
CV_Array = []
#creating n number of empty dictionaries
for i in range(no_of_projects):
 projects = {f"Project_{i+1}": {} }

#inserting mean and standard deviation values 
for i in range(no_of_projects):
    mean = float(input(f"Enter the mean for Project_{i+1}: "))
    standard_deviation = float(input(f"Enter the standard deviation for Project_{i+1}: "))
    projects[f"Project_{i+1}"] = {"Mean": mean, "Std_Dev": standard_deviation}
    if projects[f"Project_{i+1}"]["Mean"]!=0:
       CV = float(projects[f"Project_{i+1}"]["Std_Dev"]/projects[f"Project_{i+1}"]["Mean"])
       projects[f"Project_{i+1}"]["CV"]=CV 
       CV_Array.append(round(CV,6))
    else: 
       CV=0
       projects[f"Project_{i+1}"]["CV"]=CV 
       CV_Array.append(round(CV,6))


min_cv = min(CV_Array)
min_indices = []
for i in range(len(CV_Array)):
    if CV_Array[i] == min_cv: min_indices.append(i+1)

print("CV's of All Projects Starting from Project 1 (Left to Right):", CV_Array)
print("Least CV Value:",min_cv)
print("Projects with Low Risk:","Project:",min_indices)





