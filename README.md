
# Image Captioning Project

This project is a Flask web application that allows users to upload images and generate captions for them using a custom AI model. The model utilizes EfficientNet for the Convolutional Neural Network (CNN) component, a custom Long Short-Term Memory (LSTM) network, and a multihead attention layer. The model has an accuracy of 42%.

## ScreenShots

#### HomePage
![img_cap1](https://github.com/user-attachments/assets/b7411d67-2267-454b-90ec-5fc4a4e38eb8)

#### Upload Image
![img_cap2](https://github.com/user-attachments/assets/df9f81ec-5216-4c07-afbd-fa6da4a027fa)

#### Image Uploaded
![img_cap3](https://github.com/user-attachments/assets/9da11943-a789-4ac3-ad60-c7751419718f)

#### Image captioned
![img_cap4](https://github.com/user-attachments/assets/5a6f959d-6785-4b67-9900-3e8a2e763567)

## Directory Structure
```markdown
Image Captioning Project
│
├── app.py
├── prediction.py
├── templates
│   └── index.html
├── static
│   ├── css
│   ├── images
│   └── media
├── Models
│   ├── model.h5
│   └── tokenizer.json
├── test images
└── model_training.pynb
```

- **app.py**: Main Flask application file.
- **prediction.py**: Contains the logic for image captioning using the AI model.
- **templates/index.html**: HTML template for the main page.
- **static/css**: Directory for CSS files.
- **static/images**: Directory for image files.
- **static/media**: Directory for media files.
- **Models**: Directory containing the pre-trained model and tokenizer.
- **test images**: Directory containing test images.
- **model_training.pynb**: Jupyter notebook containing the code for training the AI model.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Jupyter Notebook (for running `model_training.pynb`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshit433/Image-Captioning-Cantilever-.git
   cd Image Captioning Project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Create `requirements.txt`

If `requirements.txt` is not already present, you can generate it with the following command after installing the necessary packages:

```bash
pip freeze > requirements.txt
```

### Running the Application

1. **Start the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

### Training the Model

To train the model, open the `model_training.pynb` file in Jupyter Notebook and run the cells. This notebook contains the code for training the AI model using EfficientNet for the CNN component, a custom LSTM network, and a multihead attention layer.

### Usage

1. **Upload an Image:** Click on the "Choose File" button to select an image from your computer.
2. **Generate Caption:** After selecting the image, click on the "Upload" button to generate a caption for the image.
3. **View Result:** The generated caption and the uploaded image will be displayed on the same page.

## Project Details

### app.py

This is the main Flask application file which handles the web server, routes, and the logic for handling image uploads and generating captions.

### prediction.py

This file contains the core logic for generating captions using a custom AI model. The model utilizes EfficientNet for the CNN component, a custom LSTM network, and a multihead attention layer. The model and tokenizer are loaded from the `Models` directory.

### model_training.pynb

This Jupyter notebook contains the code for training the AI model. It includes data preprocessing, model architecture, training loop, and evaluation metrics.

### templates/index.html

This HTML file serves as the front-end for the application where users can upload images and view the generated captions.

### static

- **css**: This directory is intended for any CSS files needed for styling the web pages.
- **images**: This directory can be used to store images used in the project.
- **media**: This directory is used to store the user uploaded images.

### Models

This directory contains the pre-trained model (`model.h5`) and the tokenizer (`tokenizer.json`) used for generating captions.

### test images

This directory can be used to store images for testing the application.

## Model Details

- **CNN Component**: Utilizes EfficientNet for feature extraction from images.
- **LSTM Network**: A custom LSTM network is used for sequence generation.
- **Multihead Attention Layer**: Enhances the model's ability to focus on different parts of the image when generating captions.
- **Accuracy**: The model has an accuracy of 42%.

## Contributing

Feel free to fork this repository and make your changes. Pull requests are welcome.
