from passporteye import read_mrz
from fastapi import FastAPI, UploadFile, File
from postprocess import Postprocessor
import uvicorn
import os
import glob

app = FastAPI()
IMAGE_PATH = './uploaded_images'
postprocessor = Postprocessor()

@app.get('/')
def index():
	return{
		"message": "hello world"
	}

@app.post("/passport_extract")
async def passport_extract(image: UploadFile=File(...)):
	try:
		content = image.file.read()
		path = os.path.join(IMAGE_PATH, image.filename)
		with open(path, 'wb') as f:
			f.write(content)
		mrz = read_mrz(path).to_dict()
		result = {
			"mrz_type": mrz.get('mrz_type'),
			"type": mrz.get('type'),
			"surname": mrz.get('surname'),
			"names": mrz.get('names'),
			"passport_number": mrz.get('number'),
			"country_code": mrz.get('country'),
			"nationality": mrz.get('nationality'),
			"sex": mrz.get('sex'),
			"date_of_birth": mrz.get('date_of_birth'),
			"expiration_date": mrz.get('expiration_date'),
			"valid_score": mrz.get('valid_score')
		}
		result = postprocessor(result)
  
	except Exception:
		return{
			"message": "fail",
			"info": {}
		}
	finally:
		image.file.close()
		for f in glob.glob(IMAGE_PATH + '/*'):
			os.remove(f)
	return {
		"message": "success",
		"info": result
	}
    
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run("app:app", host='0.0.0.0', port=port, reload=True)