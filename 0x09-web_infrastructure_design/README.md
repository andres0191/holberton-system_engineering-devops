# Web Infrastructure desing

Whether you are beginning to plan for the launch of a large website or managing the growing pains of an existing site, you will quickly come to the point where one server is not enough to handle the traffic to your site, or you need more reliability than a single server can provide. However, the leap from a single server to a multiserver infrastructure is a large one. There are a number of ways to architect your environment to ensure fast response times to your visitors and allow you the potential to further scale in the future.

Your infrastructure design will vary greatly based on your website’s requirements. What kind of high availability do you require? What response times will your users or your management consider acceptable? Does your site require any “extra” services or applications, outside of a standard LAMP stack? All of these considerations and (of course, expected traffic to the site) will need to be taken into account when designing, building, and maintaining a multiserver hosting environment. There is no silver bullet solution for everyone, but we can provide some guidelines that should make it easy to find the right solution for your particular needs.

Horizontal and Vertical Scaling
There are two approaches to scaling out an infrastructure to add additional resources: horizontal scaling (“scaling out”) and vertical scaling (“scaling up”). Horizontal scaling involves adding additional servers while vertical scaling involves adding more resources to existing servers. A good infrastructure plan will take both of these scaling approaches into account, as there are times when one may be more appropriate than the other. Initially, this consideration may be used to consider when to migrate from one server to multiple servers. 

The principal concept are:

Network basics
Server
Web server
DNS
Load balancer
Monitoring
Julien’s talk #0 (The audio quality is a bit rough. We recommend using the subtitles as an aid but don’t rely too much on them. You may need to raise the volume a bit.)
Julien’s talk #1 (The audio quality is a bit rough. We recommend using the subtitles as an aid but don’t rely too much on them. You may need to raise the volume a bit.)
What is a database
What’s the difference between a web server and an app server?
DNS record types
Single point of failure
How to avoid downtime when deploying new code
High availability cluster (active-active/active-passive)
What is HTTPS
What is a firewall



