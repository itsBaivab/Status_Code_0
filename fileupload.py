import os  
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings  
from dotenv import load_dotenv  
  
# Load environment variables from .env file  
load_dotenv()  
  
def upload_pdf_to_blob(pdf_path, container_name, blob_name):  
    try:  
        # Retrieve the connection string from the environment variable  
        connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')  
        if not connection_string:  
            raise ValueError("AZURE_STORAGE_CONNECTION_STRING environment variable not found")  
  
        # Create a BlobServiceClient  
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)  
  
        # Create a container client  
        container_client = blob_service_client.get_container_client(container_name)  
  
        # Create the container if it does not exist  
        try:  
            container_client.create_container()  
        except Exception as e:  
            print(f"Container creation skipped: {e}")  
  
        # Create a blob client using the local file name as the name for the blob  
        blob_client = container_client.get_blob_client(blob_name)  
  
        # Set the content type to application/pdf  
        content_settings = ContentSettings(content_type='application/pdf')  
  
        # Upload the PDF file  
        with open(pdf_path, "rb") as data:  
            blob_client.upload_blob(data, overwrite=True, content_settings=content_settings)  
  
        # Construct the URL to the uploaded PDF  
        blob_url = blob_client.url  
        print(f"PDF uploaded to: {blob_url}")  
  
        return blob_url  
  
    except Exception as e:  
        print(f"Error: {e}")  
        return None  
  
# Example usage  
pdf_path = "student_information_boundary_and_image.pdf"  # Path to your PDF file  
container_name = "pdf121"  
blob_name = "pdfupload121"  
  
upload_pdf_to_blob(pdf_path, container_name, blob_name)  
