conda create --name transformer python=3.11
conda activate transformer 
cd ~
mkdir Transformer
cd Transformer
curl --remote-name-all https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/278{/data-bin.zip,/fairseq_user_dir.zip,/infer_en_is.sh,/infer_is_en.sh,/sentence.bpe.model,/model_doc_enis.pt.zip,/model_doc_isen.pt.zip,/requirements.txt,/README}
pip install -r requirements.txt
