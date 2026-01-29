# 🐧 Linux System Monitor - Mini Top Clone

A Python-based system monitoring tool that displays real-time system information similar to the `top` command.

---

## ✨ Features

- 📊 Real-time CPU usage with visual bar
- 💾 Memory usage visualization
- 🖥️ Running processes display (Top 10 by CPU)
- 🏆 Top 5 memory-hungry processes
- ⏱️ Automatic refresh every 2 seconds
- 🎨 Colorful terminal interface

---

## 🧱 Requirements

- Python 3.x
- `psutil` library

---

## 📥 Installation

### 1️⃣ Clone or download the project

```bash
git clone <your-repo-url>
cd linux-system-monitor
```
### 2️⃣ Make scripts executable

```bash
chmod +x system_monitor.py monitor.sh
```
### 3️⃣ Install dependencies
Option 1: Using helper script
```bash
./monitor.sh --install-deps
```
Option 2: Manual install
```bash
pip3 install psutil
```


🚀 Usage
▶ Run Python script directly
```bash
python3 system_monitor.py
```

▶ Using shell wrapper
Basic usage
```bash
./monitor.sh
```

With logging enabled
```bash
./monitor.sh --log
```

Custom refresh interval (e.g. 5 seconds)
```bash
./monitor.sh --interval 5
```

Simple shell-only mode (no Python dependencies)
```bash
./monitor.sh --simple
```

Show help
```bash
./monitor.sh --help
```
