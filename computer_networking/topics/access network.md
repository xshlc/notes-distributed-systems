# Access Network

In the context of computer networks and the internet, an **access network** refers to the part of the network that connects end-user devices (such as computers, smartphones, IoT devices, etc.) to the wider internet or a core network. It is the "last mile" of the network infrastructure, providing the necessary connectivity for users to access services and resources.

### Key Characteristics of an Access Network:
1. **Connects End Users**: It links individual users or local networks (e.g., homes, businesses, or institutions) to a service provider's network.
2. **Last-Mile Connectivity**: It is often referred to as the "last mile" because it bridges the gap between the end user and the core network.
3. **Variety of Technologies**: Access networks can use different technologies depending on the medium and requirements, such as:
   - **Wired**: DSL (Digital Subscriber Line), cable (coaxial), fiber-optic (FTTH - Fiber to the Home), Ethernet.
   - **Wireless**: Wi-Fi, cellular networks (4G, 5G), satellite, fixed wireless.
4. **Managed by ISPs**: Access networks are typically operated by Internet Service Providers (ISPs) or telecommunications companies.

### Examples of Access Networks:
1. **DSL Networks**: Use telephone lines to provide internet access.
2. **Cable Networks**: Use coaxial cables, often provided by cable TV companies.
3. **Fiber-Optic Networks**: Use high-speed fiber-optic cables for faster internet access.
4. **Wireless Networks**: Include Wi-Fi hotspots, cellular networks (4G/5G), and satellite-based internet.
5. **Ethernet Networks**: Common in businesses or campuses, providing high-speed wired connections.

### Role in the Internet Ecosystem:
- The access network is crucial because it determines the quality of service (QoS) experienced by end users, such as speed, latency, and reliability.
- It acts as a gateway for users to access the broader internet, including cloud services, websites, and other online resources.

In summary, the access network is the critical link between end-user devices and the larger network infrastructure, enabling users to connect to the internet and other services.

---

## Each are encoded at different frequencies. This makes the single DSL link appear as there were three separate links. 

*Elaborate on this point.*

The statement refers to how **DSL (Digital Subscriber Line)** technology works, particularly in the context of **frequency division multiplexing (FDM)**. DSL uses different frequency ranges to separate and transmit multiple types of data simultaneously over a single physical telephone line. This allows the DSL link to appear as if there are multiple "virtual" links, each dedicated to a specific type of communication.

### How DSL Uses Different Frequencies:
1. **Frequency Division Multiplexing (FDM)**:
   - DSL divides the available frequency spectrum of the telephone line into separate channels or bands.
   - Each band is allocated to a specific [[type of data transmission]] (e.g., voice, upstream data, downstream data).
   - This separation ensures that different types of data do not interfere with each other.

2. **Three Common Frequency Bands in DSL**:
   - **Voice (Plain Old Telephone Service - POTS)**:
     - Occupies the lowest frequency range (0–4 kHz).
     - Used for traditional voice calls.
     - This band is separated from the data bands to ensure voice calls are clear and uninterrupted.
   - **Upstream Data (User to ISP)**:
     - Occupies a higher frequency range (e.g., 25–138 kHz for ADSL).
     - Used for sending data from the user to the internet (e.g., uploading files, sending emails).
   - **Downstream Data (ISP to User)**:
     - Occupies an even higher frequency range (e.g., 138 kHz–1.1 MHz for ADSL).
     - Used for receiving data from the internet (e.g., downloading files, streaming videos).

3. **Simultaneous Transmission**:
   - Because these frequency bands do not overlap, voice, upstream data, and downstream data can be transmitted simultaneously over the same physical line.
   - This makes the single DSL link appear as if there are three separate links: one for voice, one for upstream data, and one for downstream data.

### Why This Matters:
- **Efficient Use of Infrastructure**: By using different frequencies, DSL maximizes the utility of existing telephone lines without requiring additional physical infrastructure.
- **Simultaneous Voice and Data**: Users can make phone calls and use the internet at the same time without interference.
- **Scalability**: The separation of frequencies allows ISPs to allocate bandwidth dynamically based on user needs.

### Example: ADSL (Asymmetric DSL)
- In ADSL, the downstream bandwidth is typically larger than the upstream bandwidth, reflecting the common use case where users download more data than they upload (e.g., streaming videos, browsing websites).
- The frequency bands are carefully allocated to ensure optimal performance for both voice and data.

### Summary:
By encoding data at different frequencies, DSL effectively creates multiple "virtual links" over a single physical telephone line. This allows simultaneous transmission of voice, upstream data, and downstream data, making the DSL link appear as if it were three separate links. This efficient use of frequency division multiplexing is a key feature of DSL technology.