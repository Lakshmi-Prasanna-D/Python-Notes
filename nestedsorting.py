n=int(input("enter n  value\n"))
l=[]
for i in range(n):
    l1=[]
    print(f"enter the following details of employee{i+1}")
    print("enter empid:")
    empid=int(input())
    print("enter name:")
    name=input()
    print("enter job:")
    job=input()
    print("enter salary:")
    salary=int(input())
    print("grade:")
    grade=input()
    print("location")
    location=input()
    l1=[empid,name,job,salary,grade,location]
    l.append(l1)

    
print("the entered details are:")
print(l)
print("1.sort by name\n 2.sort by job \n 3. sort by salary\n 4.sort by location \n 5.sort by job and salary \n 6.sort by grade and job \n 7.grade , salary and job")

print("select your choice:")
ch=int(input())
match ch:
    case 1:
        name=sorted(l,key=lambda x:x[1])
        print(name)
    case 2:
        job=sorted(l,key=lambda x:x[2])
        print(job)
    case 3:
        salary=sorted(l,key=lambda x:x[3])
        print(salary)
    case 4:
        location=sorted(l,key=lambda x:x[5])
        print(location)
    case 5:
        job_salary=sorted(l,key=lambda x:(x[2],x[3]))
        print(job_salary)
    case 6: 
        grade_job=sorted(l,key=lambda x:(x[4],x[2]))
        print(grade_job)
    case 7:
        grade_salary_job(l,key=lambda x:(x[4],x[3],x[2]))
    case _:print("invalid")
        
                          
