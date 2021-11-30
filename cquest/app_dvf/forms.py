from django import forms

style = "px-4 py-2 rounded-lg border border-gray-300 focus:outline-none mr-4 mt-3 mb-3 focus:ring-2 focus:ring-gray-200"
class Filter(forms.Form):

    CodeCommune = forms.TextInput(attrs={'class': style})