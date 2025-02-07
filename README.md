# Problem Statement And Solution:

 Scenario There is a customer who came to you with a problem to have a custom linux
command for his operations. Our task is to understand the problem and create a linux
command via bash script as per the instructions.

* Command name - internsctl
* Command version - v0.1.0
# Section A
1. I want a manual page of command so that I can see the full documentation of the command.
For example if you execute the command
man ls
as output we get the doc and usage guidelines. Similarly if I execute man internsctl I want
to see the manual of my command.
2. Each linux command has an option --help which helps the end user to understand the use
cases via examples. Similarly if I execute internsctl --help it should provide me the
necessary help

3. I want to see version of my command by executing
internsctl --version
---
* <b>Solution:</b>

<b>step-1:</b> #!/bin/bash

function display_help() {
    echo "Usage: internsctl [OPTIONS]"
    echo "Custom Linux Command for Operations"
    echo ""
    echo "Options:"
    echo "  --help"
    echo "  --version"
}

function display_version() {
    echo "internsctl v0.1.0"
}

case "$1" in
    --help)
        display_help
        ;;
    --version)
        display_version
        ;;
    *)
        echo "Invalid option. Use 'internsctl --help' for usage guidelines."
        exit 1
        ;;
esac

<b>step-2:</b> chmod +x internsctl.sh

<b>step-3:</b> ./internsctl.sh --help

<b>step-4:</b> ./internsctl.sh --version

---

# Section B
I want to execute the following command for -
* Part1 | Level Easy
I want to get cpu information of my server through the following command:

$ internsctl cpu getinfo
Expected Output -
I want similar output as we get from lscpu command

I want to get memory information of my server through the following command:
$ internsctl memory getinfo
Expected Output
I want similar output as we get from free command

---
* <b>Solution:</b>

<b>step-1:</b> Just add bash script in above program : 

  function display_help() {
    echo "  cpu getinfo"
    echo "  memory getinfo "
  }

<b>step-2:</b> function get_cpu_info() {
    lscpu
}

function get_memory_info() {
    free
}


case "$1" in
cpu)
        if [ "$2" == "getinfo" ]; then
            get_cpu_info
        else
            echo "Invalid subcommand for 'cpu'. Use 'internsctl cpu getinfo'."
            exit 1
        fi
        ;;
    memory)
        if [ "$2" == "getinfo" ]; then
            get_memory_info
        else
            echo "Invalid subcommand for 'memory'. Use 'internsctl memory getinfo'."
            exit 1
        fi
        ;;
    *)
        echo "Invalid option. Use 'internsctl --help' for usage guidelines."
        exit 1
        ;;
esac

<b>step-3:</b> chmod +x internsctl.sh

<b>step-4:</b> ./internsctl.sh cpu getinfo & 
                ./internsctl.sh memory getinfo

---

* Part2 | Level Intermediate
I want to create a new user on my server through the following command:
$ internsctl user create <username>
Note - above command should create user who can login to linux system and access his home
directory

I want to list all the regular users present on my server through the following command:
$ internsctl user list

If want to list all the users with sudo permissions on my server through the following command:
$ internsctl user list --sudo-only

---

* <b>Solution:</b>

<b>step-1:</b> 
function display_help() {
echo "  user create <username> Create a new user"
    echo "  user list"
    echo "  user list --sudo-only"
}

<b>step-2:</b> 
function create_user() {
    if [ -z "$2" ]; then
        echo "Error: Missing username. Usage: internsctl user create <username>"
        exit 1
    fi
sudo useradd -m "$2"
echo "User '$2' created successfully."
}

function list_users() {
    cut -d: -f1 /etc/passwd
}


function list_sudo_users() {
    getent group sudo | cut -d: -f4 | tr ',' '\n'
}

<b>step-3:</b>  
case "$1" in
user)
        if [ "$2" == "create" ]; then
            create_user "$@"
        elif [ "$2" == "list" ]; then
            if [ "$3" == "--sudo-only" ]; then
                list_sudo_users
            else
                list_users
            fi
        else
            echo "Invalid subcommand for 'user'. Use 'internsctl user create <username>' or 'internsctl user list [--sudo-only]'."
            exit 1
        fi
        ;;
    *)
        echo "Invalid option. Use 'internsctl --help' for usage guidelines."
        exit 1
        ;;
esac

<b>step-4:</b> chmod +x internsctl.sh

<b>step-5:</b> 
1. ./internsctl.sh user create testuser
2. ./internsctl.sh user list
3. ./internsctl.sh user list --sudo-only

---
