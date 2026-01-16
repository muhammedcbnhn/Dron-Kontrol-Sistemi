# Dron-Kontrol-Sistemi


Bu proje, Python programlama dili ve Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak geliştirilmiş bir drone yönetim simülasyonudur. Proje, temel bir drone sınıfı ve bu sınıftan türetilmiş özelleşmiş alt sınıfları kullanarak kalıtım (inheritance) ve method ezme (overriding) kavramlarını uygular.

Proje Amacı
Uygulama, farklı görev tanımlarına sahip drone'ların (Standart, Kargo ve Güvenlik) pil yönetimini, uçuş durumlarını ve operasyonel davranışlarını simüle etmeyi amaçlar.

Mimari Yapı
Proje üç ana sınıf bileşeninden oluşmaktadır:

1. Drone (Base Class)
Sistemin temel sınıfıdır. Tüm drone tipleri için ortak olan özellikleri ve metotları barındırır.

Özellikler: Kimlik (ID), Model, Pil Seviyesi, Anlık Durum (Beklemede/Uçuşta).

Fonksiyonlar:

UcusYap(mesafe): Mesafeye bağlı olarak pil tüketimini hesaplar ve durum kontrolü yapar.

SarjEt(): Drone pilini tam kapasiteye getirir.

__str__(): Nesne çağrıldığında temel bilgileri metin olarak döndürür.

2. KargoDron (Subclass)
Yük taşımacılığı için Drone sınıfından türetilmiştir.

Ek Özellik: Yük Kapasitesi.

Override (Ezme): UcusYap metodu, kargo yükü sebebiyle standart tüketime göre enerji sarfiyatını değiştirecek şekilde yeniden düzenlenmiştir.

3. GuvenlikDronu (Subclass)
Gözetleme faaliyetleri için Drone sınıfından türetilmiştir.

Ek Özellik: Gece Görüşü (Boolean).

Override (Ezme): UcusYap metodu, güvenlik taraması ve gece görüşü durumuna özgü bildirimler sağlamak üzere özelleştirilmiştir.

Gereksinimler
Python 3.x

Kullanım
Proje dosyası çalıştırıldığında, tanımlanan sınıflardan nesneler oluşturulur ve aşağıdaki senaryolar test edilir:

Standart bir drone uçuşu ve şarj işlemi.

Yük taşıyan bir kargo drone'unun uçuş simülasyonu.

Güvenlik drone'unun operasyonel süreçleri.
