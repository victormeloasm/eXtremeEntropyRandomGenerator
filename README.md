# eXtremeEntropyRandomGenerator

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

![Build and Resources](Image1.jpg)

![Build and Resources](Image2.jpg)


eXtremeEntropyRandomGenerator is a cutting-edge project that pushes the boundaries of randomness and entropy in data generation using Python. This project aims to create secure, unpredictable random numbers by combining audio data from radio static noise and visual data from CRT static noise, enhancing entropy, and providing novel applications in various fields.

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Entropy and Random Numbers](#entropy-and-random-numbers)
- [Audio and Visual Fusion](#audio-and-visual-fusion)
- [Saving Audio](#saving-audio)
- [Cleanup](#cleanup)
- [License](#license)

## Background

In the world of data and technology, the pursuit of true randomness is a fascinating endeavor. eXtremeEntropyRandomGenerator was conceived as an exploration into the generation of secure random numbers with a focus on maximizing entropy. This project leverages Python libraries, including PyAudio and OpenCV, to capture audio data from radio static noise and visual data from CRT static noise, merging them with random bytes and timestamps, and generating unpredictable 512-bit hashes.

## Installation

To run this project, you need to have Python installed on your system. Follow these steps to set up the environment:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/victormeloasm/eXtremeEntropyRandomGenerator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd eXtremeEntropyRandomGenerator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

![How to use](Screenshot.png)

![Using](Generator.png)


[Watch the Video](https://www.youtube.com/watch?v=17MMJY9gkv4)


### Generating Random Numbers

1. Run the `eXtremeEntropyRandomGenerator.py` script to start the random number generation process or unzip the /dist/eXtremeEntropyRandomGenerator.exe with winRAR or 7zip.

2. You will be prompted to enter the range for random numbers. This input defines the upper bound for the random integers you want to generate It's from 0 to a 64 bytes integer.

3. The program will capture 1-second segments of audio from radio static noise and random frames from CRT static noise. It will also generate random bytes and timestamps to increase entropy.

4. The generated data will be combined and hashed using the SHA-512 algorithm, resulting in a 512-bit hash. This hash is then converted to an integer.

5. The generated integers within the specified range will be printed in the terminal.

### Entropy and Random Numbers

The project maximizes entropy by combining multiple sources of randomness:

- **Audio Data from Radio Static Noise:** Captured from the radio waves, this source provides audio-based entropy.
- **Visual Data from CRT Static Noise:** Captured from the CRT screen, this source offers visual-based entropy.
- **Random Bytes:** Generated using Python's `os.urandom`.
- **Timestamps:** Current Unix timestamps provide a temporal source of entropy.

The combination of these diverse sources ensures that the generated random numbers are highly unpredictable and secure.

### Audio and Visual Fusion

One of the unique aspects of this project is the fusion of audio and visual data from radio static noise and CRT static noise, respectively. By merging audio segments and random frames, we create a new form of multi-sensory data, enhancing the randomness of the final output. This concept has applications in cryptography, security, and data encryption.

### Saving Audio

To preserve the original audio segments for further analysis, the program saves them as WAV files in the current directory. The filenames correspond to each iteration of the experiment (e.g., `audio_0.wav`, `audio_1.wav`).

### Cleanup

Upon completion, the program cleans up the generated data from memory, ensuring that no sensitive information remains in the system's memory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

 This program was conceived and crafted by Víctor Duarte Melo on 14/09/2023 - Brazil. If you intend to use or modify it, please provide proper credits. 
 Building the structure and coding this project wasn't an easy task; it involved countless hours of testing and an entire night of planning. Please use it responsibly.
 Contact: victormeloasm@gmail.com

eXtremeEntropyRandomGenerator represents an exciting exploration into the world of randomness, entropy, and data fusion. It underscores the significance of entropy in data generation, highlighting its relevance in securing sensitive information. The fusion of audio and visual data from radio static noise and CRT static noise introduces new possibilities for data fusion and multi-sensory applications. This project serves as a captivating experiment in randomness, reminding us that randomness is not just a mathematical concept; it's a valuable resource with real-world applications in data security and beyond.

Enjoy experimenting with eXtremeEntropyRandomGenerator and exploring the boundless possibilities of randomness!


Everything was made by Víctor Duarte Melo, contact: victormeloasm@gmail.com

Certainly, here's an explanation of how the addition of entropy using Wi-Fi noise enhances randomness in a computational context:

**Enhancing Entropy with Wi-Fi Noise: Boosting Randomness in Computing**

Entropy, in the context of computing and cryptography, is a measure of randomness or uncertainty. In cryptographic applications, high entropy is vital for ensuring the security and unpredictability of keys, passwords, and random values generated by software. To increase entropy, developers often seek external sources of randomness to add to their computational processes, and one unconventional but intriguing source is the noise from Wi-Fi networks.

**What Is Wi-Fi Noise?**

Wi-Fi noise refers to the random electromagnetic signals that are present in the radio frequency spectrum utilized by wireless networks. These signals are generated by a multitude of factors, including interference from other electronic devices, environmental conditions, and the inherent unpredictability of wireless communications. These factors create a unique and continuously changing electromagnetic environment.

**Adding Wi-Fi Noise to Enhance Entropy**

To enhance the entropy of random number generation or cryptographic operations, developers capture Wi-Fi noise and incorporate it into their computations. The process typically involves measuring the noise level or signal strength of nearby Wi-Fi networks. The resulting value, often expressed as a numeric or bit sequence, is then used to augment the randomness of a computational task.

**Advantages of Adding Wi-Fi Noise:**

1. **Increased Entropy**: Wi-Fi noise is inherently unpredictable and dynamic, making it an excellent source of entropy. When combined with other sources of randomness, such as sensor data or user input, it significantly boosts the unpredictability of generated values.

2. **Security**: Applications requiring high levels of security, such as cryptographic key generation or password hashing, can benefit from the additional randomness provided by Wi-Fi noise. This makes it more challenging for adversaries to predict or guess generated values.

3. **Diverse Sources**: By integrating Wi-Fi noise, developers can tap into a diverse source of entropy, reducing the reliance on a single, potentially limited source of randomness.

**Considerations and Challenges:**

1. **Availability**: Capturing Wi-Fi noise depends on the presence of Wi-Fi networks in the vicinity. In areas with no Wi-Fi signals, this source of entropy may not be available.

2. **Variability**: Wi-Fi noise can vary over time due to changes in network usage and interference. Developers must account for this variability in their applications.

3. **Hardware Requirements**: To capture Wi-Fi noise, specific hardware and software libraries may be required. Additionally, access to Wi-Fi interfaces and permissions may be necessary.

In summary, incorporating Wi-Fi noise into computational processes is a creative way to augment entropy, making random number generation and cryptographic operations more robust and secure. While it may not be the sole source of randomness, it adds an extra layer of unpredictability, strengthening the overall security and reliability of computational systems. Developers should carefully consider the availability and variability of Wi-Fi noise in their specific use cases and balance it with other sources of entropy to achieve the desired level of randomness and security.
