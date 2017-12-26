# [mnemonic] Maltego Local Transforms
Maltego Local Transforms to use mnemonic Passive DNS - https://passivedns.mnemonic.no/

# Prerequisites
- Python 2.7.x + requests, re module

# Setup
- Put all python files into your working directory. (e.g. C:\Maltego\Transforms\mnemonic)
- Open mnemonic.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  
  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\mnemonic

# Transforms
- domain_to_ip.py
- ip_to_domain.py
