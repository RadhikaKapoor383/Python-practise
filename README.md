# Python Practice

A personal learning repository covering Python fundamentals, NumPy, Machine Learning with scikit-learn, and Logic Programming with Prolog — built as part of both self-study and university AI lab coursework.

---

## 🗂️ Repository Structure

```
Python-practise/
├── practice1.py                  # First list exercises
├── lists.py                      # In-depth list practice
├── Tuple.py                      # Tuple operations
├── Dictionary.py                 # Dictionary operations
├── NumPy.py                      # NumPy arrays & math functions
├── linearRegression.ipynb        # ML: Multiple Linear Regression
├── Dataset/
│   └── data.csv                  # Calories dataset
└── AI Lab codes/
    ├── AI_LAB4_radhika.ipynb     # Python basics (arithmetic)
    ├── AI_LAB5_radhika.ipynb     # Simple Linear Regression
    ├── AI_LAB6_radhika.ipynb     # Polynomial Regression
    ├── AI_LAB7_radhika.ipynb     # Naive Bayes Classification
    ├── AI_LAB10_radhika.ipynb    # Decision Tree, Random Forest, SVM
    ├── Lab Manuals/              # PDF lab sheets
    └── Prolog files and PDFs/
        ├── lab1_practise.pl      # Prolog facts
        ├── lab2_practise.pl      # Prolog rules & recursion
        └── radhika_lab2.pl       # Prolog interactive predicates
```

---

## Python Basics

| File | Topics Covered |
|---|---|
| `practice1.py` | List indexing, `append`, `remove`, `insert`, list comprehension |
| `lists.py` | Slicing, `sort`, `copy` vs reference, `enumerate`, `sorted(key=len)`, list comprehension with conditions |
| `Tuple.py` | Tuple creation, unpacking, `zip`, `enumerate`, converting to list, ignoring values with `_` |
| `Dictionary.py` | CRUD operations, `get`, `pop`, `del`, looping with `.items()`, nested dictionaries |
| `NumPy.py` | 1D & 2D arrays, `.shape`, `np.sqrt`, `np.sin`, `np.cos`, `np.exp`, `np.log` |

---

## 🤖 Machine Learning (Jupyter Notebooks)

### 📓 `linearRegression.ipynb` — Multiple Linear Regression
- Dataset: `data.csv` (predicting **Calories burned**)
- Feature scaling with `StandardScaler`
- Train/test split, model evaluation with **MSE** and **R² score**
- Libraries: `pandas`, `numpy`, `scikit-learn`

### 📓 `AI_LAB5` — Simple Linear Regression
- Dataset: House size (SqFt) → Price prediction
- Metrics: MAE, MSE, R² score
- Visualized with `matplotlib`

### 📓 `AI_LAB6` — Polynomial Regression
- Dataset: Engine RPM → Fuel Consumption (non-linear pattern)
- Degree-3 polynomial using `PolynomialFeatures`
- Printed full polynomial equation with coefficients

### 📓 `AI_LAB7` — Classification: Naive Bayes & LDA
- Dataset: Glucose & blood pressure → **Diabetes prediction**
- Models: `GaussianNB`, `LinearDiscriminantAnalysis`
- Evaluation: Confusion matrix, precision, recall, accuracy
- Visualized with `seaborn` heatmap

### 📓 `AI_LAB10` — Classification: Decision Tree, Random Forest & SVM
- Dataset: `credit_card_default.csv` — **credit default prediction**
- Data cleaning: missing values, `LabelEncoder`, `get_dummies`
- Models compared: `DecisionTreeClassifier`, `RandomForestClassifier`, `SVC`
- Metrics: accuracy, precision, recall

---

## 🔵 Prolog (Logic Programming)

| File | Topics Covered |
|---|---|
| `lab1_practise.pl` | Defining facts — `likes`, `tall`, `short`, `has`, `fruit` |
| `lab2_practise.pl` | Rules — `mortal(X):-human(X)`, recursive `is_in`, OR logic with `;`, compound predicates |
| `radhika_lab2.pl` | Person knowledge base with interactive `get_height`, `get_weight`, `get_hobby` predicates |

---

## Concepts Practiced

**Python Fundamentals**
- Lists, Tuples, Dictionaries — CRUD, iteration, comprehension
- NumPy arrays and mathematical functions

**Machine Learning**
- Supervised Learning — Regression & Classification
- Data preprocessing — scaling, encoding, null handling
- Model evaluation — MSE, R², accuracy, confusion matrix

**Logic Programming**
- Prolog facts, rules, recursion, and interactive queries

---

## Tech Stack

- **Python 3**
- **Jupyter Notebook**
- **pandas**, **NumPy**, **scikit-learn**, **matplotlib**, **seaborn**
- **SWI-Prolog**

---

## How to Run

**Python files:**
```bash
python lists.py
python Dictionary.py
# etc.
```

**Jupyter Notebooks:**
```bash
pip install notebook pandas numpy scikit-learn matplotlib seaborn
jupyter notebook
```

**Prolog files:**
```bash
# Requires SWI-Prolog installed
swipl lab2_practise.pl
```

---

## Author

**Radhika Kapoor** — [GitHub](https://github.com/RadhikaKapoor383)
