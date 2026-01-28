jon = input()
doctor = input()

jon_a = jon.count("a")
doctor_a = doctor.count("a")

if jon_a < doctor_a:
    print("no")
else:
    print("go")