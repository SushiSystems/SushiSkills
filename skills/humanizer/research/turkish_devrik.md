# Devrik cümle: araştırma notu

Tarama 2026-09-05. `../generic_turkish.md` içindeki "Devrik cümle" bölümü bu nota dayanır. Kural
bir cümledir: teknik ve iş metninde yüklem sonda durur. Bu not kuralın gerekçesini, devrik
cümlenin nasıl tanındığını ve devrik kurmadan vurgu ile ritmin nasıl sağlandığını toplar.

## 1. Tanım ve sınır

Okul dil bilgisi cümleyi yüklemin yerine göre üçe ayırır: kurallı (düz), devrik, eksiltili.
Kurallı cümlede yüklem sondadır; devrik cümlede başta ya da ortadadır; eksiltili cümlede
yüklem yoktur. Ölçüt cümlenin anlamı değil, yüklemin yeridir (Hürriyet Eğitim; Türk Edebiyatı;
Vikipedi). Türkçenin düz dizilişi özne, zarf tümleci, dolaylı tümleç, nesne, yüklem sırasıdır
(Türk Edebiyatı, "Cümlenin ögeleri").

İki sınır önemli:

- İsim cümlesi devrik değildir. "Ekip elli kişi." cümlesinde yüklem "elli kişi"dir ve sondadır.
  Ek fiilin düşmesi devriklik yapmaz.
- Eksiltili cümle devrik değildir. "Darboğaz aritmetik değil, bariyerler." cümlesinde ikinci
  parça "bariyerler(dir)" yüklemidir, sondadır.

Vikipedi'nin örnekleri devrikliğin iki ana biçimini gösterir: yüklem başta ("Çıkar ağzından şu
baklayı artık") ve nesne cümlesi sonda ("Babam söyledi bugün geleceğinizi").

## 2. Dizilişin görevi: neden yüklem sonda

Erguvanlı (1984), *The Function of Word Order in Turkish Grammar*, Türkçe cümlede her konuma
bir söylem görevi verir:

| Konum | Görev |
| --- | --- |
| Cümle başı | Konu: cümlenin neyle ilgili olduğu, önceki bağlama bağ |
| Yüklemin hemen önü | Odak: yeni ya da karşıt bilgi |
| Yüklemin sonrası | Artalan: zaten bilinen, "gerekmese de anlamaya yardım eden" bilgi |

Sonraki çalışmalar (İşsever; Ankara Üniversitesi dilbilim tezi, üç parçalı model: konu, odak,
eklenti) aynı bölüşümü korur. Yüklemden sonraya atılan öge, dinleyene "bunu zaten biliyorsun"
der. Konuşmada bunun iki işi var: heyecan ve onarım (Tekin & Öztürk 2022, RumeliDE): söyleyip
eksik kalan ögeyi arkadan ekleme.

Teknik belge için sonuç açık. Belgedeki her öge ya konudur ya odak; "zaten biliyorsun" diye
arkaya atılacak bilgi yoktur, sonradan akla gelen öge de yoktur. Devrik cümle bir olguyu
artalana iter; belge olguyu öne koymak için yazılır.

## 3. Kurumsal kural

- Teknik Dergi (TMMOB İnşaat Mühendisleri Odası) yazım kuralı 4: "Metin yalın bir dil ve
  anlatımla yazılmalı, Türkçe yazım kurallarına uygun olmalı, üçüncü tekil şahıs ve edilgen
  fiiller kullanılmalı, devrik cümleler içermemelidir." Devrikliği adıyla yasaklayan tek
  kurumsal kural budur; edilgen tercihi bu kılavuzun kuralına ters, o kısmı almıyoruz.
- Resmî Yazışmalar Yönetmeliği ve üniversite yazışma kılavuzları devrikliği adıyla anmaz;
  "kısa, açık, anlaşılır anlatım" ister ve örneklerinin tümü kurallıdır.
- Bilimsel yazı kılavuzları (Çokbilgi) devrik cümleyi şiire yakıştırır, akademik üslubu
  konuşma dilinden ayırır.

## 4. Ataç tartışması ve nesirdeki yeri

Nurullah Ataç devrik cümleyi konuşma dilinin sıcaklığını yazıya taşımak için bilerek kullandı
ve savundu: Türkçenin hâl ekleri dizilişi serbest bırakır, halk ağzı ve şiir devrik kurar,
"Var mı inecek?" Türkçedir (BirGün; Edebiyat Pınarım; TDK Türk Dili Ataç özel sayısı). Tartışma
ikiye ayrılır: devriklik anlatım bozukluğu mudur? Değildir; "Dün akşam aramış beni" bozuk
değil. Ama "Yedim pilav akşam, içtim ayran" gibi yığılmış devriklik bozukluk sayılır (Edebiyat
Pınarım). Toplum araştırması (Researchgate, "Toplumun Devrik Cümle Hakkındaki Düşüncesi ve
Nesirde Devrik Cümlenin Yeri") devrikliğin konuşma ve şiirde yaygın, nesirde tartışmalı
olduğunu ölçer; tam metne erişilemedi, özetiyle alındı.

Bu kılavuz için çıkarım: Ataç'ın devrikliği deneme ve söyleşinin aracıdır. README, tasarım
notu, commit, PR ve sohbet yanıtı o türden değildir.

## 5. Yapay zekâ Türkçesinde devriklik

Türkçe LLM metninin en bilinen imzası -mektedir kafiyesidir. Bunu kırmak için yayılan
kılavuzlar (insanca, GitHub) devrik cümle serpmeyi öğütler. Uygulamada bu ikinci bir imza
üretir:

- Her paragrafta bir devrik cümle, düzenli aralıkla.
- Hep aynı biçim: nesne ya da zarf tümleci yüklemin arkasına atılmış.
- Söylem gerekçesi yok: arkaya atılan öge bilinen değil, çoğu zaman cümlenin asıl bilgisi.
- Çevre kurallı ve resmî; devrik cümle o kayıtta yabancı durur.

Kafiyeyi kırmanın doğru yolu ek çeşitliliğidir: -ir, -iyor, -di, isim cümlesi, eksiltili
cümle, iki noktayla açılan liste. Diziliş değişmez.

## 6. Tanıma yöntemi

Cümlenin son sözcüğüne bak.

1. Çekimli fiilse (-dı, -ır, -iyor, -miş, -ecek, -meli, -sın, -se) kurallı.
2. Ek fiilli ad ya da sıfatsa (-dır, -dı, -miş; var, yok, değil) kurallı.
3. Son sözcük bunlardan değilse ve yüklem cümlenin içinde bir yerdeyse devrik.
4. Yüklem hiç yoksa eksiltili; devrik değil.

Sık biçimler ve onarımı:

| Biçim | Devrik | Kurallı |
| --- | --- | --- |
| Nesne sonda | Sahne yöneticisi günceller kamera matrisini. | Sahne yöneticisi kamera matrisini günceller. |
| Zarf tümleci sonda | Tampon sıfırlanır her karede. | Tampon her karede sıfırlanır. |
| Özne sonda | Dört ms arttı kare süresi. | Kare süresi 4 ms arttı. |
| Yüklem başta | Yoktu böyle bir gereksinim. | Böyle bir gereksinim yoktu. |
| Açıklama sonda | Testler geçti, hepsi. | Testlerin hepsi geçti. |
| "ki" yan cümlesi sonda | Gördük ki önbellek işe yaramıyor. | Önbelleğin işe yaramadığını gördük. |
| Ünlem başta | Kalktı bütün ekip ayağa. | Bütün ekip ayağa kalktı. |

"ki" biçimi ayrıca `generic_turkish.md` "ki bağlacı" maddesinde: nesne cümlesi -dığını ile kurulur.

## 7. Devrik kurmadan vurgu ve ritim

- **Vurgu.** Odak yeri yüklemin hemen önüdür. Vurgulanacak ögeyi oraya taşı; gerisi düz kalır.
  "Bu hatayı derleyici yakaladı" (fail vurgulu), "Derleyici bu hatayı yakaladı" (nesne vurgulu),
  "Derleyici bu hatayı dün yakaladı" (zaman vurgulu). Üçü de kurallı.
- **Bilinen öge.** Arkaya atma, sil. Türkçe özne ve nesne düşürür; bağlamdan belli olan öge
  yazılmaz.
- **Ritim.** Kısa cümle, isim cümlesi, iki nokta, üç sözcüklük yargı. Kılavuz kaydında soru.
- **Tek sözcük vurgusu.** İki nokta: "Tek bir şey istedi: sessizlik." Ya da vurguyu yüklem
  önüne alan kurallı cümle: "Tek istediği sessizlikti."

## 8. İstisna

- Konuşma çizgisiyle ya da tırnakla verilen alıntı: kaynağın dizilişi korunur.
- Kalıp sözler yalnız diyalogda: hoş geldin, var mı inecek, gel bakalım.
- "değil mi" soru kuyruğu.
- Başlık ve madde imi başı: yargı taşımaz, yüklem yoktur.

Bunların dışında bu kılavuzun kapsadığı hiçbir kayıt devrik cümle taşımaz.

## Kaynaklar

1. Erguvanlı, E. E. (1984). *The Function of Word Order in Turkish Grammar*. University of
   California Press. Konu / odak / artalan bölüşümü.
2. İşsever, S. Türkçede bilgi yapısı ve yüklem sonrası alan; Ankara Üniversitesi dilbilim tezi
   (dspace.ankara.edu.tr), üç parçalı model.
3. Tekin, A. & Öztürk, ? (2022). "Türkçenin yabancı/ikinci dil olarak öğretiminde devrik cümle
   yapısı", RumeliDE. dergipark.org.tr/tr/pub/rumelide/article/1104087. Heyecan ve onarım işlevi;
   ikinci yazarın adı özette yok.
4. Teknik Dergi, Yazım Kuralları, madde 4. dergipark.org.tr/tr/pub/tekderg/writing-rules.
5. "Toplumun Devrik Cümle Hakkındaki Düşüncesi ve Nesirde Devrik Cümlenin Yeri", Researchgate
   322161545. Tam metin 403 verdi; özetiyle alındı.
6. TDK, *Türk Dili* Ataç özel sayısı (2014-09-19 PDF). Metin katmanı çıkarılamadı; Ataç'ın
   görüşü BirGün ve Edebiyat Pınarım üzerinden doğrulandı.
7. "Devrik cümle anlatım bozukluğu mudur?", edebiyatpinarim.blogspot.com (2018).
8. Vikipedi, "Devrik cümle". Tanım ve örnekler.
9. Türk Edebiyatı, "Ögelerin dizilişine göre cümle türleri" ve "Cümlenin ögeleri".
   turkedebiyati.org. Düz diziliş ve vurgu kuralı.
10. Hürriyet Eğitim, "Devrik cümle nedir" ve "Yüklemin yerine göre cümleler". Okul tanımı.
11. insanca, github.com/tahiryildiz/insanca. Kafiye kırmak için devrik öğüdü; bu kılavuz
    tersini kurar.

## Açık noktalar

- Devrik cümle sıklığını Türkçe teknik belge derlemi üzerinde ölçen çalışma bulunamadı; "LLM
  her paragrafa bir devrik serper" gözlemi editörlük deneyimine dayanır, sayıya değil.
- Resmî Yazışma Kılavuzu (tccb.gov.tr) sertifika hatası verdi; devrikliği anıp anmadığı
  doğrulanamadı, yönetmelik metninden anmadığı biliniyor.
