from subprocess import check_output as retrive

Raw = retrive(['netsh','wlan','show','profiles']).decode('utf-8').split("\n")
Proflies = [x.split(":")[1][1:-1] for x in Raw if "All User Profile" in x]

file_name = "Passwords.dat"

with open(file_name, "w")
    for profile in Profiles:
        Dig = retrive(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split("\n")
        Result = [x.split(":")[1][1:-1] for x in Dig if "Key Content" in x]
        try:
            string = "{:<} | {:<}".format(profile, Result[0])
        except Exception as Error:
            string = "{:<} | NULL".format(profile)

        File.write(string + "\n")

print("Code Executed Successfully...")