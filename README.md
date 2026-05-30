# 🦜 Parrot Species Classifier

A deep learning-powered image classification application that identifies four different species of parrots from uploaded images. The model is built using Transfer Learning with MobileNetV2 and achieves an impressive **96% classification accuracy**.

## 🚀 Features

* Classifies **4 Parrot Species**

  * African Grey Parrot
  * White Parrot
  * Amazon Green Parrot
  * Macaw
* Transfer Learning using **MobileNetV2**
* Lightweight and efficient architecture
* User-friendly frontend built with **Streamlit**
* Real-time image prediction
* High classification accuracy of **96%**

---

## 🏗️ Model Architecture

The model uses a pre-trained **MobileNetV2** backbone for feature extraction, followed by custom classification layers:

```text
MobileNetV2 (Pre-trained)
        ↓
Global Average Pooling
        ↓
Dropout Layer
        ↓
Dense Layer
        ↓
Softmax Output Layer (4 Classes)
```

### Why MobileNetV2?

* Lightweight and computationally efficient
* Excellent performance on image classification tasks
* Suitable for deployment on resource-constrained environments

---

## 📊 Performance

| Metric       | Value                     |
| ------------ | ------------------------- |
| Accuracy     | 96%                       |
| Classes      | 4                         |
| Architecture | MobileNetV2 + Custom Head |

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* MobileNetV2
* NumPy
* Matplotlib
* Streamlit

---

## 📂 Project Workflow

1. Collect and preprocess parrot image dataset.
2. Apply image augmentation and normalization.
3. Use MobileNetV2 as the feature extractor.
4. Add custom classification layers.
5. Train and validate the model.
6. Deploy the prediction interface using Streamlit.

---

## 📸 Supported Classes

| Class        | Description                             |
| ------------ | --------------------------------------- |
| African Grey | Intelligent grey-colored parrot species |
| White Parrot | White-feathered parrot species          |
| Amazon Green | Green-colored Amazon parrot             |
| Macaw        | Large colorful parrot species           |

---

## ⚠️ Deployment Note

The frontend was developed using Streamlit and works correctly in a local environment. However, public deployment could not be completed due to compatibility issues between TensorFlow, Python versions, and hosting platform dependencies.

Despite the deployment limitation, the project runs successfully on a local machine with the required environment setup.

---

## 👨‍💻 Author

**Subhadip Some**

Aspiring AI/ML Engineer passionate about Deep Learning, Computer Vision, and building intelligent applications that solve real-world problems.
