# 💰 Prop Firm Profit Calculator

A simple, responsive profit calculator for prop firm traders that estimates potential earnings based on:

* Funded account size
* Risk-to-Reward Ratio (R)
* Risk per trade (%)
* Profit split
* Live USD → PHP exchange rate

The calculator automatically converts your estimated payout into Philippine Pesos (PHP).

---

## ✨ Features

* 📈 Select funded account size

  * $5,000
  * $10,000
  * $25,000
  * $50,000
  * $100,000
  * $200,000
* 🎯 Custom Risk-to-Reward (R)
* ⚠️ Adjustable Risk per Trade (%)
* 💵 Adjustable Profit Split
* 🌍 Live USD → PHP exchange rate
* 📱 Mobile-friendly interface
* ⚡ Instant calculations

---

## 📊 Formula

```
Profit % = Risk Reward (R) × Risk %

Gross Profit = Account Size × Profit %

Take Home = Gross Profit × Profit Split

PHP Value = Take Home × USD/PHP Exchange Rate
```

### Example

```
Funded Account: $50,000

Risk Reward: 60R

Risk: 0.5%

Profit Split: 80%

Profit %
= 60 × 0.5
= 30%

Gross Profit
= 30% × $50,000
= $15,000

Take Home
= $15,000 × 80%
= $12,000

PHP
= $12,000 × Current USD/PHP Rate
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/prop-firm-profit-calculator.git

cd prop-firm-profit-calculator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

If `streamlit` is not recognized:

```bash
python -m streamlit run app.py
```

---

## 📦 Requirements

* Python 3.10+
* Streamlit
* Requests

Install:

```bash
pip install streamlit requests
```

---

## 📱 Deployment

### Streamlit Community Cloud

1. Push your project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app.
4. Select your repository.
5. Deploy.

### Local

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📌 Future Features

* Multiple funded accounts
* Monthly income estimator
* Daily profit tracker
* Prop firm presets
* Trading journal
* Risk management calculator
* Challenge fee ROI calculator
* Account scaling calculator
* Dark mode
* Export to PDF

---

## ⚠️ Disclaimer

This calculator provides estimates only and does not guarantee trading profits. Actual results depend on market conditions, execution quality, prop firm rules, and individual trading performance.

Always trade responsibly and never risk more than you can afford to lose.

---

## 📄 License

MIT License

Feel free to use, modify, and share this project.
