from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_model():
    model_name_or_path = "TehranNLP-org/electra-base-ag-news-2e-5-42"
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path, num_labels=4)
    tokenizer.save_pretrained("/code/.cache")
    model.save_pretrained("/code/.cache")