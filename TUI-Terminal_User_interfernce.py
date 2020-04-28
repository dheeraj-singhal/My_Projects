import os
import getpass

os.system("tput setaf 1")
print("\t\tHey welcome to my TUI thats life simple.")
os.system("tput setaf 7")
print("\t\t----------------------------------------")

passwd = getpass.getpass("Enter your password : ")
actual_passwd = "redhat"

if passwd != actual_passwd:
    print("Auth incorrect")
    exit()

location = input("Where you would like to perform your job (local/remote): ")
if location == "remote":
    remoteIP = input("Enter your IP : ")
while True:
    print("""
    Press 1 : to see date
    Press 2 : to check calender
    Press 3 : to launch firefox
    Press 4 : to see IP address
    Press 5 : to conf server
    Press 6 : to create user
    Press 7 : to create file
    Press 8 : to setup n/w
    Press 9 : docker services
    Press 10 : to check free memory
    Press 11 : to exit
    """)

    ch = int(input("Enter your choice : "))

    if location == "local":
        if ch == 1:
            os.system("date")
        elif ch == 2:
            os.system("cal")
        elif ch == 3:
            os.system("firefox")
        elif ch == 4:
            os.system("ifconfig")
        elif ch == 5:
            os.system("yum install httpd")
        elif ch == 6:
            create_user = input("Can you please tell user name : ")
            os.system("useradd {}".format(create_user))
        elif ch == 7:
            file_location = input("Enter the location where you want to create file : ")
            file_name = input("Enter the file name : ")
            os.system("cd {0}".format(file_location))
            os.system("gedit {0}".format(file_name))
            os.system("cd")
        elif ch == 8:
            os.system("date")
        elif ch == 9:
            while True:
                print("""
    Press 1 : to check docker version
    Press 2 : to show all running docker images
    Press 3 : to show all docker images installed in the system
    Press 4 : to install docker image
    Press 5 : to launch new docker image
    Press 6 : to run pre uesd docker image
    Press 7 : to check docker info
    Press 8: to return back to main menu 
                """)
                doc = int(input("Enter your choice : "))
                if doc == 1:
                    os.system("docker version")
                elif doc == 2:
                    os.system("docker ps")
                elif doc == 3:
                    os.system("docker images")
                elif doc == 4:
                    image = input("Enter the name of image you want to install [in format (image:version)] : ")
                    os.system("docker pull {0}".format(image))
                elif doc == 5:
                    docker_image = input("Enter the name of image you want to run [in format (image:version)] : ")
                    print("\tPress 1 : to run with specific name\n\tPress 2 : else continue")
                    img = int(input("Enter your choice : "))
                    if img == 1:
                        docker_name = input("Enter the name of image : ")
                        os.system("docker run -t -i --name {0} {1}".format(docker_name,docker_image))
                    elif img == 2:
                        os.system("docker run -t -i {0}".format(docker_image))
                    else :
                        print("option doesnt support")
                elif doc == 6:
                    img_name = input("Enter the name of image : ")
                    os.system("docker attach {0}".format(img_name))
                elif doc == 7:
                    os.system("docker info")
                elif doc == 8:
                    break
                else :
                    print("option doesnt support")
                input("Enter to continue....")
                os.system("clear")
        elif ch == 10:
            os.system("free -m")
        elif ch == 11:
            print("Bye...!!!")
            exit()
        else:
            print("option doesnt support")
        input("Enter to continue....")
        os.system("clear")
    elif location == "remote":
        if ch == 1:
            os.system("ssh {0} date".format(remoteIP))
        elif ch == 2:
            os.system("ssh {0} cal".format(remoteIP))
        elif ch == 3:
            os.system("ssh {0} yum install httpd".format(remoteIP))
        elif ch == 4:
            create_user = input("Can you please tell user name : ")
            os.system("ssh {0} useradd {1}".format(remoteIP, create_user))
        elif ch == 5:
            os.system("date")
        elif ch == 6:
            os.system("date")
        elif ch == 8:
            print("Bye...!!!")
            exit()
        else:
            print("option doesnt support")
        input("Enter to continue....")
        os.system("clear")
    else:
        print("Location doesnt support")
        break
