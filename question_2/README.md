# Question 2: Sentiment Analysis on IMDB Dataset

This folder contains solutions for sentiment classification using both:
- 🔹 Traditional ML approach (TF-IDF + SVM)
- 🔹 Transformer-based fine-tuned model (BERT)

---

## 📄 Dataset

The dataset used is the **IMDB Movie Reviews Dataset** (50K reviews with sentiment labels).

To download the dataset, use the following code snippet in Python:

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")

print("Path to dataset files:", path)