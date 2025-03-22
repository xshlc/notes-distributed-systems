## What is a circuit-switched network?

A circuit-switched network is a type of telecommunications network in which a dedicated communication path, or circuit, is established between two parties for the duration of the communication session. This path remains reserved and exclusively used by the communicating parties until the session is terminated. Circuit switching is traditionally used in voice communication networks, such as the Public Switched Telephone Network (PSTN).

### Key Characteristics of Circuit-Switched Networks:
1. **Dedicated Path**: A dedicated communication path is established from the sender to the receiver.
2. **Resource Reservation**: Network resources (like bandwidth) are reserved for the entire duration of the communication.
3. **Fixed Bandwidth**: The bandwidth is fixed and guaranteed for the duration of the call.
4. **Connection-Oriented**: Requires a setup phase to establish the connection before data transfer begins.

### How It Works:
1. **Connection Setup**: A dedicated circuit is established between the communicating parties through a series of switches.
2. **Data Transfer**: Data is transmitted continuously over the established circuit.
3. **Connection Termination**: The circuit is terminated, and resources are released once the communication session ends.

### Advantages:
- **Predictable Performance**: Guaranteed bandwidth and consistent latency, making it suitable for real-time communication like voice calls.
- **Simple Data Transfer**: Once the circuit is established, data transfer is straightforward with minimal overhead.
- **Quality of Service (QoS)**: High quality of service due to dedicated resources.

### Disadvantages:
- **Inefficient Resource Utilization**: Resources are reserved even when no data is being transmitted, leading to potential inefficiency.
- **Scalability Issues**: Less scalable compared to packet-switched networks, as each active connection requires dedicated resources.
- **Higher Costs**: Generally more expensive due to the need for dedicated circuits and infrastructure.

### Examples:
- **Traditional Telephone Networks**: The PSTN is a classic example of a circuit-switched network.
- **ISDN (Integrated Services Digital Network)**: A digital version of circuit-switched telephony.
- **Leased Lines**: Dedicated communication lines used by businesses for private voice or data networks.

### Comparison with Packet-Switched Networks:
- **Resource Usage**: Circuit-switched networks reserve resources for the entire session, while packet-switched networks share resources dynamically.
- **Latency**: Circuit-switched networks offer consistent latency, whereas packet-switched networks may have variable latency.
- **Efficiency**: Packet-switched networks are generally more efficient in terms of resource utilization.

Circuit-switched networks are well-suited for applications requiring consistent and reliable communication, such as traditional voice calls. However, with the advent of digital communication and the internet, packet-switched networks have become more prevalent due to their flexibility and efficiency.