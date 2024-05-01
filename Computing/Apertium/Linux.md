Install and run Apertium

```bash
curl -sS https://apertium.projectjj.com/apt/install-release.sh | sudo bash
sudo apt-get -f install apertium-all-dev
mkdir Apertium
cd Apertium
git clone https://github.com/apertium/apertium-isl-eng.git
git clone https://github.com/apertium/apertium-isl.git
cd apertium-isl
./autogen.sh
make
cd ../apertium-isl-eng
./autogen.sh --with-lang1=../apertium-isl
make
echo "Hæ, ég heiti Apertium!" | apertium -d . isl-eng
```