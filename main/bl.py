from main.models import UsefulNumber, UsefulText
from django.db.models import Sum


class NumberHandler:
    def __init__(self, validated_data):
        self.number = validated_data['number']

    def run(self):
        UsefulNumber.objects.create(number=self.number)
        average_number = \
            UsefulNumber.objects.aggregate(Sum('number'))['number__sum'] / UsefulNumber.objects.count()
        return {'Average number': average_number}


class TextHandler:
    def __init__(self, validated_data):
        self.text = validated_data['text']

    def run(self):
        UsefulText.objects.create(text=self.text)
        all_useful_texts = UsefulText.objects.all()
        concatenated_text = ' SPAM '.join([entity.text for entity in all_useful_texts])
        return {'Concatenated text': concatenated_text}
