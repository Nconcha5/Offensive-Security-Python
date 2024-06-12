from subprocess import check_output as retrieve

Raw = retrieve(['netsh','wlan','show','profiles']).decode('utf-8').split("\n")
Profiles = [x.split(":")[1][1:-1] for x in Raw if "All User Profile" in x]

file_name = "Passwords.dat"

with open(file_name, "w") as file:
    for profile in Profiles:
        Dig = retrieve(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split("\n")
        Result = [x.split(":")[1][1:-1] for x in Dig if "Key Content" in x]
        try:
            string = "{:<} | {:<}".format(profile, Result[0])
        except IndexError:
            string = "{:<} | NULL".format(profile)

        file.write(string + "\n")

print("Code Executed Successfully...")
