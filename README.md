# 🌍 Language Detection System using Machine Learning

## 📌 Overview

This project is a **Language Detection System** built using Machine Learning. It can automatically identify the language of a given text input by learning patterns from labeled text data.

The model is trained using a dataset of text samples and their corresponding languages, and it predicts the language for new, unseen text entered by the user.

---

## 🚀 Features

* 🔤 Automatic language detection from text
* ⚡ Fast and efficient prediction using Naive Bayes
* 🧠 Machine learning-based approach
* 📊 Model evaluation with accuracy score
* 💬 Real-time user input prediction

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine learning tools

---

## 📂 Project Workflow

1. **Data Loading**

   * Load dataset (`new_data.csv`) containing text and language labels

2. **Data Preprocessing**

   * Extract input text (`Language` column)
   * Extract labels (`Label` column)
   * Handle missing values

3. **Feature Extraction**

   * Convert text into numerical format using **CountVectorizer (Bag-of-Words)**

4. **Train-Test Split**

   * Split dataset into training and testing sets

5. **Model Training**

   * Train a **Multinomial Naive Bayes** classifier

6. **Prediction**

   * Accept user input
   * Predict the language of the text

7. **Evaluation**

   * Calculate model accuracy on test data

---

## 🧪 Example Usage

```bash
Enter some text: Bonjour tout le monde
Output: French
```

---

## 📊 Model Performance

The model is evaluated using:

* **Accuracy Score**
* **Classification Report**

Example:

```python
print(model.score(X_test, y_test))
```

---

## 💡 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/language-detection-ml.git
```

2. Navigate to the project folder:

```bash
cd language-detection-ml
```

3. Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

4. Run the script:

```bash
python main.py
```

---

## 📁 Dataset

Make sure you have a dataset file named:

```
new_data.csv
```

With columns:

* `Language` → Text data
* `Label` → Language name

---

## 🔮 Future Improvements

* 🌐 Add support for more languages
* 🧠 Use advanced models (LSTM, Transformers)
* 🎯 Improve accuracy with better preprocessing
* 🖥️ Build a web interface using Flask or Streamlit

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Aryan Khalique**

---

⭐ If you found this project helpful, don't forget to star the repo!
