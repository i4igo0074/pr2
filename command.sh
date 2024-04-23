mkdir virus
cp main.py virus/
cd virus
python3 main.py
ls / > data.txt
mv data.txt /Home/islambek
cd ..
rm -rf virus
