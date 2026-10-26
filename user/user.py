from django import forms 

class UserForm (forms.Form):
    Itemname = forms.CharField(max_length=30,label="Enter Item Name")
    costprice = forms.CharField(label="Enter cost price")
    # cateogry and company choice
    cateogry = forms.ChoiceField(choices=[('','Select cateogry'),
    ('Electronics','Electronics'),
    ('Clothing','Clothing'),('books','Books'),
    ('mobile','mobile')],label="cateogry")   
    company  = forms.ChoiceField(choices=[('','Select company'),
    ('Samsung','Samsung'),
    ('Apple','Apple'),('Pepe Jeans','Pepe Jeans'),
    ('FabIndia','FabIndia'),('Biba','Biba')
    ],label="company")    
 # data of manufacturing ,  Date of expiry 
    dom = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="Date of manufacturing ")  
    doe = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="Date of expiry")
    discount = forms.DecimalField(max_digits=5, decimal_places=2, initial=0.00,label="Enter Discount")
    
    
