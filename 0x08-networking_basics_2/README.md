# Networking basics #1

The general objectives are:

-What is localhost/127.0.0.1
-What is 0.0.0.0
-What is /etc/hosts
-How to display your machines active network interfaces

In computer networking, localhost is a hostname that means this computer. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware.

In the Internet Protocol Version 4, the address 0.0.0.0 is a non-routable meta-address used to designate an invalid, unknown or non-applicable target. This address is assigned specific meanings in a number of contexts, such as on clients or on servers

# Whats the Linux Hosts File?

The hosts file is a plain text file that all operating systems use to translate hostnames (also known as web addresses or URLs) into IP addresses. When you type in a hostname, such as wikipedia.org, your system will look into the hosts file to get the IP address needed to connect to the appropriate server.

If you open the hosts file, youll quickly notice that it doesnt have the directory of the entire internet in there. Instead, there might be just a couple lines and thats it. What gives?

Turns out, your system will check the hosts file first before looking up a site on the DNS servers defined in your network settings (usually your ISPs DNS servers).
