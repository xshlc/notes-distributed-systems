
# 1 Computer Networks and the Internet

Overview is structured as:
1. **Basic terminology and concepts**
2. **Basic hardware and software components**
    1. Network's edge
    2. End systems
    3. Network applications running in the network
3. **The core of computer network**
    1. Links and switches that transport data
    2. Access networks and physical media that connect end systems to the network core
4. **The Internet is a network of networks**
    1. How do these networks connect with each other?
5. **Data in a computer network**
    1. Delay
    2. Loss
    3. Throughput
    4. Simple quantitative models for end-to-end throughput and delay
    5. Models that take into account transmission, propagation, and queuing delays
6. **Key architectural principles**
    6. Protocol layering
    7. Service models
7. **Security attacks**
    1. Examples of attacks
    2. How computer networks can be made more secure
8. **A brief history of computer networking**

## 1.1 What is the Internet?

Public internet is used as "the principle vehicle" for discussing things 

Internet  — a computer network that interconnects billions of computing devices throughout the world

   ***Note** that we can print the `em dash` or a "long hyphen" by doing `ctrl shift u` and typing `2014`.*

### 1.1.1 A "Nuts and Bolts" Description
- The basic hardware and software components that make up the Internet
	- Used to be desktops, laptops, workstations, and servers that store and transmit information like web pages and email message.
	- Now, many non-traditional devices also connect to the Internet. These devices are called the IoT (Internet of Things). 
		- Ex: smartphones, gaming consoles, home security systems, traffic control systems.
		- These devices are called **hosts** or **end systems**.
		- By 2015, ~5 billion devices connected to the Internet with ~3.2 billion Internet users worldwide (or ~40% of the world population) and by 2020, 25 billion. 
	- End systems - connected by a network of **communication** links and **packet switches**. 
		- Communication links - made up of different physical media (coaxial cable, copper wire, optical fiber, radio spectrum, etc.).
			- Different links can transmit at different rates. 
			- **Transmission rate** of a link - measured in *bits/second*.
- Data across a network.
	- The *sending* end system - segments the data, adds header bytes to each segment
	- The resulting packages are **packets**.
	- Packets are sent through the network to the destination end system.
	- The *destination* end system - reassembles packets into the original data.
- Packet switch - takes a packet arriving on one of the communication links and forwards that packet on one of its outgoing communication links. 
	- Two key types: **routers** and **link-layer switches**. 
	- Link-layer switches — typically used in access networks.
	- Routers — typically used in the network core.
	- **Route** or **path** through the network - sequence of communication links and packet switches traversed by a packet from the *sending* end system to the *receiving* end system.
	- IP traffic - the data moving throughout the network
- *Analogy*: Packet-switched networks are like transportation networks (highways, roads, and intersections).
	- Packet-switch network transports packets. Transportation network transports vehicles. 
	- Factory needs to move a large amount of cargo. 
		- Factory - divides and loads cargo onto trucks. 
		- Destination - cargo is unloaded and grouped by same shipment.
		- Packets are like trucks.
		- Communication links are like highways and roads.
		- Packet switches are like intersections.
		- End-systems are like buildings. 
- End-systems access the Internet through ISPs (Internet Service Providers).
- **ISP** — itself a network of packet switches and communication links. 
	- ISPs are also interconnected.
	- Low-tier ISPs are interconnected through national and international upper-tier ISP. 
		- Upper tier ISP — high-speed routers interconnected with high-speed fiber optic links.
	- Each ISP regardless of tier is managed independently. 
	- ISP protocol. 
	- Conforms to certain naming and address conventions.
	- "The Internet is all about connecting end systems to each other." 
- Each entity (end systems, packet switches, etc.) that forms the Internet run **protocols**.
	- Protocol — control the sending and receiving of information within the Internet. 
	- The two most important include:
		- **Transmission Control Protocol** (TCP) — 
		- **Internet Protocol** (IP) — specifies the format of the packets sent and received among routers and end systems.
		- **TCP/IP** - collectively the Internet's principal protocols. 
	- Important that everyone agrees on what each and every protocol does, so that systems and products can interoperate. 
		- **Internet standards** - developed by the IETF (Internet Engineering Task Force)
			- Standard documents of the IETF - **requests for comments (RFCs)**, or requests to resolve network and protocol design problems that faced the precursor of the Internet. More than 7000 RFCs. TCP, IP. HTTP for web and SMTP for email.

### 1.1.2 A Services Description 

Another definition and perspective of the Internet. 

**Internet** — an infrastructure that provides services to applications. 

***Distributed applications*** — involves multiple end-systems that exchange data with each other.

- Web applications, mobile applications, and Internet messaging. 
	- Mapping with real-time road-traffic information. 
	- Music streaming from the cloud.
	- Movie and television streaming. 
	- Online social networks. 
	- Video conferencing.
	- Multi-person games.
	- Location-based recommendation systems. 
- Applications run on end-systems.
- Applications *do not* run in the packet switches in the network core. 
	- Packet switches facilitates data exchange between end systems, but they are not concerned with the application that is the source or sink of data.

What do we mean by infrastructure that provides services to applications?

Let's say we want to create a distributed Internet application. How is an idea transformed into an actual Internet application? 
- Programs that run on end-systems.
- Programs running on different end-systems need to send data to each other. 
- "And here we get to a central issue—one that leads to the alternative way of describing the Internet as a platform for applications. *How does one program running on one end system instruct the Internet to deliver data to another program running on another end system?*"

Socket interface — a set of rules that the sending program must follow so that the Internet can deliver the data to the destination program.
- Provided by end-systems attached to the Internet.
- Specifies how a program running on one end system asks the Internet infrastructure to deliver data to a specific destination program running on another system. 

"When you develop an Internet application, you too must choose one of the Internet's services for your application."

Questions: What are packet switching and TCP/IP? What are routers? What kinds of communication links are present in the Internet? What is a distributed application? How can a thermostat or body scale be attached to the Internet? 

### 1.1.3 What is a Protocol? 

What is a protocol? What does it do? 

#### A Human Analogy
Unwillingness or inability to communicate.
	If people run different protocols (for example, if one person has manners but the other does not, or if one understands the concept of time and the other does not) the protocols do not interoperate and no useful work can be accomplished. The same is true in networking—it takes two (or more) communicating entities running the same protocol in order to accomplish a task.

#### Network Protocols

A **protocol** defines the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event. 

**Hardware-implemented protocols** in two physically connected computers control the flow of bits on the “wire” between the two network interface cards; congestion-control protocols in end systems control the rate at which packets are transmitted between sender and receiver; protocols in routers determine a packet’s path from source to destination. 

Different protocols are used to accomplish different communication tasks.

