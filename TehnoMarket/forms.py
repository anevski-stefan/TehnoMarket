from django import forms

from TehnoMarket.models import Product,Comment,PaymentMethod


class ContactForm(forms.Form):
    name = forms.CharField(label="Име", max_length=100)
    email = forms.EmailField(label="Е-маил адреса", max_length=100)
    message = forms.CharField(label="Порака", widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class LoginForm(forms.Form):
    username = forms.CharField(label="Корисничко име", max_length=100)
    password = forms.CharField(label="Лозинка", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"



class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Име", max_length=100)
    last_name = forms.CharField(label="Презиме", max_length=100)
    username = forms.CharField(label='Корисничко име', max_length=100)
    email = forms.EmailField(label="Е-маил адреса", max_length=100)
    password = forms.CharField(label="Лозинка", widget=forms.PasswordInput)
    city = forms.CharField(label='Град', max_length=100)
    address = forms.CharField(label='Адреса на живеење', max_length=100)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.RadioSelect):
                field.field.widget.attrs["class"] = "form-control"

class PersonalInfoForm(forms.Form):
    name = forms.CharField(label="Име", max_length=100)
    surname = forms.CharField(label="Презиме", max_length=100)
    email = forms.EmailField(label="Е-маил адреса", max_length=100)
    address = forms.CharField(label='Адреса на живеење', max_length=100)
    city = forms.CharField(label='Град', max_length=100)
    password = forms.CharField(label="Лозинка", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ("seller","is_approved",)
        labels = {
            'category': 'Категорија',
            'image': 'Слика од производот',
            'name': 'Име на производот',
            'stock': 'Залиха',
            'price': 'Цена',
            'description': 'Опис на производот',
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ("author", "date_created", "product",)

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.RadioSelect):
                field.field.widget.attrs["class"] = "form-control"


class SelectPaymentMethodForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PaymentMethod
        fields = '__all__'
        exclude = ("buyer",)

    def __init__(self, *args, **kwargs):
        super(SelectPaymentMethodForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.RadioSelect):
                field.field.widget.attrs["class"] = "form-control"