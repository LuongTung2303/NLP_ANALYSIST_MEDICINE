label_list = [
    "O", "B-DISEASE", "I-DISEASE", "B-DRUG", 
    "I-DRUG", "B-SYMPTOM", "I-SYMPTOM"
]
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for i, label in enumerate(label_list)}