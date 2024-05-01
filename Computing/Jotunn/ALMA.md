Setting up and running ALMA on Jotunn

You first log in to Jotunn using your username and ssh-key


## Setting up ALMA
```bash
conda create --name alma-r python=3.11
conda activate alma-r
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
git clone https://github.com/fe1ixxu/ALMA.git
cd ALMA
bash install_alma.sh
```
- copy scripts to ALMA folder
- interactive mode
- batch mode
