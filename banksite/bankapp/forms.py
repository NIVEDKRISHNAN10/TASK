from django import forms
from .models import Form, Material

class UserForm(forms.ModelForm):
    district = forms.ChoiceField(choices=[('Ernakulam', 'Ernakulam'), ('Kannur', 'Kannur'), ('Thrissur', 'Thrissur')])

    materials_provide = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Form
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type', 'materials_provide']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'district' in self.data:
            self.fields['branch'].choices = self.get_branch_choices(self.data['district'])
        elif self.instance and self.instance.district:
            self.fields['branch'].choices = self.get_branch_choices(self.instance.district)

    def get_branch_choices(self, district):
        if district == 'Ernakulam':
            branch_choices = [('aluva', 'Aluva'), ('kakkanad', 'Kakkanad')]
        elif district == 'Kannur':
            branch_choices = [('payyanur', 'Payyanur'), ('pazhayangadi', 'Pazhayangadi')]
        elif district == 'Thrissur':
            branch_choices = [('chavakkad', 'Chavakkad'), ('guruvayur', 'Guruvayur')]
        else:
            branch_choices = []

        return branch_choices



