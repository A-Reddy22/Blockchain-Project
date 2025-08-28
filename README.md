# Mini Blockchain (Python + Flask)

A simple blockchain implementation built from scratch in **Python** with a **Flask** API.  
This project demonstrates the fundamentals of distributed ledgers, transactions, Proof of Work, and consensus across nodes.  

---

## 🚀 Features
- Create and store transactions
- Mine new blocks using a **Proof of Work (PoW)** algorithm
- Query the blockchain state via API
- Register multiple nodes for decentralization
- Reach agreement on the **longest valid chain** using a Consensus Algorithm

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask** (for RESTful API endpoints)
- **Requests** (for node-to-node communication)
- **Postman / cURL** (for testing)

---

## 📌 API Endpoints

- `GET /mine` → Mine a new block and receive a reward  
- `POST /transactions/new` → Add a new transaction (`sender`, `recipient`, `amount`)  
- `GET /chain` → View the full blockchain  
- `POST /nodes/register` → Register neighboring nodes  
- `GET /nodes/resolve` → Run the Consensus Algorithm to resolve conflicts  

---
