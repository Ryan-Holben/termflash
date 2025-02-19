# 🚨 termflash 🚨

A simple utility to flash the terminal screen, useful for grabbing attention.  
Ideal for alerting when a long-running job is complete.

## 📦 Features  
- Flashes the terminal at a configurable rate  
- Set the total duration of flashing  
- Useful for automation and script notifications  

## 🚀 Installation  
 
```sh
git clone https://github.com/Ryan-Holben/termflash.git # Clone the repo
cd termflash
pip install .   # Install via pip
cd .. && rm -rf termflash   # Remove the repo folder
```

## 🖥️ Example usage

```sh
run my_long_training.py && python3 termflash.py --flash_rate 0.1 --duration 1.0
```