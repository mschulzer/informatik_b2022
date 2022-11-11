class StudentAdd(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email', 'training_status']
        # subject = forms.ChoiceField(choices = SUBJECT_CHOICES, widget = forms.RadioSelect())
        # date = forms.DateField(widget = forms.DateInput(attrs = {'type': 'date', 'max':datetime.now().date()}))
