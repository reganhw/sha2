# SHA-256 
### Overview
This is a Python programme that performs SHA-256 hashing. It was built following this [NIST document](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf) and the variables are named accordingly.
### Structure
- **sha256.py:** Main encryption function. When run from the command line, it takes in a string input and prints the SHA-256 hash.
- **bitwise_funcs.py:** Bitwise functions that are the building blocks of the algorithm (ROTR, SHR, Sigma functions.).
- **preprocessing.py:** Functions for preprocessing a message so that it is suitable to put through the main algorithm.
- **constants.py:** Constants specified in the NIST document.
### References
- I referenced [sha256algorithm.com](https://sha256algorithm.com/) by [@dmarman](https://github.com/dmarman) and the corresponding [Javascript code](https://github.com/dmarman/sha256algorithm/blob/main/src/classes/sha.js) to test helper functions.
