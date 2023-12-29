# E3 Colorizer: Enhancing Emotions, Eras, and Enhanced Colorization

![E3 Colorizer Logo](https://github.com/abinashlingank/E3Colorizer/blob/main/images/report.png)

## Overview

The "E3 Colorizer" project is an innovative image colorization tool that leverages the power of deep learning, emotion recognition, and historical style modeling to transform grayscale images into vibrant, emotionally resonant masterpieces. The project is developed in Python and integrates cutting-edge AI models to provide a comprehensive solution for colorizing images with a focus on enhancing emotions, representing historical eras accurately, and ensuring accessibility for all users.

## Project Objectives

### 1. Emotion Recognition Module:

- **Objective:** Develop and integrate an emotion recognition module.
- **Rationale:** Enhance the viewer's emotional connection by infusing color based on the underlying emotions conveyed in grayscale images.

### 2. Historical Colour Palettes:

- **Objective:** Integrate a repository of historical color palettes and styles.
- **Rationale:** Facilitate the visualization of history in vivid detail by allowing users to select specific time periods or historical styles for colorization.

### 3. Accessibility-Driven Colour Schemes:

- **Objective:** Create accessibility-driven color schemes.
- **Rationale:** Improve engagement for visually impaired individuals through carefully designed color schemes that maximize contrast, readability, and clarity.

### 4. User-Friendly Interface:

- **Objective:** Design and implement a user-friendly interface.
- **Rationale:** Prioritize usability and user experience to ensure easy navigation, customization of preferences, and seamless interaction with the "E3 Colorizer."

## Literature Survey

The "E3 Colorizer" project draws inspiration and methodologies from a rich body of research across diverse fields:

- **Image Colorization:** Traces the historical evolution of image colorization, from manual methods to automated techniques.
- **Emotion Recognition:** Explores the impact of color on emotional perception, demonstrating the potential for colorization to evoke specific emotions.
- **Historical Image Analysis:** Examines the application of deep learning in reconstructing historical colors and styles.
- **Accessibility:** Investigates various techniques, including color enhancement and contrast adjustments, to make images more accessible and comprehensible.
- **Deep Learning:** Highlights the role of Convolutional Neural Networks (CNNs) in revolutionizing image processing tasks, including colorization.

## Methodology

The "E3 Colorizer" system employs a fusion of deep learning techniques, emotion recognition algorithms, historical style modeling, and accessibility enhancement approaches:

### Deep Learning Integration:

- **Data Preparation:** Collect and preprocess an extensive dataset of grayscale images and their corresponding color versions.
- **Model Architecture:** Utilize a modified U-Net architecture tailored to the colorization task.
- **Loss Function:** Design a customized loss function incorporating perceptual, adversarial, and emotion loss components.

### Emotion Recognition:

- **Feature Extraction:** Extract salient features from input images, including facial expressions, contextual elements, and object composition.
- **Emotion-Colour Mapping:** Reference a database of emotion-colour mappings to infuse emotionally resonant colorizations.

### Historical Style Modelling:

- **Historical Colour Palettes:** Integrate a curated database of historical color palettes derived from research on art, fashion, and design.
- **Stylized Colorization:** Adjust colorization strategy to replicate chosen historical eras' aesthetics.

### Accessibility Enhancement:

- **Contrast Enhancement:** Employ accessibility-driven color schemes to enhance contrast and readability.
- **User Customization:** Provide customization options for users to tailor colorization settings to their specific needs.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e3-colorizer.git
   cd e3-colorizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Application
   ```bash
   python main.py

## Required Model Files

To utilize the "E3 Colorizer" project, you need to download the following model files and place them in the specified directories:

1. **`colorization_deploy_v2.prototxt`**

   - *Description:* This file contains the architecture or structure of the neural network used for image colorization.

2. **`coloriztion_release_v2.caffemodel`**

   - *Description:* This file contains the pre-trained weights of the colorization neural network.

3. **`pts_in_hull.npy`**

   - *Description:* This file contains the cluster centers used in the colorization process.

## Contact

For questions or feedback, feel free to reach out at [abinashlingank@gmail.com].
