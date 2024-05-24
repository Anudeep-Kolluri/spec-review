# spec-review
A website that helps in comparing 2 items in depth

To run,
- clone the repo
- install dependencies
- run `streamlit run app.py` in terminal
- the app should be running locally on browser

Spec review takes 2 apis. Openai api and seper api (for google search). When given 2 laptops to compare, it will pass through 2 agents, one is researcher and other is writer and then gives the output. This is very helpful because the output is always in the expected format. You can visit this [website](https://spec-review.streamlit.app/) to run online

![image](https://github.com/Anudeep-Kolluri/spec-review/assets/50168940/c65affc3-166b-4091-9732-01c237f4151f)

## Output
![Project output2](https://github.com/Anudeep-Kolluri/spec-review/assets/50168940/5e3ba964-512c-4e06-8816-666547c3132b)
Full output <br>
Laptop 1
```
### Technical Features

#### Processor (CPU)
- **Model**: Intel Core i5-13420H
- **Clock Speed**: 1.5 GHz (up to 4.7 GHz with Turbo Boost)
- **Number of Cores**: 10 cores (6 performance cores + 4 efficiency cores)
- **Cache Size**: 18 MB L3 cache
- **Architecture**: Alder Lake

#### Memory (RAM)
- **Type**: DDR4
- **Size**: 8 GB (2 x 4 GB)
- **Speed**: 3200 MHz
- **Expandability**: Yes, up to 32 GB

#### Storage
- **Type**: PCIe NVMe SSD
- **Capacity**: 512 GB
- **Speed (Read/Write)**: Not specified
- **Expandability**: Yes, additional M.2 slot available

#### Graphics (GPU)
- **Integrated or Dedicated**: Dedicated
- **Model**: NVIDIA GeForce RTX 3050
- **VRAM Size**: 6 GB GDDR6
- **Graphics Clock Speed**: Not specified

#### Operating System
- **Pre-installed OS**: Windows 11 Home
- **Supported OS versions**: Windows 11 Home

#### Screen Features
- **Size**: 15.6 inches
- **Resolution**: Full HD (1920 x 1080)
- **Panel Type**: IPS
- **Refresh Rate**: 144 Hz
- **Brightness (nits)**: Not specified
- **Color Accuracy**: Not specified
- **Touchscreen**: No
- **Aspect Ratio**: 16:9

#### Build and Design
- **Dimensions (Height, Width, Depth)**: 0.93" x 14.09" x 10.04"
- **Weight**: Not specified
- **Material**: Plastic chassis
- **Color Options**: Performance Blue
- **Build Quality**: Sturdy and durable
- **Keyboard**: Backlit keyboard
- **Touchpad**: Yes

#### Connectivity

##### Ports
- **USB**: Multiple USB Type-A and Type-C ports
- **HDMI**: Yes
- **DisplayPort**: Not specified
- **Ethernet**: Not specified
- **Audio Jack**: Yes
- **SD Card Reader**: Yes

##### Wireless
- **Wi-Fi Standards**: Wi-Fi 6
- **Bluetooth Version**: Bluetooth 5.2

##### Additional Connectivity
- **NFC**: Not specified
- **SIM Card Slot**: Not specified

#### Battery and Power
- **Battery Capacity (Wh)**: Not specified
- **Battery Life (in hours)**: Average, varies with usage
- **Charging Speed**: Not specified
- **Type of Charger**: Not specified

#### Audio and Camera

##### Speakers
- **Number**: Not specified
- **Quality**: Not specified

##### Microphone
- **Number**: Not specified
- **Quality**: Not specified

##### Camera
- **Resolution**: Not specified
- **Features**: Not specified

#### Additional Features

##### Security
- **Fingerprint Reader**: Not specified
- **Facial Recognition**: Not specified
- **TPM**: Not specified

##### Included Software
- **Antivirus**: Not specified
- **Office Suite**: Not specified
- **Custom Utilities**: Not specified

##### Cooling System
- **Type**: Not specified
- **Efficiency**: Not specified

##### Expandability
- **Ease of Access for Upgrades**: Not specified
- **Supported Upgrades**: RAM and storage

#### Warranty and Support
- **Duration**: Not specified
- **Type**: Not specified

#### Accessories
- **Included**: Not specified
- **Compatibility with additional accessories**: Not specified

#### Environmental and Energy Efficiency
- **Energy Star Rating**: Yes
- **RoHS Compliance**: Not specified

#### User Reviews and Ratings
- **Average Rating**: 4.6 out of 5 stars (from 1009 reviews)
- **Common Pros and Cons**: 
  - **Pros**: Sleek design, sturdy build, powerful hardware, high refresh rate display, customizable backlit keyboard
  - **Cons**: Slightly shorter battery life, heavier side, produces substantial heat under full load
```

Laptop 2
```
### Technical Features

#### Processor (CPU)
- **Model**: AMD Ryzen 5 7535HS
- **Clock Speed**: 3.3 GHz (base) to 4.55 GHz (boost)
- **Number of Cores**: 6 cores
- **Cache Size**: 16 MB L3 cache
- **Architecture**: Zen 3+ microarchitecture

#### Memory (RAM)
- **Type**: DDR5
- **Size**: 8 GB
- **Speed**: 4800 MHz
- **Expandability**: Yes, additional RAM can be added

#### Storage
- **Type**: PCIe NVMe TLC M.2 SSD
- **Capacity**: 512 GB
- **Speed (Read/Write)**: Not found
- **Expandability**: Yes, can be replaced or supplemented with additional storage

#### Graphics (GPU)
- **Integrated or Dedicated**: Dedicated
- **Model**: NVIDIA GeForce RTX 2050
- **VRAM Size**: 4 GB
- **Graphics Clock Speed**: Not found

#### Operating System
- **Pre-installed OS**: Windows 11 Home
- **Supported OS versions**: Windows 11 Home and later

#### Screen Features
- **Size**: 15.6 inches
- **Resolution**: 1920 x 1080 (Full HD)
- **Panel Type**: IPS
- **Refresh Rate**: 144Hz
- **Brightness (nits)**: 250 nits
- **Color Accuracy**: 45% NTSC
- **Touchscreen**: No
- **Aspect Ratio**: 16:9

#### Build and Design
- **Dimensions (Height, Width, Depth)**: 35.79 x 25.5 x 2.35 cm
- **Weight**: 2.29 kg
- **Material**: Not found
- **Color Options**: Mica Silver
- **Build Quality**: Good, but screen feels slightly flimsy
- **Keyboard**: Backlit keyboard with integrated numeric pad
- **Touchpad**: Standard touchpad

#### Connectivity

##### Ports
- **USB**: 1 USB Type-C 5Gbps, 2 USB Type-A 5Gbps
- **HDMI**: HDMI 2.1
- **DisplayPort**: Through USB-C
- **Ethernet**: RJ-45
- **Audio Jack**: Headphone/microphone combo
- **SD Card Reader**: 1 multi-format SD media card reader

##### Wireless
- **Wi-Fi Standards**: Wi-Fi 6 (MediaTek Wi-Fi 6 MT7921)
- **Bluetooth Version**: Bluetooth 5.3

##### Additional Connectivity
- **NFC**: No
- **SIM Card Slot**: No

#### Battery and Power
- **Battery Capacity (Wh)**: 52.5 Wh
- **Battery Life (in hours)**: Up to 6 hours
- **Charging Speed**: Approximately 50% in 30 minutes (fast charge)
- **Type of Charger**: 150 W Smart AC power adapter

#### Audio and Camera

##### Speakers
- **Number**: Dual speakers
- **Quality**: Audio by B&O; HP Audio Boost

##### Microphone
- **Number**: Dual array digital microphones
- **Quality**: Integrated with temporal noise reduction

##### Camera
- **Resolution**: HP Wide Vision 720p HD camera
- **Features**: Temporal noise reduction

#### Additional Features

##### Security
- **Fingerprint Reader**: Not found
- **Facial Recognition**: Not found
- **TPM**: Trusted Platform Module (Firmware TPM) support

##### Included Software
- **Antivirus**: McAfee Online Protection 30-day trial
- **Office Suite**: Not found
- **Custom Utilities**: Not found

##### Cooling System
- **Type**: Dual fans on one side
- **Efficiency**: Noted to have heating issues under high load

##### Expandability
- **Ease of Access for Upgrades**: RAM and SSD can be upgraded
- **Supported Upgrades**: Additional RAM and larger SSD

#### Warranty and Support
- **Duration**: 1 year
- **Type**: Limited warranty includes 1 year of parts and labor

#### Accessories
- **Included**: 64GB USB Flash Drive (not always included as noted by some users)
- **Compatibility with additional accessories**: Standard laptop accessories (mouse, external drives, etc.)

#### Environmental and Energy Efficiency
- **Energy Star Rating**: Not found
- **RoHS Compliance**: Not found

#### User Reviews and Ratings
- **Average Rating**: 4.2 to 4.6 out of 5 stars across different platforms
- **Common Pros and Cons**: Good performance for the price, decent display, expandable RAM; Quiet speakers, heating issues, poor battery life, some build quality concerns, missing USB flash drive in some cases

This comprehensive report provides a detailed understanding of the HP Victus 15.6" Gaming Laptop's specifications, functionalities, and potential applications.
```
