# SHA2
### 개요
SHA2 해싱을 하는 파이썬 프로그램입니다 . SHA2에 대한 [미국 국립표준기술연구소 문서](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)를 기반으로 만들어졌으며 변수 이름 또한 해당 문서를 참조하여 지었습니다.

### 사용법
(1) Git 저장소를 복사한 뒤 새로 생성된 디렉토리로 이동합니다.
```
# git clone https://github.com/reganhw/sha2.git
# cd sha2
```
(2) main 파일을 실행합니다.
```
# python main.py
```
다음과 같이 인풋을 받는 프롬프트가 출력됩니다.
```
Input:
```
(3) 원하는 문자열을 입력합니다.
```
Input: sha2algorithm
```
다음과 같이 해싱 결과가 출력됩니다.
```
--SHA224:  1c83fa0e2b75a0a19d2732ab27c0dd7fbbfd9f9cab3286fbc80b7be1
--SHA256:  610d6abdaaaef84c588dae50aa886577c5756b9884b295a33eef4cd90737626e
--SHA384:  de22e9d3f4bf405f99d8d277d3e28607a25cb70577cad4a3a7a8827c27e46d2737391600ac6488a6a81c7ea0a6cd38ef
--SHA512:  ca5e7314ef96ad0acb43f57950630511e581928747be7a3e4100f7da128e3b2834ef7bffa406edffdbeef07689a291eeb6c1209f36cf40b3742a0e61dac20ece  
--SHA512/224:  36ecd6399e439d5c10d1cc22606905facc0ffbf0fd2054819fc35648
--SHA512/256:  38694fbc005163ea46cb0abc08ab62ed4ba185e4c48c694beceab5a24359b82a
```
이는 가장 간단한 사용법이며 SHA2 해싱이 필요할 시 모듈로도 사용할 수 있습니다. main.py에 `sha224`, `sha256`, `sha384`, `sha512`, `sha_512_224`, `sha_512_256`이 각각 정의되어 있기 때문에 필요한 해싱만 할 수 있습니다.

### 구조
SHA2 알고리즘은 SHA256 계열(SHA224, SHA256)과 SHA512 계열(SHA384, SHA512, SHA512/224, SHA512/256)로 나눌 수 있습니다. 따라서 `grp256`, `grp512` 함수가 정의되어 있으며 `sha224`, `sha256`은 `grp256`을, `sha384`, `sha512`, `sha_512_224`, `sha_512_256`은 `grp512`를 호출합니다. 또한 `grp256`, `grp512`는 `sha2`라는 기본 뼈대 함수를 호출합니다.

- **basic_funcs.py:** 알고리즘의 기초가 되는 비트 함수가 있는 파일입니다. 또한 문자열을 이진수로 치환하는 함수도 있습니다.
- **sha2.py** 함수 `sha2`가 정의되어 있습니다. `sha2`는 메시지 `M`과 딕셔너리 `config`을 인자로 받아 `config`의 필드에 따라 다른 해싱을 진행합니다. `config`의 필드는 다음과 같습니다.
  - **bl:** bit length
  - **mbl:** message block lengthm 즉 메시지 블락의 길이
  - **t_lim:** 해싱시 필요한 변수 t의 상한값
  - **MASK:** 2**bl -1
  - **K_constants:** 미국 국립표준기술연구소 문서에 정의된 상수들
  - **initial_hash:** 미국 국립표준기술연구소 문서에 정의된 알고리즘의의 초기값
  - **sigma functions:** 미국 국립표준기술연구소 문서에 정의된 시그마 함수들
  - **get_k:** 메시지 블락에 패딩할 0의 개수를 계산하는 함수
- **groups.py:** `grp256`, `grp512` 함수가 있는 파일입니다. `grp256`는 SHA256에 해당하는 config를 사용하여 `sha2`를 실행합니다. `grp512`는 SHA512에 해당하는 config를 사용하여 `sha2`를 실행합니다.
- **main.py:** `sha224`, `sha256`, `sha384`, `sha512`, `sha_512_224`, `sha_512_256` 함수가 있는 파일입니다. 터미널에서 __main__으로 실행했을 시 인풋을 받아 모든 SHA2 함수에 대한 해시를 출력합니다.
  - `sha224`,`sha256`은 `grp256`을 호출합니다.
  - `sha384`, `sha512`, `sha_512_224`, `sha_512_256`은 `grp512`를 호출합니다.
- **constants.py:** 각종 상수를 담고 있는 파일입니다.
- **tests:** pytest를 이용한 테스트입니다.

### 테스팅 방법
(1) pytest를 다운받습니다.
```
# pip install -q pytest==8.3.3.
```
(2) sha2 디렉토리로 이동합니다.
```
# cd sha2
```
(3) 다음 문법을 활용합니다. <br>
`basic_funcs` 기본 함수 테스팅:
```
# python -m pytest tests/test_basic_funcs.py
```
`sha256`, `sha512` 등 메인 함수 테스팅:
```
# python -m pytest tests/test_algorithms.py
```
전체 테스팅:
```
# python -m pytest tests/
```