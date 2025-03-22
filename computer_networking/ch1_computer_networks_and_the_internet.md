
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

## 1.2 The Network Edge 

This section will... 
1. move from the network edge to the network core. 
2. examine switching and routing in computer networks.

**host** == **end system**

Types of hosts:
- clients
	- desktops, smartphones, etc.
- servers
	- data centers
		- Google has 50-100 data centers, including about 15 large centers, each with more than 100,000 servers. 

### 1.2.1 Access Networks

**[[access network]]** — the network that physically connects an end system to the first router (or **edge router**) on a path from the end system to any other distant end system.

#### Home Access: DSL, Cable, FTTH, Dial-Up, and Satellite 

Two most prevalent types of broadband residential access:
1. Digital subscriber line (DSL)
	1. Same as local telephone company (telco). For DSL, telco also becomes the customer's ISP.
	2. Customer’s DSL modem uses the existing telephone line  to exchange data with a digital subscriber line access multiplexer ([[DSLAM]]) located in the telco’s local central office ([[CO]]). The home’s DSL modem takes digital data and translates it to high- frequency tones for transmission over telephone wires to the CO; the analog signals from many such houses are translated back into digital format at the DSLAM.
	3. Residential telephone lines carry both data and traditional telephone signals simultaneously.
		1. Each are encoded at different frequencies.
		2. A high-speed downstream channel, in the 50 kHz to 1 MHz band
		3. A medium-speed upstream channel, in the 4 kHz to 50 kHz band
		4. An ordinary two-way telephone channel, in the 0 to 4 kHz band
		5. This makes the single DSL link appear as there were three separate links. 
		6. Frequency-division multiplexing 
	4. On the customer side, a splitter separates the data and telephone signals arriving to the home and forwards the data signals to the DSL modem. 
	5. On the telco side, in the CO, the DSLAM separates the data and phone signals, and sends the data into the Internet. Hundreds or even thousands of households connect to a single DSLAM.
	6. DSL standards define multiple transmission rates (downstream and upstream).
	7. When downstream and upstream rates are different, the access is said to be asymmetric.
	8. The maximum rate is limited by the distance between the home and the CO. 
2. Cable internet access
	1. Makes use of the cable television's company's existing cable television infrastructure. 
	2. Coaxial.
	3. Fiber optics.
	4. Hybrid fiber coax (HFC)
	5. Requires special modems. called cable modems.
	6. The *cable modem termination system (CMTS)* serves a similar function as DSL network's DSLAM ― turning the analog signal sent from the cable modems in many downstream homes back into digital format. 
3. Difference:
	1. Cable modems divide the HFC network into two channels, downstream and upstream.
	2. DSL - access is asymmetric, with the downstream channel typically allocated a higher transmission rate than the upstream channel.
4. Cable Internet access is a *shared broadcast medium*. 
	1. Every packet sent by the head end travels downstream on every link to every home.
	2. Every packet sent by a home travels on the upstream channel to the head.
	3. If several users are simultaneously downloading a video file on the downstream channel, the actual rate at which each user receives its video file will be significantly lower than the aggregate cable downstream rate.
	4. On the other hand, if there are only a few users and they are all web surfing, each user may receive web pages at the full cable downstream rate. 
5. Because the upstream channel is also shared, a distributed multiple access protocol is needed to coordinate transmissions and avoid collisions.
6. *Fiber to the home (FTTH)* ― provide an optical fiber path from the CO directly to the home. 
7. There are several competing technologies for optical distribution from the CO to the homes. The simplest optical distribution network is called direct fiber, with one fiber leaving the CO for each home. More commonly, each fiber leaving the central office is actually shared by many homes; it is not until the fiber gets relatively close to the homes that it is split into individual customer-specific fibers.
8. Two competing optical-distribution network architectures that perform this splitting:
	1. Active optical networks (AONs)
		1. A switched Ethernet.
	2. Passive optical networks (PONs)
		1. Used in Verizon FIOS service
		2. Each home has an optical network terminator (ONT), which is connected by dedicated optical fiber to a neighborhood splitter. 
		3. The splitter combines a number of homes (typically less than 100) onto a single, shared optical fiber, which connects to an optical line terminator (OLT) in the telco’s CO. 
		4. The OLT, providing conversion between optical and electrical signals, connects to the Internet via a telco router.
		5. In the home, users connect a home router (typically a wireless router) to the ONT and access the Internet via this home router. In the PON architecture, all packets sent from OLT to the splitter are replicated at the splitter (similar to a cable head end).
	3. FTTH can potentially provide Internet access rates in the gigabits per second range. 
9. Two other access network technologies:
	1. Satellite link
		1. StarBand
		2. HughesNet
	2. Dial-up access over traditional phone lines. 
		1. Excruciatingly slow.

#### Access in the Enterprise (and the Home): Ethernet and WiFi 
**local area network (LAN)** ― used to connect an end system to an edge router. Ethernet is the most prevalent.

The Ethernet switch, or network of such interconnected switches, is then in turn connected into the larger Internet. Users typically have greater speeds with Ethernet (100 Mbps to 10 Gbps access).

**Wireless LAN** ― wireless users transmit/receive packets to/from an access point that is connected into the enterprise’s network (most likely using wired Ethernet), which in turn is connected to the wired Internet.
- A wireless LAN user must typically be within a few tens of meters of the access point.
- More colloquially known as WiFi, is now just about everywhere.

Many homes combine broadband residential access
(that is, cable modems or DSL) with these inexpensive wireless LAN technologies to create powerful home networks.

#### Wide-Area Wireless Access: 3G and LTE

Smartphones - iPhone and Android devices 

These devices employ the same wireless infrastructure used for cellular telephony to send/receive packets through a base station, operated by the cellular network provider. 

Unlike WiFi, a user need only be within a few tens of kilometers (as opposed to a few tens of meters) of the base station.

Third-generation (3G) wireless and fourth-generation (4G) wireless -  provides packet-switched wide-area wireless Internet access.

LTE (Long-Term Evolution) - can achieve rates in excess of 10 Mbps. 

### 1.2.2 Physical Media

A brief overview of transmission media that are commonly used in the Internet (already discussed are fiber and coaxial for HFC, copper wire for DSL and Ethernet. radio spectrum for mobile access networks).

A bit get tossed and passed around through a series of transmitter-receiver pairs. For each transmitter-receiver pair, the bit is sent by propagating electromagnetic waves or optical pulses across a **physical medium**.
1. Physical medium can take many shapes and forms.

Two categories of physical medium:
1. Guided media
	1. Waves are guided along a solid medium.
	2. Fiber-optic cable
	3. A twisted pair of copper wire
	4. Coaxial cable
	5. The cost of physical link is relatively minor compared with other networking costs.
		1. The labor cost for installation of the physical link can be orders of magnitude higher than the cost of the material. 
		2. For this reason, many builders install twisted pair, optical fiber, and coaxial cable in every room in a building.
			1. Money is saved by not having to lay additional wires in the future.
2. Unguided media
	1. Waves propagate in the atmosphere and in outer space.
	2. Wireless LAN / WiFi
	3. Digital satellite channel
	
#### Twisted-Pair Copper Wire
Least expensive and most commonly used guided transmission medium. 
Used by telephone networks for hundreds of years. 
Twisted pair consists of:
1. Two insulated copper wires (around 1mm thick)
2. Arranged in a regular spiral pattern. 
3. Twisted to reduce the electrical interference from similar pairs close by.
4. Typically, a number of pairs are bundled together in a cable by wrapping the pairs in a protective shield. 
A wire pair constitutes a single communication link. 

Unshielded twisted pair (UTP) - commonly used for computer networks within a building for LANs
- Data rates that can be achieved depend on the thickness of the wire and the distance between transmitter and receiver. 

Modern twisted-pair technology
- For example, category 6a cable
- Can achieve data rates of 10 Gbps for distances up to hundreds of meters. 
- Fiber-optics did not completely replace twisted pair. 
- Instead, twisted pair has emerged as the dominant solution for high-speed LAN networking.

DSL (Digital subscriber line) technology has enabled residential users to access the Internet at tens of Mbps over twisted pair. 

#### Coaxial Cable
- Like twisted pair. consists of two copper conductors, but the two conductors are concentric rather than parallel. 
- Can achieve high data transmission rates.
- Common in cable television systems. 
- Coupled with the cable modem to provide residential users with Internet access.

In cable television and cable Internet access, the transmitter shifts the digital signal to a specific frequency band, and the resulting analog signal is sent from the transmitter to one or more receivers.

Coaxial cable can be used as a guided shared medium. Specifically, a number of end systems can be connected directly to the cable, with each of the end systems receiving whatever is sent by the other end systems.


#### Fiber Optics
An optical fiber is a thin, flexible medium that conducts pulses of light, with each pulse representing a bit. 
- A single optical fiber can support tremendous bit rates, upp to tens or even hundreds of gigabits per second. 
- They are immune to electromagnetic interference, have very low signal attenuation up to 100 kilometers, and are very hard to tap. 
- Preferred long-haul guided transmission media, particularly for overseas links

High-cost of optical devices (transmitters, receivers, switches) hindered their deployment for short-haul transport. 

The Optical Carrier (OC) standard link speeds range from 51.8 Mbps to 39.8 Gbps; these specifications are often referred to as OC-n, where the link speed equals n ∞ 51.8 Mbps. Standards in use today include OC-1, OC-3, OC-12, OC-24, OC-48, OC-96, OC-192, OC-768 provide coverage of various aspects of optical networking.

#### Terrestrial Radio Channels 

Radio channels carry signals in the electromagnetic spectrum. 

Pros:
- Require no physical wire to be installed.
- Can penetrate walls.
- Provide connectivity to mobile user.
- Can potentially carry a signal for long distances.

The characteristics of a radio channel depend significantly n the propagation environment and the distance over which a signal is to be carried. 

Cons:
- Environmental considerations determine path loss and shadow fading (which decrease the signal strength as the signal travels over a distance and around/through obstructing objects), multipath fading (due to signal reflection off of interfering objects), and interference (due to other transmissions and electromagnetic signals).

Three groups:
1. Those that operate over a very short distance.
	1. A couple meters.
	2. Personal devices.
		1. Wireless headphones.
		2. Keyboards.
		3. Medical devices.
2. Those that operate in local areas.
	1. 10 to a few 100 meters.
	2. Wireless LAN / WiFi
	3. Local-area radio channels.
3. Those that operate in a wide-area.
	1. 10s of kilometers. 
	2. Cellular access technologies.

#### Satellite Radio Channels
A communication satellite links two or more Earth-based microwave transmitter/receivers, known as ground stations. 

The satellite receives transmission on one frequency band, regenerates the signal using a repeater, and transmits the signal on another frequency. 

Two types of satellites used for communications:
1. Geostationary satellites
	1. Permanently remain above the same spot on Earth.
	2. Orbits at 36,000 kilometers above Earth’s surface.
	3. Huge distance from ground station through satellite back to ground station introduces a substantial signal propagation delay of 280 milliseconds.
2. Low-earth orbiting (LEO) satellites
	1. Does not remain permanently above one spot on Earth.
	2. Rotates around Earth (just as the Moon does) and may communicate with each other, as well as with ground stations.

---

## 1.3 The Network Core

The *network core* is the mesh of packet switches and links that interconnects the Internet's end systems.

### 1.3.1 Packet Switching 

In a network application, end systems exchange ***messages*** with each other. 

Messages:
1. Can contain anything the application wants. 
2. May perform a control function.
	1. For example, the "Hi" messages in our handshaking example (Figure 1.2).
3. Can contain data.
	1. Email message.
	2. JPEG image.
	3. MP3 audio file. 

To send a message from a source end system to destination end system, the source breaks long messages into small chunks of data known as **packets**. Between source and destination, each packet travels through communication links and **packet switches**.
- Two main types of packet switches:
	1. Routers
	2. Link-layer switches

Packets are transmitted over each communication link at a rate equal to the *full* transmission rate of the link. 

So, if a source end system or a packet switch is sending a packet of L bits over a link with transmission rate R bits/sec, then the time to transmit the packet is L / R seconds.

#### Store-and-Forward Transmission 
Most packets use **store-and-forward transmission** at the inputs to the links. 

***Store-and-forward transmission*** ― means that packet switch must receive the entire packet before it can begin to transmit the first bit of the packet onto the outbound link. 

Consider this: Suppose source has transmitting some of packet 1, and the front of packet 1 has already arrived at the router. Because the router employs store-and-forwarding, at this instant of time, the router cannot transmit the bits it has received; instead it must first *buffer* (or "store") the packet's bit. Only after the router has received *all* of the packet's bits can it begin to transmit (or "forward") the packet onto the outbound link. 

Routers need to receive, store, and process the entire packet before forwarding. 

The **[[end-to-end delay]]** formula:
$$d_{end-to-end} = N \frac{L}{R}$$
General case of sending one packet from source to destination over a path consisting of $N$ links each of rate $R$ (thus, there are $N - 1$ routers between source and destination). 

You may now want to try to determine what the delay would be for $P$ packets sent over a series of $N$ links. 

#### Queuing Delays and Packet Loss
- Each packet has multiple links attached to it.
- For each attached link, the packet switch has an **output buffer** (or output queue). 
	- Output buffer ― stores packets that the router is about to send into that link
		- Plays a key role in packet switching.
		- If an arriving packet needs to transmitted onto a link but finds the link busy with the transmission of another packet, the arriving packet must wait in the output buffer. 
	- In addition to the store-and-forward delays, packets suffer output buffer queuing delays. 
		- These delays are variable and depend on the level of congestion in the network.
		- The amount of buffer space is finite. 
			- An arriving packet may find that the buffer is completely full with other packets waiting for transmission. 
			- In this case, **packet loss** will occur.
	- ***Packet loss*** ― when either the arriving packet or one of the already-queued packets is dropped
- Scenario:
	- Hosts A and B send packets to Host E via a router.
	- Hosts A and B use 100 Mbps Ethernet links, but the router directs packets to a slower 15 Mbps link.
	- If the arrival rate of packets exceeds 15 Mbps, congestion occurs at the router.
	- Example: If Hosts A and B each send 5 packets back-to-back, most packets will wait in the queue.
- Real-World Analogy
    - Congestion in networks is compared to everyday situations like waiting in line at a bank or tollbooth.
**Summary:**
In a network, packets (chunks of data) can face delays and even get lost if the network is too busy. When packets arrive at a router faster than they can be sent out, they pile up in a waiting area called a buffer. If the buffer gets full, some packets are dropped.

For example, imagine two computers (Hosts A and B) sending data to another computer (Host E) through a router. The router can only send data at 15 Mbps, but the two computers are sending data at 100 Mbps. If both send a lot of data at the same time, the router gets overwhelmed, and packets have to wait in line. This is like waiting in line at a bank or tollbooth when there are too many people. If the line gets too long, some people (or packets) might have to leave.

#### Forwarding Tables and Routing Protocols 
A router takes a packet arriving on one of its attached communication links and forwards that packet onto another one of its attached communication links. 

But how does the router determine which link it should forward the packet onto? 

Packet forwarding is done in different ways in different types of computer networks. 

How it's done on the Internet:
- Every end system has an IP address.
- When a source end system wants to send a packet to a destination end system, the source includes the destination's IP address in the packet's header. 
	- As with postal addresses, this address has a hierarchical structure. 
- When a packet arrives at a router in the network, the router examines a portion of the packet's destination address and forwards the packet to an adjacent router. 
- Each router has a **forwarding table** that maps destination addresses (or portions of the destination addresses) to that router's outbound link. 
	- The router then directs the packet to its outbound link. 
- *Analogy*: The end-to-end routing process is analogous to a car driver who does not use maps but instead prefers to ask for directions. 
- A router uses a packet’s destination address to index a forwarding table and determine the appropriate outbound link. But this statement begs yet another question: How do forwarding tables get set? Are they configured by hand in each and every router, or does the Internet use a more automated procedure? This issue will be studied in depth in Chapter 5.
- The Internet has **routing protocols** that are used to automatically set the forwarding tables. 
	- For example, a routing protocol may determine the shortest path from each router to each destination and use the shortest path results to configure the forwarding tables in the routers. 
- How would you actually like to see the end-to-end route that packets take in the Internet? 
	- Trace-route program: www.traceroute.org 

### 1.3.2 Circuit Switching 
Two fundamental approaches to moving data through a network of links and switches:
1. **[[Circuit switching]]**
2. **[[Packet switching]]** (already covered in previous section)

*Circuit-switched networks*
- The resources needed along a path (buffers, link transmission rate) to provide for communication between the end systems are reserved for the duration of the communication session between the end systems. 
- Packet-switch networks -> these resources are not reserved.
	- A session's messages use the resources on demand.
		- as a consequence, may have to wait (queue) for access to a communication link. 
- Traditional telephone networks are examples of circuit-switched networks. 
	- Before the sender can send information, the network must establish a connection between the sender and the receiver. 
	- a **circuit** in telephony ― a bona fide connection for which the switches on the path between the sender and the receiver maintain connection state for that connection. 
	- When the network establishes the circuit, it also reserves a constant transmission rate in the network's links (representing a fraction of each link's transmission capacity) for the duration of the connection. 
	- Since a given transmission rate has been *reserved* for this sender-receiver connection, the sender can transfer the data to the receiver at the *guaranteed constant rate*.
	- 

"The Internet makes its best effort to deliver packets in a timely manner, but it does not make any guarantees."

#### Multiplexing in Circuit-Switched Networks 


### 1.3.3 A Network of Networks 

The network of networks that forms the Internet has evolved into a very complex structure. Much of this evolution is driven by economics and national policy, rather than by performance considerations.

Recall that the overarching goal is to interconnect the access ISPs so that all end systems can send packets to each other. One naive approach would be to have each access ISP directly connect with every other access ISP. Such a mesh design is, of course, much too *costly* for the access ISPs, as it would require each access ISP to have a separate communication link to each of the hundreds of thousands of other access ISPs all over the world.

Internet [[network structures]]: 
1. Network Structure 1 ―  interconnects all of the access ISPs with a single global transit ISP
2. Network Structure 2 ―  consists of the hundreds of thousands of access ISPs and multiple global transit ISPs
	- a two-tier hierarchy with global transitp providers residing at the top tier and access ISPs at the bottom tier
3. Network Structure 3 ― multi-tier hierarchy 
4. Network Structure 4 ― consisting of access ISPs, regional ISPs, tier-1 ISPs, PoPs, multi-homing, peering, and IXPs
	- points of presence **PoP** - a group of one or more routers at the same location in the provider's network where customer ISPs can connect into the provider ISP
	- **multi-home** - connect two or more provider ISPs
	- Internet exchange points **IXPs** - a meeting point where multiple ISPs can peer together
5. Network Structure 5 — builds on top of Network Structure 4 by adding **content-provider networks** 

[[Evolution to network structures]]


