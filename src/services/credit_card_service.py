from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_Client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))

        result = card_info.result()

        for document in result.documents:
            fields = document.get("fields", {})

            return {
                "CardholderName": fields.get("CardholderName", {}).get("value", "Not Found"),
                "CardNumber": fields.get("CardNumber", {}).get("value", "Not Found"),
                "ExpirationDate": fields.get("ExpirationDate", {}).get("value", "Not Found"),
                "SecurityCode": fields.get("SecurityCode", {}).get("value", "Not Found"),
                "BankName": fields.get("IssuingBank", {}).get("value", "Not Found")
            }

    except Exception as e:
        print(f"Error analyzing credit card: {e}")
        return None