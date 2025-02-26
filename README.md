# **PharmAssist**
An AI-powered application to automate the extraction and matching of handwritten prescriptions to assist pharmacists.

## **Overview:**
PharmAssist is designed to help pharmacies process handwritten prescriptions efficiently. By leveraging OCR (Optical Character Recognition) and batch processing, the application extracts medicine names from prescriptions and matches them against a predefined medicine database.

## **Features (Current Implementation)**
Batch Processing of Prescription Images – Allows multiple prescription images to be processed at once.\
OCR-Based Text Extraction – Uses Google Vision API to extract text from handwritten prescriptions.\
Medicine Name Matching – Compares extracted text against a structured medicine database(taken from the WHO website) to identify prescribed drugs.

## **Tech Stack:**
Python – Core logic and data processing\
Google Vision API – Handwritten text recognition\
Pandas – Handling and processing the medicine database\
OpenCV / PIL (optional) – Image preprocessing

## **Installation & Setup**:
1. **Clone the Repository*
```
git clone https://github.com/yourusername/pharmassist.git
cd pharmassist
```

3. **Set Up a Virtual Environment (Recommended)**
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

5. **Install Dependencies**
```
pip install -r requirements.txt
```

7. **Set Up Google Vision API Credentials**
Obtain API credentials from Google Cloud Console.\
Download the JSON key file and save it in the project directory.\
Set the environment variable:\
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"\
(For Windows, use set instead of export.)

## **Usage:**
**Batch Process Prescription Images:**\
Upload the images of handwritten prescriptions in a folder named "test_images".\
Create an empty folder "processed_images" to store images after pre-processing.


**Match Extracted Medicines Against Database:**\
Run the medicine-data-convert.py file to obtain a json file of the medicine database.\
Insert your Google Vision API key in the code of vision_ocr.py and run it.\
Run the file vision_ocr.py.\
Expected Output:
```
✅ Batch processing complete. Extracted medicines saved to output_medicines.json
```

## **Future Enhancements**
UI for pharmacists to upload images & stock data manually.\
Error handling for unmatched or expired medicines.\
Integration with order generation and stock management.\
Cloud-based deployment for real-world pharmacy use.

## **Contributing:**
If you'd like to contribute, feel free to open an issue or submit a pull request.
