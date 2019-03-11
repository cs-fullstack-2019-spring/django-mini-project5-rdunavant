from django import forms
class RecipeModel(forms.ModelForm):
    class Meta:
        exclude = ["userTableForeignKey"]
        fields = ["picture", "name", "description", "date", "creator", "edit"]