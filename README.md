# wowai-passport-reader
## 1. INSTALLATION
### Preprequisite
We must have the Tesseract OCR installed to our machine and added to system path. If you are in Linux, installation is quite simple:
```
$ sudo apt-get update -y
$ sudo apt-get tesseract-ocr -y
```
### a. Build from source
```
# Create and activate a virtual environment
$ conda create -n passport_reader python=3.10 -y
$ source activate passport_reader
 
# Install dependencies
$ pip install -r requirements.txt
 
# Install the PassportEye from source
$ cd PassportEye && python setup.py install
$ cd ..

# Create an empty directory for temporarily storing uploaded files
$ mkdir -p uploaded_images

# Start the API
$ python app.py
```

### b. Install via Docker
```
$ docker build -t wowai/passport-reader .
$ docker run --name passport-reader -p 8000:8000 wowai/passport-reader
```
The API is then available at http://0.0.0.0:8000/

## 2. API ENDPOINTS
### 1. POST /passport_extract
Request URL: http://0.0.0.0:8000/passport_extract
#### Request body
Key | Description | Type | Note
|--------|----------|--------|--------|
image| An image of passport| multipart/form-data| required|

#### Response
Successful response (Code 200) will return a json with following fields:
Key | Description | Type | Note
|--------|----------|--------|-------|
mrz_type| Type of machine readable zone (MRZ), being one of 'TD1', 'TD2', 'TD3'| string||
type| Type (for countries that distinguish between different types of passports) | string||
surname| Surname of passport owner| string||
names| Name of passport owner (without surname)| string||
passport_number| Passport number| string||
country code| Country code| string||
nationality| National code of passport owner's nationalities| string||
sex| 'M' - male or 'F' - female| string||
date_of_birth| Date of birth| string| dd-MM-yy|
expiration_date| Date of expiry| string| dd-MM-yy|
valid_score| The valid code of the passport and its extracted information| string||

## 3. DEMO
Here is an example of the passport extraction's result:

![passport1](https://user-images.githubusercontent.com/79528257/200649695-d5ce12fe-7827-4c39-b8d4-64dc10a5095c.jpg)

The json contains extracted information from the image:

```
{
    "message": "success",
    "info": {
        "mrz_type": "TD3",
        "type": "P",
        "surname": "TRAN",
        "names": "DINH MINH HUY",
        "passport_number": "C1489285",
        "country_code": "VNM",
        "nationality": "VNM",
        "sex": "M",
        "date_of_birth": "28-02-01",
        "expiration_date": "05-05-26",
        "valid_score": 100
    }
}
```

