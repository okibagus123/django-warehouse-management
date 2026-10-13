from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# =========================
# USER PROFILE
# =========================

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )


    foto = models.ImageField(
        upload_to='profile/',
        default='profile/default-user.png',
        blank=True,
        null=True
    )


    ROLE_CHOICES = [

        ('Administrator', 'Administrator'),

        ('Staff Gudang', 'Staff Gudang'),

        ('Operator', 'Operator'),

        ('Viewer', 'Viewer'),

    ]


    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='Administrator'
    )


    no_hp = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


    alamat = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return self.user.username



# =========================
# CREATE PROFILE AUTOMATIC
# =========================


@receiver(post_save, sender=User)

def create_user_profile(sender, instance, created, **kwargs):

    if created:

        UserProfile.objects.create(
            user=instance
        )



@receiver(post_save, sender=User)

def save_user_profile(sender, instance, **kwargs):

    instance.userprofile.save()
    
    
class Kategori(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama


class Supplier(models.Model):
    nama = models.CharField(max_length=100)
    kontak = models.CharField(max_length=50, blank=True)
    alamat = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama


class Lokasi(models.Model):
    kode_lokasi = models.CharField(max_length=50, unique=True)
    nama_lokasi = models.CharField(max_length=100)

    def __str__(self):
        return self.kode_lokasi


class Barang(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    nama = models.CharField(max_length=100)

    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.SET_NULL,
        null=True
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True
    )

    satuan = models.CharField(
        max_length=20,
        default="PCS"
    )

    minimum_stock = models.IntegerField(
        default=5
    )

    harga_satuan = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    def __str__(self):
        return f"{self.sku} - {self.nama}"


class Inventory(models.Model):

    barang = models.ForeignKey(
        Barang,
        on_delete=models.CASCADE
    )

    lokasi = models.ForeignKey(
        Lokasi,
        on_delete=models.CASCADE
    )

    jumlah = models.IntegerField(
        default=0
    )


    def __str__(self):
        return f"{self.barang.nama} - {self.jumlah}"

# =========================
# STOCK MOVEMENT
# =========================

class StockMovement(models.Model):


    TIPE = (

        ("MASUK", "Barang Masuk"),

        ("KELUAR", "Barang Keluar"),

        ("TRANSFER", "Transfer"),

        ("ADJUSTMENT", "Adjustment"),

    )



    barang = models.ForeignKey(

        Barang,

        on_delete=models.CASCADE

    )



    tipe = models.CharField(

        max_length=20,

        choices=TIPE

    )



    jumlah = models.IntegerField()



    lokasi_asal = models.ForeignKey(

        Lokasi,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name='stock_keluar'

    )



    lokasi_tujuan = models.ForeignKey(

        Lokasi,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name='stock_masuk'

    )



    tanggal = models.DateTimeField(

        auto_now_add=True

    )



    user = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True

    )



    keterangan = models.TextField(

        blank=True,

        null=True

    )



    def __str__(self):

        return f"{self.barang.nama} - {self.tipe}"