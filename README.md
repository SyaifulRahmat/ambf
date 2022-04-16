
#### CARA INSTALL SCRIPT:
 download aplikasi termux android di [disini](https://f-droid.org/repo/com.termux_118.apk)
 lalu buka aplikasinya ketikan perintah dibawah ini.
 ```
 $ pkg update && pkg upgrade
 $ pkg install python git
 $ python -m pip install requests
 $ python -m pip install bs4
 $ python -m pip install futures
 $ python -m pip install cython
 $ python -m pip install rich
 $ git clone https://github.com/SyaifulRahmat/ambf
 $ cd ambf
 $ cythonize -i ambf.c
 $ python run.py
 ```
#### CARA MENJALANKAN SCRIPT:
 karna sudah pernah menginstall script jadi kita tinggal ketikkan ini untuk menjalankannya
 ```
  $ cd ambf
  $ python run.py
 ```
