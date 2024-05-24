from crewai import Task

class TechTasks:
    def __init__(self, tools):
        self.tools = tools

    def gather_information(self, agent):
        return Task(
            description = "Conduct an in-depth analysis of all the specifications of {item}",
            expected_output = (
                "Give information about the following features for a laptop: the processor, including the model, clock speed, "
                "number of cores, cache size, and architecture; the memory, including type, size, speed, and expandability; "
                "the storage, including type, capacity, speed (read/write), and expandability; the graphics, specifying whether "
                "it is integrated or dedicated, the model, VRAM size, and graphics clock speed; the operating system, including "
                "the pre-installed OS and supported OS versions; the screen features, including size, resolution, panel type, "
                "refresh rate, brightness (nits), color accuracy, touchscreen capability, and aspect ratio; the build and design, "
                "including dimensions (height, width, depth), weight, material, color options, build quality, keyboard, and touchpad; "
                "connectivity options, including USB ports, HDMI, DisplayPort, Ethernet, audio jack, and SD card reader; wireless capabilities, "
                "including Wi-Fi standards and Bluetooth version; additional connectivity features, including NFC and SIM card slot; battery and "
                "power specifications, including battery capacity (Wh), battery life (in hours), charging speed, and type of charger; audio and "
                "camera features, including the number and quality of speakers and microphones, as well as camera resolution and features; "
                "additional features, including security options like fingerprint reader, facial recognition, and TPM, included software like "
                "antivirus, office suite, and custom utilities; the cooling system, including type and efficiency; expandability options, "
                "including ease of access for upgrades and supported upgrades; warranty and support details, including duration and type; "
                "included accessories and compatibility with additional accessories; environmental and energy efficiency ratings, including "
                "Energy Star rating and RoHS compliance; and user reviews and ratings, including the average rating and common pros and cons."),
            agent = agent,
            async_execution = True,
            tools = self.tools
        )
    
    def format_text(self, agent):
        return Task(
            description = "",
            expected_output = """Give in the following format please.
### Technical Features

#### Processor (CPU)
- **Model**: [Model]
- **Clock Speed**: [Clock Speed]
- **Number of Cores**: [Number of Cores]
- **Cache Size**: [Cache Size]
- **Architecture**: [Architecture]

#### Memory (RAM)
- **Type**: [Type]
- **Size**: [Size]
- **Speed**: [Speed]
- **Expandability**: [Expandability]

#### Storage
- **Type**: [Type]
- **Capacity**: [Capacity]
- **Speed (Read/Write)**: [Speed (Read/Write)]
- **Expandability**: [Expandability]

#### Graphics (GPU)
- **Integrated or Dedicated**: [Integrated or Dedicated]
- **Model**: [Model]
- **VRAM Size**: [VRAM Size]
- **Graphics Clock Speed**: [Graphics Clock Speed]

#### Operating System
- **Pre-installed OS**: [Pre-installed OS]
- **Supported OS versions**: [Supported OS versions]

#### Screen Features
- **Size**: [Size]
- **Resolution**: [Resolution]
- **Panel Type**: [Panel Type]
- **Refresh Rate**: [Refresh Rate]
- **Brightness (nits)**: [Brightness (nits)]
- **Color Accuracy**: [Color Accuracy]
- **Touchscreen**: [Touchscreen]
- **Aspect Ratio**: [Aspect Ratio]

#### Build and Design
- **Dimensions (Height, Width, Depth)**: [Dimensions (Height, Width, Depth)]
- **Weight**: [Weight]
- **Material**: [Material]
- **Color Options**: [Color Options]
- **Build Quality**: [Build Quality]
- **Keyboard**: [Keyboard]
- **Touchpad**: [Touchpad]

#### Connectivity

##### Ports
- **USB**: [USB]
- **HDMI**: [HDMI]
- **DisplayPort**: [DisplayPort]
- **Ethernet**: [Ethernet]
- **Audio Jack**: [Audio Jack]
- **SD Card Reader**: [SD Card Reader]

##### Wireless
- **Wi-Fi Standards**: [Wi-Fi Standards]
- **Bluetooth Version**: [Bluetooth Version]

##### Additional Connectivity
- **NFC**: [NFC]
- **SIM Card Slot**: [SIM Card Slot]

#### Battery and Power
- **Battery Capacity (Wh)**: [Battery Capacity (Wh)]
- **Battery Life (in hours)**: [Battery Life (in hours)]
- **Charging Speed**: [Charging Speed]
- **Type of Charger**: [Type of Charger]

#### Audio and Camera

##### Speakers
- **Number**: [Number]
- **Quality**: [Quality]

##### Microphone
- **Number**: [Number]
- **Quality**: [Quality]

##### Camera
- **Resolution**: [Resolution]
- **Features**: [Features]

#### Additional Features

##### Security
- **Fingerprint Reader**: [Fingerprint Reader]
- **Facial Recognition**: [Facial Recognition]
- **TPM**: [TPM]

##### Included Software
- **Antivirus**: [Antivirus]
- **Office Suite**: [Office Suite]
- **Custom Utilities**: [Custom Utilities]

##### Cooling System
- **Type**: [Type]
- **Efficiency**: [Efficiency]

##### Expandability
- **Ease of Access for Upgrades**: [Ease of Access for Upgrades]
- **Supported Upgrades**: [Supported Upgrades]

#### Warranty and Support
- **Duration**: [Duration]
- **Type**: [Type]

#### Accessories
- **Included**: [Included]
- **Compatibility with additional accessories**: [Compatibility with additional accessories]

#### Environmental and Energy Efficiency
- **Energy Star Rating**: [Energy Star Rating]
- **RoHS Compliance**: [RoHS Compliance]

#### User Reviews and Ratings
- **Average Rating**: [Average Rating]
- **Common Pros and Cons**: [Common Pros and Cons]
If you cant find information about that feature, you can say, not found""",
            agent = agent,
            async_execution = False,
            tools = self.tools
        )