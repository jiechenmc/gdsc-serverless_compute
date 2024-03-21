# Make sure that requirements.txt has the following 2 lines
# functions-framework==3.*
# google-cloud-storage

import functions_framework
from google.cloud import storage


def upload_blob_pdf(bucket_name, destination_blob_name, file_data):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(
        file_data,
        content_type='application/pdf',
    )
    
    blob.make_public()
    return blob.public_url

    
@functions_framework.http
def hello_http(request):

    # request_json = request.get_json(silent=True)
    request_args = request.args

    #name = request_json['name']

    data = request.get_data()
    dest_filename = request_args["dest"]

    #upload_blob("loqi-loqi.appspot.com", "requirements.txt", "requirements.txt")

    return upload_blob_pdf("loqi-loqi.appspot.com", dest_filename, data)
