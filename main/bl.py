from main.models import UsefulNumber, UsefulText


class NumberHandler:
    def __init__(self, validated_data):
        self.number = validated_data['number']

    def run(self):
        UsefulNumber.objects.create(number=self.number)
        all_useful_numbers = UsefulNumber.objects.all()
        average_number = \
            sum([entity.number for entity in all_useful_numbers]) / all_useful_numbers.count()
        return {'Average number': average_number}


class TextHandler:
    def __init__(self, validated_data):
        self.text = validated_data['text']

    def run(self):
        UsefulText.objects.create(text=self.text)
        all_useful_texts = UsefulText.objects.all()
        concatenated_text = ' SPAM '.join([entity.text for entity in all_useful_texts])
        return {'Concatenated text': concatenated_text}
