from django import forms

from django.contrib.auth.models import User

from .models import (
    Barang,
    Kategori,
    Supplier,
    Lokasi,
    UserProfile,
)

# =========================
# USER PROFILE FORM
# =========================


class UserProfileForm(forms.ModelForm):


    class Meta:


        model = UserProfile


        fields = [

            'foto',

            'role',

            'no_hp',

            'alamat'

        ]



        widgets = {


            'foto': forms.FileInput(

                attrs={

                    'class':'form-control'

                }

            ),



            'role': forms.Select(

                attrs={

                    'class':'form-control'

                }

            ),



            'no_hp': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Nomor HP'

                }

            ),



            'alamat': forms.Textarea(

                attrs={

                    'class':'form-control',

                    'rows':4,

                    'placeholder':'Alamat lengkap'

                }

            )


        }

# =========================
# BARANG
# =========================

class BarangForm(forms.ModelForm):

    class Meta:

        model = Barang


        fields = [
            'sku',
            'barcode',
            'nama',
            'kategori',
            'supplier',
            'satuan',
            'harga_satuan',
            'minimum_stock'
        ]


        widgets = {


            'sku': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),


            'barcode': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),


            'nama': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),


            'kategori': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),


            'supplier': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),


            'satuan': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),


            'harga_satuan': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),


            'minimum_stock': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),

        }



# =========================
# KATEGORI
# =========================

class KategoriForm(forms.ModelForm):

    class Meta:

        model = Kategori


        fields = [
            'nama',
            'deskripsi'
        ]



# =========================
# SUPPLIER
# =========================

class SupplierForm(forms.ModelForm):

    class Meta:

        model = Supplier


        fields = [
            'nama',
            'kontak',
            'alamat'
        ]



# =========================
# LOKASI
# =========================

class LokasiForm(forms.ModelForm):

    class Meta:

        model = Lokasi


        fields = [
            'kode_lokasi',
            'nama_lokasi'
        ]



# =========================
# TRANSAKSI BARANG MASUK
# =========================

class BarangMasukForm(forms.Form):


    barang = forms.ModelChoiceField(

        queryset=Barang.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    lokasi = forms.ModelChoiceField(

        queryset=Lokasi.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    jumlah = forms.IntegerField(

        min_value=1,

        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jumlah barang'
            }
        )

    )



    keterangan = forms.CharField(

        required=False,


        widget=forms.Textarea(

            attrs={
                'class':'form-control',
                'rows':3,
                'placeholder':'Keterangan transaksi'
            }

        )

    )
# =========================
# TRANSAKSI BARANG KELUAR
# =========================

class BarangKeluarForm(forms.Form):


    barang = forms.ModelChoiceField(

        queryset=Barang.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    lokasi = forms.ModelChoiceField(

        queryset=Lokasi.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    jumlah = forms.IntegerField(

        min_value=1,

        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jumlah barang keluar'
            }
        )

    )



    keterangan = forms.CharField(

        required=False,


        widget=forms.Textarea(

            attrs={
                'class':'form-control',
                'rows':3,
                'placeholder':'Keterangan pengeluaran barang'
            }

        )

    )

    # =========================
# TRANSAKSI TRANSFER BARANG
# =========================

class TransferForm(forms.Form):


    barang = forms.ModelChoiceField(

        queryset=Barang.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    lokasi_asal = forms.ModelChoiceField(

        queryset=Lokasi.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    lokasi_tujuan = forms.ModelChoiceField(

        queryset=Lokasi.objects.all(),

        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )

    )



    jumlah = forms.IntegerField(

        min_value=1,

        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jumlah barang transfer'
            }
        )

    )



    keterangan = forms.CharField(

        required=False,


        widget=forms.Textarea(

            attrs={
                'class':'form-control',
                'rows':3,
                'placeholder':'Keterangan transfer barang'
            }

        )

    )

# =========================
# USER FORM
# =========================


class UserCreateForm(forms.ModelForm):


    password = forms.CharField(

        widget=forms.PasswordInput(

            attrs={

                'class':'form-control',

                'placeholder':'Password'

            }

        )

    )


    class Meta:

        model = User


        fields = [

            'username',

            'email',

            'first_name',

            'last_name',

            'password'

        ]


        widgets = {


            'username': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Username'

                }

            ),


            'email': forms.EmailInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Email'

                }

            ),


            'first_name': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Nama depan'

                }

            ),


            'last_name': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Nama belakang'

                }

            ),

        }



    def save(self, commit=True):

        user = super().save(commit=False)


        user.set_password(
            self.cleaned_data['password']
        )


        if commit:

            user.save()


        return user
    

# =========================
# USER EDIT FORM
# =========================


class UserEditForm(forms.ModelForm):


    password = forms.CharField(

        required=False,

        widget=forms.PasswordInput(

            attrs={

                'class':'form-control',

                'placeholder':'Password baru'

            }

        )

    )


    class Meta:

        model = User

        fields = [

            'username',

            'email',

            'first_name',

            'last_name',

            'password'

        ]


        widgets = {


            'username': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Username'

                }

            ),


            'email': forms.EmailInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Email'

                }

            ),


            'first_name': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Nama depan'

                }

            ),


            'last_name': forms.TextInput(

                attrs={

                    'class':'form-control',

                    'placeholder':'Nama belakang'

                }

            ),

        }



    def save(self, commit=True):

        user = super().save(commit=False)


        password = self.cleaned_data.get('password')


        if password:

            user.set_password(password)


        if commit:

            user.save()


        return user