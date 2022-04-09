# CROSS VALIDATION SPLIT AND STATISTICS
Splits NER dataset into cross validation and generate statistics.

Generates subfolder for each version and fold's, with stats and filtered max_length sentence.


## How to use 
- Example

python main.py --f corejur_nerv2.conll --kfold 5 --version versao0 --max_length 250



## Args 
Args:

    --f filename (example: dataset.conll)
    
    --kfold kfold's number (example: 5)
    
    --version folder_version (example: version_0)
    
    --max_length filter for sentence tokens max_length (example: 256)

    --verbose For showing the graphs, and editing them (default = False)
    


<img src="https://user-images.githubusercontent.com/58753373/157150045-d1749366-3ac8-412b-b71d-20b89105793d.png" width="600" height="200">


TO DO

[ X ] Args de verbose para ver ou não os gráficos

[ X ] Pre processamento de dataset -> filtro de sentença máxima 

[ X ] Pre processamento de dataset -> remoção de entidades

[ X ] Pre processamento de dataset -> remoção de sentenças sem nenhuma entidade 

[ ] Criar uma thread para a visualização dos gráfico, para permitir a execução durante a visualização
