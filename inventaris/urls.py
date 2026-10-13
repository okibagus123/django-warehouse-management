from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    # =========================
    # LOGIN
    # =========================

    path(
        'login/',
        views.login_view,
        name='login'
    ),



    # =========================
    # DASHBOARD
    # =========================

    path(
        '',
        views.dasbor_view,
        name='dasbor'
    ),



    # =========================
    # USER & AUTH
    # =========================

    path(
        'user/profil/',
        views.profil_view,
        name='profil'
    ),


    path(
        'user/',
        views.user_list_view,
        name='user_list'
    ),


    path(
        'user/tambah/',
        views.tambah_user_view,
        name='tambah_user'
    ),


    path(
        'user/edit/<int:id>/',
        views.edit_user_view,
        name='edit_user'
    ),


    path(
        'logout/',
        views.logout_akun,
        name='logout'
    ),


    # ========================================================
    # MASTER DATA
    # ========================================================

    path(
        'master/',
        views.master_data_view,
        name='master'
    ),


    # ========================================================
    # MASTER BARANG
    # ========================================================

    path(
        'master/barang/',
        views.master_barang_view,
        name='master_barang'
    ),

    path(
        'master/barang/tambah/',
        views.tambah_barang_view,
        name='tambah_barang'
    ),

    path(
        'master/barang/edit/<int:id>/',
        views.edit_barang_view,
        name='edit_barang'
    ),

    path(
        'master/barang/hapus/<int:id>/',
        views.hapus_barang_view,
        name='hapus_barang'
    ),

    path(
        'master/barang/hapus-semua/',
        views.hapus_semua_barang_view,
        name='hapus_semua_barang'
    ),


    # ========================================================
    # MASTER KATEGORI
    # ========================================================

    path(
        'master/kategori/',
        views.master_kategori_view,
        name='master_kategori'
    ),

    path(
        'master/kategori/tambah/',
        views.tambah_kategori_view,
        name='tambah_kategori'
    ),

    path(
        'master/kategori/edit/<int:id>/',
        views.edit_kategori_view,
        name='edit_kategori'
    ),

    path(
        'master/kategori/hapus/<int:id>/',
        views.hapus_kategori_view,
        name='hapus_kategori'
    ),

    path(
        'master/kategori/hapus-semua/',
        views.hapus_semua_kategori_view,
        name='hapus_semua_kategori'
    ),


    # ========================================================
    # MASTER SUPPLIER
    # ========================================================

    path(
        'master/supplier/',
        views.master_supplier_view,
        name='master_supplier'
    ),

    path(
        'master/supplier/tambah/',
        views.tambah_supplier_view,
        name='tambah_supplier'
    ),

    path(
        'master/supplier/edit/<int:id>/',
        views.edit_supplier_view,
        name='edit_supplier'
    ),

    path(
        'master/supplier/hapus/<int:id>/',
        views.hapus_supplier_view,
        name='hapus_supplier'
    ),

    path(
        'master/supplier/hapus-semua/',
        views.hapus_semua_supplier_view,
        name='hapus_semua_supplier'
    ),


    # ========================================================
    # MASTER LOKASI
    # ========================================================

    path(
        'master/lokasi/',
        views.master_lokasi_view,
        name='master_lokasi'
    ),

    path(
        'master/lokasi/tambah/',
        views.tambah_lokasi_view,
        name='tambah_lokasi'
    ),

    path(
        'master/lokasi/edit/<int:id>/',
        views.edit_lokasi_view,
        name='edit_lokasi'
    ),

    path(
        'master/lokasi/hapus/<int:id>/',
        views.hapus_lokasi_view,
        name='hapus_lokasi'
    ),

    path(
        'master/lokasi/hapus-semua/',
        views.hapus_semua_lokasi_view,
        name='hapus_semua_lokasi'
    ),
path('barang/detail/<int:pk>/', views.detail_barang_view, name='detail_barang'),
path('lokasi/detail/<int:pk>/', views.detail_lokasi_view, name='detail_lokasi'),

    # ========================================================
    # IMPORT EXCEL MASTER
    # ========================================================

    path(
        'master/import/<str:jenis>/',
        views.import_excel_view,
        name='import_excel'
    ),


    # ========================================================
    # TRANSAKSI
    # ========================================================

    path(
    'transaksi/',
    views.transaksi_view,
    name='transaksi'
),

path(
    'transaksi/barang-masuk/',
    views.barang_masuk_view,
    name='barang_masuk'
),

path(
    'transaksi/barang-keluar/',
    views.barang_keluar_view,
    name='barang_keluar'
),

path(
    'transaksi/transfer/',
    views.transfer_view,
    name='transfer'
),
path('transaksi/adjustment/', views.adjustment_stok_view, name='adjustment_stok'),

# =========================
# KONTROL STOK
# =========================

path(
    'transaksi/kontrol-stok/',
    views.kontrol_stok_view,
    name='kontrol_stok'
),



# =========================
# VALIDASI OPERASIONAL
# =========================

path(
    'transaksi/validasi-operasional/',
    views.validasi_operasional_view,
    name='validasi_operasional'
),

    # ========================================================
    # WMS
    # ========================================================

    path(
        'wms/',
        views.wms_monitor_view,
        name='wms_monitor'
    ),

    path(
        'wms/stok-barang/',
        views.stok_barang_view,
        name='stok_barang'
    ),

    path(
        'wms/lokasi-stok/',
        views.lokasi_stok_view,
        name='lokasi_stok'
    ),


path('laporan/', views.laporan_view, name='laporan'),
path('laporan/export/inventory/', views.export_inventory_csv, name='export_inventory'),
path('laporan/export/transaksi/', views.export_transaksi_csv, name='export_transaksi'),

    # ========================================================
    # PROFIL
    # ========================================================

    path(
        'profil/',
        views.profil_view,
        name='profil'
    ),
    
# =========================
# USER
# =========================


path(
    'user/',
    views.user_list_view,
    name='user_list'
),


path(
'user/tambah/',
views.tambah_user_view,
name='tambah_user'
),


path(
    'user/edit/<int:id>/',
    views.edit_user_view,
    name='edit_user'
),


path(
    'user/hapus/<int:id>/',
    views.hapus_user_view,
    name='hapus_user'
),


path(
    'user/profil/',
    views.profil_view,
    name='profil'
),


    # ========================================================
    # LOGOUT
    # ========================================================

    path(
        'logout/',
        views.logout_akun,
        name='logout'
    ),

]