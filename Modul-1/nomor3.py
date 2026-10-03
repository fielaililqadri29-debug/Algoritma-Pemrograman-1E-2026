jarak_satu_arah = 100
total_jarak_pulang_pergi = 200
konsumsi_bbm = 40
sisa_bbm = 1.5
harga_per_liter = 10000

total_jarak = jarak_satu_arah + total_jarak_pulang_pergi
total_kebutuhan_bbm = total_jarak_pulang_pergi / konsumsi_bbm


print("total_pulang_pergi=", jarak_satu_arah + total_jarak_pulang_pergi)
print("total_kebutuhan_bbm=", total_jarak_pulang_pergi / konsumsi_bbm)

total_beli_bbm = total_kebutuhan_bbm - sisa_bbm
print("total_beli_bbm=",total_kebutuhan_bbm - sisa_bbm)

total_biaya_bbm = total_beli_bbm * harga_per_liter
print("total_biaya_bbm =",total_beli_bbm * harga_per_liter)

print("total_jarak:", total_jarak, "km")
print("total_bbm:", total_kebutuhan_bbm, "liter")
print("total_beli_bbm:", total_beli_bbm, "liter")
print("total_biaya_bbm:", "Rp", total_biaya_bbm) 