# 🚨 termflash 🚨

A simple utility to flash the terminal screen, useful for grabbing attention.  
Ideal for alerting when a long-running job is complete, e.g. building code,
running tests, or training a model.


## 📦 Features  
- Flashes the terminal at a configurable rate & duration
- Combine with other commands to flash green or red for pass/fail exit codes
- Useful for automation and script notifications  

## 🚀 Installation  
 
```sh
git clone https://github.com/Ryan-Holben/termflash.git  # Clone the repo
pip install termflash/                                  # Install via pip
rm -rf termflash                                        # Remove the repo folder
```

## 🖥️ Example usage

```sh
run_my_long_training; termflash --code $?
```