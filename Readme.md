## Dummy FastAPI app

This is simple python PoC to demonstrate encryption of data in client-side (JS) and decryption of the data in server - side (python)

### Libraries used
- FastApi
- [Fernet JS](https://github.com/csquared/fernet.js/blob/master/README.md)
- [Cryptography](https://cryptography.io/en/latest/fernet/) 

**Steps**
- create conda environement
   `conda env create -f environment.yml`
- activate the environment
   `conda activate demo`   
- start the server by running run.sh file
    `./run.sh`   
- test the service by hitting the url
   `https://localhost:8000/hello    