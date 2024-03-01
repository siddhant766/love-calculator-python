his=str(input("What is your name: "))
her=str(input("What is her name: "))
combined=his+her
#print(combined)
lower_case=combined.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
true=t+r+u+e
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
love=l+o+v+e
score=str(true)+str(love)
print(score)
total=int(score)
if total<=10 or total>=90:
    print(f"your score is {total}, you both are like coke and mentos")
if 40<=total<=50:
    print(f"your score is {total}, you are good together")
else:
    print(f"your score is {total}")