weight=int(input("enter weight:"))
height=float(input("enter height:"))
print(f"Weight:{weight}")
print(f"Height:{height}")
bmi=weight/(height*height)
print(f"BMI {bmi}")
if(bmi<18.5):
    print("under weight")
elif bmi>18.5 and  bmi<=24.9 :
    print("normal")
elif bmi>=25 and bmi<=29.9 :
    print("over weight")
else:    
  print("obesity")
