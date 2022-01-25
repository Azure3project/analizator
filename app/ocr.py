import os
from os import environ as env
import time

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from app.extracting import extract_products
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

TENANT_ID = os.environ["AZURE_TENANT_ID"]
CLIENT_ID = os.environ["AZURE_CLIENT_ID"]
CLIENT_SECRET = os.environ["AZURE_CLIENT_SECRET"]

KEYVAULT_NAME = os.environ["AZURE_KEYVAULT_NAME"]
KEYVAULT_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

_credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)
OUR_SUBSCRIPTION_KEY = _sc.get_secret("subscriptionKey").value
OUR_ENDPOINT= _sc.get_secret("endpoint").value
'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = OUR_SUBSCRIPTION_KEY
endpoint = OUR_ENDPOINT


def ocr_function(filename):
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    #print("===== Read File - remote =====")
    # Get an image with text

    # Call API with URL and raw response (allows you to get the operation location)
    images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static/uploads")

    read_image_path = os.path.join(images_folder, filename)
    read_image = open(read_image_path, "rb")

    read_response = computervision_client.read_in_stream(read_image,  raw=True)

    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    message = "You bought: "

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    txt = ''
    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                #print(line.text)
                txt += line.text

    # extract_products returns a list of all products that have been found on the receipt
    products, dates = extract_products(txt)
    message = str(products)

    return message


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
