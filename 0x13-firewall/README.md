# FIREWALL

In computing, a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.A firewall typically establishes a barrier between a trusted internal network and untrusted external network, such as the Internet.

Firewalls are often categorized as either network firewalls or host-based firewalls. Network firewalls filter traffic between two or more networks and run on network hardware. Host-based firewalls run on host computers and control network traffic in and out of those machines.

## Types

Firewalls are generally categorized as network-based or host-based. Network-based firewalls are positioned on the gateway computers of LANs, WANs and intranets. They are either software appliances running on general-purpose hardware, or hardware-based firewall computer appliances. Firewall appliances may also offer other functionality to the internal network they protect, such as acting as a DHCP or VPN server for that network.Host-based firewalls are positioned on the host itself and control network traffic in and out of those machines. The host-based firewall may be a daemon or service as a part of the operating system or an agent application such as endpoint security or protection. Each has advantages and disadvantages. However, each has a role in layered security.

Firewalls also vary in type depending on where communication originates, where it is intercepted, and the state of communication being traced.

### Network layer or packet filters
Network layer firewalls, also called packet filters, operate at a relatively low level of the TCP/IP stack, blocking packets unless they match the established rule set. The firewall administrator may define the rules; or default rules may apply.

Network layer firewalls generally fall into two sub-categories, stateful and stateless.

Commonly used packet filters on various versions of Unix are ipfirewall (FreeBSD, Mac OS X (< 10.7)), NPF (NetBSD), PF (Mac OS X (> 10.4), OpenBSD, and some other BSDs), iptables/ipchains (Linux) and IPFilter. Prior to iptables, ipchains was the predominant software package for creating Linux firewalls.

### Application-layer
Application-layer firewalls work on the application layer of the Internet protocol suite (e.g., browser, telnet or FTP traffic), and may intercept all packets traveling to or from an application. Application firewalls function by determining whether a process should accept any given connection. Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. Application firewalls that hook into socket calls are also referred to as socket filters.

The extent of the filtering that occurs is defined by the provided rule set. Given the variety of software that exists, application firewalls only have more complex rule sets for the standard services, such as sharing services. Application firewalls work much like a packet filter but application filters apply filtering rules (allow/block) on a per-process basis instead of filtering connections on a per-port basis. Generally, prompts are used to define rules for processes that have not yet received a connection. It is rare to find application firewalls not combined or used in conjunction with a packet filter.

Per-process rule sets used by application firewalls have limited efficacy in filtering every possible association that may occur with other processes. Also, these per-process rule sets cannot defend against modification of the process via exploitation, such as memory corruption exploits. Because of these limitations, application firewalls are beginning to be supplanted by a new generation of application firewalls that rely on mandatory access control (MAC), also referred to as sandboxing, to protect vulnerable services.

### Proxies
A proxy server (running either on dedicated hardware or as software on a general-purpose machine) may act as a firewall by responding to input packets (connection requests, for example) in the manner of an application, while blocking other packets. A proxy server is a gateway from one network to another for a specific network application, in the sense that it functions as a proxy on behalf of the network user.

Proxies make tampering with an internal system from the external network more difficult, so that misuse of one internal system would not necessarily cause a security breach exploitable from outside the firewall (as long as the application proxy remains intact and properly configured). Conversely, intruders may hijack a publicly reachable system and use it as a proxy for their own purposes; the proxy then masquerades as that system to other internal machines. While use of internal address spaces enhances security, crackers may still employ methods such as IP spoofing to attempt to pass packets to a target network.

### Network address translation
Firewalls often have network address translation (NAT) functionality, and the hosts protected behind a firewall commonly have addresses in a "private address range", such as those defined in RFC 1918 for IPv4.