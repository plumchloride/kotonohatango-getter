[![Open in Code Ocean](https://codeocean.com/codeocean-assets/badge/open-in-code-ocean.svg)](https://codeocean.com/capsule/7739771/tree)
[![Open in pypi](https://img.shields.io/pypi/v/kotonohagetter)](https://pypi.org/project/kotonohagetter/)
# kotonohatango-getter
ことのはたんごのプレイヤーの集計データを可視化できるPython Package。  
Python Package for visualization of aggregate data of players in "Kotoha Tango".

[ことのはたんご](https://plum-chloride.jp/kotonoha-tango/index.html)

## Example of use
```
pip install kotonohagetter
python kotonohagetter.py 20
```
usage: kg.py [-h] [--F F] Number  
visualization of aggregate data of players in Kotoha Tango  
positional arguments:  
　Number      Get the [Number]th data.(int)  
optional arguments:  
　-h, --help  show this help message and exit  
　--F F       Getting word data?(bool:[y,t,true]or[n,f,false])[Default:True] 

**output**  
  
![image](https://user-images.githubusercontent.com/70005022/171073813-301307d5-268d-42ec-9fc8-5de011af87aa.png)
  
1-10 Percentage of users cleared there.  
x Percentage of users who could not clear.
