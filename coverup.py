#this code was written by Nikolas Coleman and is intended for use on linux operating systems
import subprocess


subprocess.call(['clear'])
print ("   _   _   _   _   _   _   _  ")
print ("  / \ / \ / \ / \ / \ / \ / \ ")
print (" ( C ) O ) V ) E ) R ) U ) P )")
print ("  \_/ \_/ \_/ \_/ \_/ \_/ \_/ ")
print ("    Code by: Nikolas Coleman  ")
print ("")
while True:
    print ("Select a coverup option (Press q to quit):")
    print ("1.Clear auth.log file")
    print ("2.Clear user bash history")
    print ("3.Delete bash history file")
    print ("4.Send all bash history to /bash/null")
    print ("5.Clear current session history")
    print ("6.Set history maxcommands to 0")
    print ("7.Set history maxcommands to 0")
    print ("8.Disable history logging (logout to take effect)")
    print ("9.ALL THE ABOVE")
    print ("")
    option = input("Please enter the number you have chosen:")
    if option == "1":
        print ("Clearing auth.log file...")
        subprocess.call(['echo "" /var/log/auth.log'])
        print ("File cleared.")
    elif option == "2":
        print ("Clearing user bash history...")
        subprocess.call (['echo "" ~/.bash_history'])
        print ("User bash history cleared.")
    elif option == "3":
        confirm = input ("You have chosen to delete the bash history file.\n\
    Are you sure you want to do this? (y/n):")
        #I should probably change sting from uper to lower automaticly
        if confirm == "y":
            print ("Deleting bash history file...")
            subprocess.call(['rm ~/.bash_history -rf'])
            print ("File deleted.")
        elif confirm == "Y":
            print ("Deleting bash history file...")
            subprocess.call(['rm ~/.bash_history -rf'])
            print ("File deleted.")
        elif confirm == "n":
            print ("COVERUP will now shutdown.")
            exit()
        elif confirm == "N":
            print ("COVERUP will now shutdown.")
            exit() 
    elif option == "4":
        print ("Sending all history to /dev/null...")
        subprocess.call (['ln /dev/nul ~/.bash_history -sf'])
        print ("All bash history sent to /dev/null.")
    elif option == "5":
        print ("Clearing current session history...")
        subprocess.call (['history -c'])
        print ("Current session history cleared.")
    elif option == "6":
        print ("Setting history maxlines to 0...")
        subprocess.call (['export HISTFILESIZE=0'])
        print ("History maxlines set to 0.")
    elif option == "7":
        print ("Setting history maxcommands to 0...")
        subprocess.call (['export HISTSIZE=0'])
        print ("History maxcommands set to 0.")
    elif option == "8":
        print ("Disabling history log...")
        subprocess.call (['unset HISTFILE'])
        print ("History log disabled.")
        confirm2 = input ("You have chosen to disable the history log.\n\
    Would you like to restart your computer in order\n\
    for this to take effect? (y/n):")
        if confirm2 == "y":
            print ("Computer will now restart...")
            subprocess.call (['sudo reboot'])
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "Y":
            print ("Computer will now restart...")
            subprocess.call (['sudo reboot'])
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "n":
            print ("COVERUP will now shutdown.")
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "N":
            print ("COVERUP will now shutdown.")
            exit()
            subprocess.call (['exit'])
    elif option == "9":
        print ("Clearing auth.log file...")
        subprocess.call (['echo "" /var/log/auth.log'])
        print ("Auth.log file cleared.")
        print ("Clearing user bash history...")
        subprocess.call (['echo "" ~/.bash_history"])
        print ("User bash history cleared.")
        confirm = input ("You have chosen to delete the bash history file.\n\
    Are you sure you want to do this? (y/n):")
        if confirm == "y":
            print ("Deleting bash history file...")
            subprocess.call(['rm ~/.bash_history -rf'])
            print ("File deleted.")
        elif confirm == "Y":
            print ("Deleting bash history file...")
            subprocess.call(['rm ~/.bash_history -rf'])
            print ("File deleted.")
        elif confirm == "n":
            print ("COVERUP will now shutdown.")
            exit()
        elif confirm == "N":
            print ("COVERUP will now shutdown.")
            exit()
        print ("Sending all history to /dev/null...")
        subprocess.call (['ln /dev/nul ~/.bash_history -sf'])
        print ("All bash history sent to /dev/null.")
        print ("Clearing current session history...")
        subprocess.call (['history -c'])
        print ("Current session history cleared.")
        print ("Setting history maxlines to 0...")
        subprocess.call (['export HISTFILESIZE=0'])
        print ("History maxlines set to 0.")
        print ("Setting history maxcommands to 0...")
        subprocess.call (['export HISTSIZE=0'])
        print ("History maxcommands set to 0.")
        print ("Disabling history log...")
        subprocess.call (['unset HISTFILE'])
        print ("History log disabled.")
        confirm2 = input ("You have chosen to disable the history log.\n\
    Would you like to restart your computer in order\n\
    for this to take effect? (y/n):")
        if confirm2 == "y":
            print ("Computer will now restart...")
            subprocess.call (['sudo reboot'])
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "Y":
            print ("Computer will now restart...")
            subprocess.call (['sudo reboot'])
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "n":
            print ("COVERUP will now shutdown.")
            exit()
            subprocess.call (['exit'])
        elif confirm2 == "N":
            print ("COVERUP will now shutdown.")
            exit()
            subprocess.call (['exit'])
    elif option == "q":
        break
    elif option == "Q":
        break
    
    
    
    
    
    

    
               
    
