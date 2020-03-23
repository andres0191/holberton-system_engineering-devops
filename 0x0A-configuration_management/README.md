

# Introduction to configuration management:

It is the process of systematically managing changes in a system in a way that maintains integrity over time. Automation plays an essential role in managing server configuration. It is the mechanism used to bring the server to a desirable state, previously defined by parovisioning scripts using the language and specific characteristics of a tool. Automation is indeed the heart of configuration management for servers, and that is why it is common to refer to configuration management tools as an automation tool as well.

Another term used to describe the automation features implemented by configuration management tools is "Server Orchestration and Orchestration".
There are a number of configuration management tools available on the market. Puppet, Ansible, Chef, Salt are popular options. Although each tool will have its own characteristics and function in slightly different ways, they are all driven by the same purpose: To ensure that the state of the system matches the state specified by your provisioning scripts.

Benefits of server configuration management:
Although the use of configuration management generally requires more planning and initial effort than manual system administration, all but the simplest server infrastructure will be enhanced by the benefits it provides. To name a few:

1. Rapid provisioning of new servers:

Automation makes provisioning much faster and more efficient because it enables tedious tasks to be performed faster and more accurately than any human. Even with adequate and comprehensive documentation, manual implementation of a web server, for example, could take hours compared to a few minutes with configuration management / automation.

2. Quick recovery of critical events:

When a server goes offline due to unknown circumstances, it can take several hours to properly audit the system and find out what really happened. In situations like this, implementing a replacement server is usually the safest way to get your services back online while performing a detailed inspection on the affected server. With configuration management and automation, this can be done quickly and reliably.

3. No more snowflake servers:

Over time it can be extremely difficult to know exactly what is installed on a server and what changes were made when the process is not automated. Manual reviews, configuration adjustments, and software updates can make servers unique snowflakes, difficult to manage, and even more difficult to replicate. When using a configuration management tool, the procedure for opening a new server or updating an existing one will be documented in the provisioning scripts.
4. Version control for the server environment:

Version control tools like Git can be used to track changes made in provisioning and to keep separate branches for legacy versions of scripts. You can also use version control to implement a code revision policy for provisioning scripts, where any changes must be submitted as a pull request and must be approved by a project leader before being accepted. This practice will add additional consistency to the configuration of your infrastructure.

5. Replicated environments:

Configuring production, development and test servers, and the use of local virtual machines for development created with the same provisioning crypts, will minimize the problems caused by environment discrepancies that frequently run when applications are deployed in production or are deployed. They share between coworkers with different machine configurations.

General description of configuration management tools:
Most configuration management tools use a controller / master - node / agent model. Essentially, the controller directs the configuration of the nodes, based on a series of instructions or tasks defined in its provisioning scripts.

# Most common features in most server admin tools:

1. Automation framework: Each tool provided a specific syntax and set of features that you can use to write provisioning scripts. Most of the tools will have features that will make their language similar to conventional programming languages, but in a simplified way. Variables, loops, and conditionals are common features provided to facilitate the creation of more truthful provisioning scripts.

2. Independent behavior: If a package has already been installed, the tool will not try to install it again, since it tracks the status of resources to avoid repeating tasks that have already been executed previously. The goal is that after each provisioning run, the system reaches or maintains the desired state, even if you run it multiple times. This is what characterizes these tools as having an independent behavior. However, this behavior does not necessarily apply in all cases.

3. System data: This data is available through global variables, known as facts. They include things like network interfaces, IP addresses, operating system, and distribution. Each tool will provide a different set of facts. It can be used to make provisioning scripts and templates more adaptable for multiple systems.

4. Template system: Templates generally support variables, loops, and conditionals that can be used to maximize versatility. For example, you can use a template to easily configure a new virtual host within Apache, while reusing the same template for multiple server installations. Rather than having only static encoded values, a template should contain placeholders for values ​​that can change from one host to another, such as NameServer and DocumentRoot.

5. Extensibility: CM tools tend to have a strong community built around them and users are encouraged to share their custom extensions. Using extensions provided by other users can save you a lot of time, while serving as a great way to learn how other users solved common problems using their tool of choice.

Choose a configuration management tool:
Popular options include Chef, Ansible, and Puppet. The first challenge is choosing a tool that fits your needs well. For that, there are a few things to keep in mind before making a decision:

1. Infrastructure complexity: Most configuration admin tools will require a minimum hierarchy consisting of a controlling machine and a node that will be managed by it. Puppet, for example, requires that an agent application be installed on each node and that a master application be installed on the controller machine. Ansible, on the other hand, has a decentralized structure that does not require the installation of additional software on the nodes, but instead relies on SSH to perform the provisioning tasks. For smaller projects, a simplified infrastructure may seem like a better option, however, it is important to consider aspects such as scalability and security, which the tool cannot apply.

2. Learning Curve: CM tools provide custom syntax, sometimes using a DSL domain-specific language, and a set of features that comprise your framework for automation. As with conventional programming languages, some tools will require that a higher learning curve be mastered. Infrastructure requirements can also influence the complexity of the tool and how quickly you can see a return on investment.

# ***Puppet Packages and Versions***


***Puppet's open source have two launch tracks:***
* Development releases: Puppet versions not associated with any PE version release a new minor version (or "and") approximately once a month. Development releases generally do not receive patch (or "z") releases. Each minor version in this sequence replaces the previous minor version.
* Long-term releases: Puppet versions associated with Puppet Enterprise get patch releases (or "z") a few times a year. Each version contains fixes and features of various development versions.
Important: To ensure you have the latest features, fixes and patches and security, update your version of Puppet whenever there is a new version in your release track.

***Puppet Packages:***
* puppet-agent: This package contains the puppet main code and all the necessary dependencies to run it, including Facter, Hiera and the included versions of Ruby and OpenSSL.

* Puppet server is a JVM-based application that, among other things, executes instances of the master application.
* Puppet and serves catalogs to nodes running the agent service. It has its own version number and can be compatible with more than one version of puppet. This package depends on puppet-agent.
* Puppetdb collects data generated by Puppet. It allows additional functions such as exported resources, advanced queries and reports on your infrastructure.

# ***Puppet's shell language: Modeling instead of scripting.***

Puppet uses a charitable language, Ppuppet is told how he wants the system to be, not the steps to get there. Especially for configuration management, this approach makes perfect sense. You shouldn't have to think about building a LAMP stack by installing Apache, MySQL and PHP. You should be able to specify what you need and have everything ready to go.

***Benefits of Puppet's declarative language:***
* The Puppet DSL is tested: Thousands of people use Puppet modules and have actually tested them for you. If you write a single script, you only have one user: you. So you are the person responsible for checking if it works, detecting and correcting every error.

* It’s repeatable: Once you run Puppet, it knows that the computer will be configured as it should be, in the state you have defined. And you can use a manifest to configure as many machines as you need, even on multiple platforms.

* Consistency: No matter what state your servers start in, once you run Puppet, they will end exactly as described. If you update your Puppet apache module, each Apache machine managed by Puppet will update to the new configuration automatically. your systems will throw fewer errors.

* You save time: It is much faster to run Puppet than to write a script. If a machine is accidentally configured incorrectly, Puppet will find the change and correct it (unless you run puppet in non-operational mode, which is definitely an option)

* Self-documentation: Puppet manifests are so simple that anyone can read and understand them, including people outside of your IT and engineering departments.

* Auditability: Many regulatory bodies accept Puppet manifests as proof of compliance. Whether it is an external or internal audit. Puppet's declarative language allows communicating the expected and desired state, not only to Puppet, but to the other humans on the team. It is easy to write and easy to read and understand.