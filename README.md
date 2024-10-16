# SHA2
### Overview
This is a Python programme that performs SHA2 hashing. It was built following this [NIST document](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf) and the variables are named accordingly.
### Structure
- **basic_funcs.py:** This file contains the bitwise functions that are the building blocks of the algorithm. It also has a string-to-binary encoding function.
- **sha2.py** Function `sha2` that performs SHA2 encryption based on a dictionary called `config`. The dictionary `config` should have the following fields:
  - **bl:** bit-length. Integers are regarded as bl-bits.
  - **mbl:** message block length
  - **t_lim:** upper limit for _t_ for the main hashing part
  - **MASK:** 2**bl -1
  - **K_constants:** random-looking constants defined in the NIST document
  - **initial_hash:** initial values for the hashing algorithm to take in
  - **sigma functions:** sigma functions as defined in the NIST document
  - **get_k:** a function that calculates the number of zeroes to append during preprocessing 

- **groups.py:** This file contains the `grp256` and `grp512` functions. The function `grp256` runs `sha2` with configurations for SHA256. The function `grp512` runs `sha2` with configuartions for SHA512.
- **main.py:** This file contains `sha224`, `sha256`, `sha384`, `sha512`, `sha512/224`, and `sha512/256`. When run from the command line, it takes in an input and generates hashes for all six algorithms.
  - Algorithms `sha224` and `sha256` are similar. Both run `grp256` under the hood.
  - Algorithms `sha384`, `sha512`, `sha512/224`, and `sha512/256` are similar. These run `grp512` under the hood.
- **constants.py:** Constants specified in the NIST document.
- **tests:** Testing was done using Pytest.
