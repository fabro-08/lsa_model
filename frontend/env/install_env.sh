# Variables config.yaml
env_name=$(grep 'params:' -A 4 config.yaml | grep 'env_name' | awk '{print $2}')
python_version=$(grep 'model:' -A 4 config.yaml | grep 'python_version' | awk '{print $2}')
 
 
# Crea el entorno conda para MODEL y actívalo
if conda env list | grep -wq "$env_name"; then
    conda remove -n "$env_name" --all --yes
fi
 
conda create -y -n "$env_name" python="$python_version"
source activate "$env_name"
 
PIP_YES=1 pip install ipykernel
PIP_YES=1 pip install -r requirements.txt
 
python -m ipykernel install --user --name "$env_name"
 
# Guarda las dependencias en requirements.txt
pip list --format=freeze > freeze_req/req.txt