# Türkçe

Kurallar TDK yazım kılavuzu ve noktalama sayfalarından, Resmî Yazışmalar Yönetmeliği'nden,
Alpay / Aksoy / Hepçilingirler / Özdemir İnce çizgisindeki dil eleştirisinden, Türkçe okuma
deneylerinden (Aydın & Cedden, Özge, Mutlu vd.), Bayat'ın paragraf ölçümünden ve Barış Özkul'un
yapay zekâ Türkçesi üzerine editörlük gözlemlerinden çıkarıldı. Kaynaklar
`research/turkish_sources.md` dosyasında.

İngilizce tik listeleri Türkçeye doğrudan çevrilmez. Türkçe LLM metninin imzası üç yerde
toplanır: ek morfolojisi (-mektedir tekdüzeliği), bürokratik bağlaç zinciri, İngilizce retorik
kalıplarının çevirisi. Aşağıdaki kurallar bu üçünü hedefler.

Üç kural gerisini kapsar:

1. **Niteleme yerine ölçü ver.** "Oldukça hızlı" bir görüş; "3,2 kat hızlı" bir bilgi.
2. **Faili yüzeye çıkar.** "Kamera matrisi sahne yöneticisi tarafından güncellenmektedir"
   değil, "Sahne yöneticisi kamera matrisini her karede günceller."
3. **Söyleyince bitir.** "Sonuç olarak" ile açılan tekrar paragrafı yok, "umarım faydalı
   olmuştur" yok.

## Cümle kurgusu

- **Uzunluk.** Genel Türkçenin ortalaması 9–10 sözcük (Ateşman); akademik Türkçe 21'e çıkıyor ve
  "çok zor" bandına düşüyor. Teknik metinde 20 civarı gerçekçi; 30'u geçen cümle bölünür. Özne
  ile yüklem arasına 15'ten fazla sözcük sokma; ağır öbeği yükleme yakın diz.
- **Ortaç ve ulaç zinciri.** Okuma deneyleri -dık'lı nesne ortaçlarının -an'lı özne ortaçlarından
  ağır olduğunu, aynı hâl ekini taşıyan iç içe öznelerin en zor okunan yapı olduğunu ölçtü.
  Uygulama kuralı: bir baş addan önce en fazla bir ortaç öbeği; art arda üç ulaç (-arak / -ıp /
  -ken) yok, çünkü ulaç öznesini ana yüklemden ödünç alır ve zincir uzadıkça özne kaybolur.
- **Yüklem sonda.** Devrik cümle kurma; ayrıntısı aşağıda kendi bölümünde.
- **"ki" bağlacı.** Farsça kökenli; okumayı yavaşlatmıyor ama biriktikçe çeviri kokuyor.
  Kalıplaşmışlar (demek ki, ne var ki, kaldı ki, iyi ki) ve derece bildiren "öyle … ki" kalır.
  "Belirtmek gerekir ki / açıktır ki / unutulmamalıdır ki" ile açılan cümle ve -dığını ile
  kurulabilecek nesne cümlesinde "ki" gider: "anlamıştı ki doğru değildi" → "doğru olmadığını
  anlamıştı".
- **"ve" ile "ile".** "ile" cümle bağlamaz, yalnız sözcük ve öbek bağlar. Aynı öznenin iki
  eylemini -ıp / -arak bağlar, "ve" değil; listede "ve" yalnız son ögeden önce durur. "ve/veya"
  belirsizliği çözmez; "veya" ya da "en az biri".
- **"olup" ile iki yargıyı tek cümleye sıkıştırma.** Nokta koy.
- **Nedensellik.** Neden yan cümledeyse `-dığı için` / `-dığından`; ad öbeğiyse `nedeniyle`
  (yansız), `sayesinde` (olumlu), `yüzünden` (olumsuz); amaçsa `için`. "Bu nedenden dolayı" ve
  "-dığından dolayı" ikili yineleme; "bu nedenle" yeter. "Yeni önbellek sayesinde kare süresi
  4 ms arttı" yanlış: artış olumsuzsa "yüzünden".

## Devrik cümle

Araştırma notu ve kaynaklar `research/turkish_devrik.md` dosyasında. Kural: belgede, commit'te,
PR'da, tasarım notunda, sohbet yanıtında devrik cümle yok. Yüklem sonda.

- **Tanım.** Türkçenin düz dizilişi özne, zarf tümleci, dolaylı tümleç, nesne, yüklem. Yüklemi
  sonda olan cümle kurallı; yüklemi başta ya da ortada olan cümle devrik. Ölçüt anlam değil,
  yüklemin yeri. Yüklemsiz cümle (eksiltili) devrik değildir: "Ekip elli kişi." yüklemi "elli
  kişi" olan isim cümlesidir ve kurallıdır.
- **Neden yok.** Erguvanlı'nın dizilişe verdiği görevler: cümle başı konu, yüklemin hemen önü
  odak, yüklemin sonrası artalan. Yüklemden sonra gelen öge "zaten biliniyor, sonradan aklıma
  geldi" demektir. Teknik belgede sonradan akla gelen bilgi olmaz; her öge ya odaktır ya konu.
  Konuşmada devriklik heyecan ve onarım işidir (Tekin & Öztürk 2022): söyleyip eksiği ekleme.
  Yazıda eksik yoksa onarım da yok. Teknik Dergi yazım kuralı 4 açıkça yasaklar: "devrik cümleler
  içermemelidir". Ataç'ın savunduğu devriklik deneme ve söyleşi içindir; nesirde bile yaygın
  kabul görmedi, belgede hiç.
- **Yapay zekâ Türkçesindeki yeri.** Model -mektedir kafiyesini kırmak için devrik cümle serper;
  "insanca" türü kılavuzlar bunu öğütler. Sonuç ölçülebilir bir imza: her paragrafta bir tane,
  hep aynı biçimde (nesne ya da tümleç yükleme atılmış), gerekçesi yok. Kafiye ek çeşidiyle
  kırılır, dizilişle değil.
- **Tanıma testi.** Noktadan önceki sözcük yüklem mi? Çekimli fiil (-dı, -ır, -iyor, -miş,
  -ecek, -meli, -sın), ek fiilli ad ya da sıfat (-dır, -dı, -miş, var, yok, değil) ise kurallı.
  Yüklemden sonra aynı cümleye ait bir öge duruyorsa devrik. Sık biçimler:
  - Nesne sonda: "Sahne yöneticisi günceller kamera matrisini." → "Sahne yöneticisi kamera
    matrisini günceller."
  - Tümleç sonda: "Tampon sıfırlanır her karede." → "Tampon her karede sıfırlanır."
  - Özne sonda: "Dört ms arttı kare süresi." → "Kare süresi 4 ms arttı."
  - Yüklem başta: "Yoktu böyle bir gereksinim." → "Böyle bir gereksinim yoktu."
  - Yüklem ortada, açıklama sonda: "Testler geçti, hepsi." → "Testlerin hepsi geçti."
  - "ki" ile sonraya atılmış yan cümle: "Gördük ki önbellek işe yaramıyor." → "Önbelleğin işe
    yaramadığını gördük."
- **Vurgu nasıl verilir.** Odak yeri yüklemin hemen önüdür; vurgulanacak ögeyi oraya taşı,
  gerisi kurallı kalır. "Bu hatayı derleyici yakaladı" (derleyici vurgulu), "Derleyici bu hatayı
  yakaladı" (hata vurgulu). Bilinen ögeyi arkaya atma; Türkçe özne ve nesne düşürür, sil:
  "Derleyici uyarı verdi. Sonra da hata." değil "Derleyici uyarı verdi, sonra hata."
- **Ritim nasıl kırılır.** Kısa cümle, isim cümlesi, iki nokta, soru (yalnız kılavuzda), üç
  sözcüklük yargı. "Darboğaz aritmetik değil, bariyerler." kurallıdır: yüklem "bariyerler".
- **Devrik sayılmayan ya da izinli olan.** Alıntı ve konuşma çizgisiyle verilen söz; kalıp sözler
  (hoş geldin, var mı inecek) yalnız diyalogda; "değil mi" sorusu; başlık ve madde imi (yargı
  yok). Bunların dışında istisna yok.

> Önce: Bu geçiş çizer gölge haritasını, her karede. Sonuç iyi, çoğu sahnede.
> Sonra: Bu geçiş gölge haritasını her karede çizer. Çoğu sahnede sonuç iyi.

## Çatı ve kip

- **Edilgen, faili gizler.** Teknik belgede bu "bunu hangi bileşen yapıyor" sorusunu cevapsız
  bırakır. Tek meşru yeri: fail gerçekten ilgisiz ya da bağlamdan belli ("Tampon her karede
  sıfırlanır"). Fail bir modülse etken yaz. "X tarafından Y-ildi" İngilizce "by" izidir; fail
  zaten söyleniyorsa edilgenin kazancı yok.
- **-ir varsayılan, -iyor gözlem, -mektedir neredeyse hiç.** `-mAktA` mastar + bulunma hâlidir;
  eylemi bir hâle çevirir, hareketi soğutur, faili silikleştirir. "Sürerlik bildirir" gerekçesi
  ölçülemiyor ("üç yıldır çalışıyorum" ile "çalışmaktayım" arasında fark yok); geriye yalnız
  bürokratik ton kalıyor. Kural, sözleşme, değişmez davranış → -ir. Ölçüm ve gözlem → -iyor.
- **-mektedir tekdüzeliği Türkçeye özgü en güçlü tik.** Her cümle aynı ekle bitince kafiye oluşur.
  Kırmanın yolu ek çeşitliliği: -ir, -iyor, -di, isim cümlesi (yüklem ad ya da sıfat), eksiltili
  cümle, iki noktayla açılan liste. Devrik cümleyle kırma; kafiye gider, tik gelir.

> Önce: Şirket 2020 yılında kurulmuştur. Merkezi İstanbul'da bulunmaktadır. Elli kişilik bir
> ekiple hizmet vermektedir.
> Sonra: Şirket 2020'de kuruldu, merkezi İstanbul'da. Ekip elli kişi.

## Dolgu fiiller ve ilgeçler

- **"gerçekleştirmek"** tasarı, proje, ideal için; ölçüm, tahsis, test "yapılır" ya da doğrudan
  fiil: ölçüm gerçekleştirmek → ölçmek.
- **"sağlamak"** yalnız olumlu sonuç için. Hata, gecikme, kayıp cümlesinde geçiyorsa kesin
  yanlış. "senkronizasyon sağlamak" → "eşitlemek".
- **Koşaç kaçışı.** Model düz "X, Y'dir" diyemiyor; yerine "işlevi görmektedir", "konumundadır",
  "olarak öne çıkmaktadır", "niteliği taşımaktadır", "olma özelliğine sahiptir", "teşkil
  etmektedir" koyuyor. İngilizce "is → serves as" kaymasının karşılığı. "-dır" ya da "var" yaz.
- **"yer almaktadır / bulunmaktadır / söz konusu olmaktadır / tespit edilmiştir"** → var, içerir,
  olur, gördük, ölçtük.
- **İlgeç enflasyonu.** "kapsamında, çerçevesinde, doğrultusunda, bağlamında, noktasında,
  bazında, nezdinde, itibarıyla, -e yönelik, -e ilişkin, -e dair" bir fiil çağırır, fiil boş
  çıkar, cümle iki kat uzar. Onarım: fiili at, adlaştır. "gelişine ilişkin yaptığı
  değerlendirmede" → "gelişine ilişkin değerlendirmesinde". "Bellek yönetimi noktasında ciddi
  sıkıntılarımız var" → "Bellek yönetiminde üç kaynak sızıntısı var." "adına" neden ilgeci
  değildir; "açısından".
- **"sahip olmak"** "have" çevirisidir. Sıra: tek sıfat > -li/-siz > iyelik + var > sahip olmak
  (yalnız gerçek mülkiyet). "Düşük bellek ayak izine sahiptir" → "Bellek ayak izi düşüktür."
- **Gereksiz "bir".** "a/an" çevirisi. Kalır: gerçekten sayıysa, ilk anılan ve sonra gönderme
  yapılacak varlıksa, atılınca sıfat tamlaması gibi okunup anlam kayıyorsa. "Derleyici bir
  uyarı üretti ve bir hata verdi" → "Derleyici uyarı üretti, sonra hata verdi."
- **"bir şekilde"** İngilizce -ly zarfının dolgusu: "etkin bir şekilde" → "etkin" ya da ölçü.

## Sıfat ve pekiştirici

- Sıfatı sil; cümle bilgi kaybetmiyorsa geri koyma, kaybediyorsa yerine sayı koy. Aynı test
  "oldukça / son derece / büyük ölçüde / önemli ölçüde / ciddi anlamda" için.
- "Oldukça" aslen "yetecek kadar"; "çok" anlamı "quite" çevirisinden. Galatımeşhur yolunda;
  yanlış değil ama teknik metinde kullanma, ölçü ver.
- Şişkin küme: kapsamlı, bütüncül, kritik, kilit, dinamik, yenilikçi, dönüştürücü, benzersiz,
  hayati, vazgeçilmez, sürdürülebilir, kullanıcı dostu, sorunsuz, kusursuz, güçlü, sağlam, etkin,
  esnek. Tek tük geçmeleri normal, kümelenmeleri imza.
- Boş fiil kalıpları: kritik/önemli/kilit rol oynar, büyük önem taşır, hayati önem arz eder,
  vazgeçilmez unsurdur, olanak tanır, imkân verir, mümkün kılar, katkıda bulunur, kolaylaştırır.
- Pekiştirmeli sözler bitişik (apaçık, bembeyaz, sapasağlam); pekiştirme ile derecelendirme (çok
  temiz) ayrı şeyler.

> Önce: Son derece kapsamlı bir test paketi yazdık.
> Sonra: 340 birim testi, dört donanım yapılandırması.

## Söylem yapısı

- **Konu cümlesi.** Türkçe akademik yazımda zayıf gelenek (%22'ye karşı İngilizce bölümde %60).
  Teknik paragraf konu cümlesiyle açılır; sona saklanan genelleme deneme içindir, belge için
  değil. Kabul testi: paragrafların yalnız ilk cümlelerini okuyan biri argümanı çıkarabilmeli.
- **Bağlaç yığını.** "Bu bağlamda, bu doğrultuda, bu çerçevede, bununla birlikte, öte yandan,
  dahası, ek olarak, üstelik, ne var ki, sonuç olarak, özetle, genel olarak, nihayetinde" —
  paragraf başına en çok bir tane. Ölçülebilir test: Türkçe sıklık derlemlerinde "ama" ilk 25'te,
  "bununla birlikte" ve "öte yandan" ilk 50'de yok. Metinde "bununla birlikte" sayısı "ama"
  sayısını geçiyorsa metin insan Türkçesinin istatistiğine aykırı.
- **"Sadece X değil, aynı zamanda Y."** "Not only … but also" makine çevirisi. Türkçenin araçları
  zaten var: üstelik, dahası, hem … hem de, bununla kalmayıp. Ailesi: "yalnızca bir araç
  değildi, bir dönüşümün başlangıcıydı"; "Tek başına yeterli değil. Kültür gerekiyor."; "Ne hız.
  Ne fiyat. Sadece güven." Test: metindeki "değil" sayısı üçü geçiyorsa kalıp iskelete dönüşmüş.
- **Simetrik üçlü.** "hızlı, güvenli ve ölçeklenebilir" makine listesi. İnsan listesi ya taşar
  (dört-beş öğe, bakışımsız) ya örnekleyip kesilir. Yaklaşıklık sayı ikilisiyle: "üç beş
  kelime", "sekiz on kişi"; "yaklaşık 8-10 kişi" değil.
- **-arak/-erek ile sahte derinlik.** "…na katkıda bulunarak", "…ni gözler önüne sererek",
  "…ne ışık tutarak": bilgiye bir şey eklemeyen anlam iliştirmesi. Kes.
- **Metafor tikleri.** Mecazi yolculuk, ekosistem, manzara, dokunuş, DNA'sı, oyun değiştirici,
  ezber bozan, derinlemesine incelemek, dünyasına dalmak, keşfetmek (yazı için), ışık tutmak,
  gözler önüne sermek, altını çizmek, görünür kılmak, alan açmak, bir sonraki seviyeye taşımak,
  günün sonunda, konfor alanı.
- **Sohbet kalıntısı, hiç:** Elbette, Tabii ki, Harika bir soru, İşte …, Umarım faydalı olmuştur,
  Başka bir sorunuz varsa, Hadi başlayalım, İşte bu kadar, Bu yazıda … ele alacağız.
- **Resmî yazışma kalıbı teknik belgeye girmez.** "Arz ederim / rica ederim" kodlanmış hiyerarşi
  beyanıdır (yönetmelik: alta rica, üste arz). README'de, tasarım notunda, commit'te ast-üst
  yoktur. "işbu, mezkûr, söz konusu, ilgili (dolgu), yukarıda arz edilen" de gider.
- **Zamir düşür.** Her cümlede "siz / biz" çeviri kokar: "Siz de kendi yapılandırmanızı siz
  oluşturabilirsiniz" → "Kendi yapılandırmanı oluşturabilirsin."
- **Belirsizlik bir kez, yerinde, ne çözeceğiyle.** "3080 Ti'da ölçülmedi; golden koşusu
  belirler." Her cümleye serpilen "olabilir / düşünülmektedir / değerlendirilmektedir" kaçamak.

## Noktalama ve yazım

- **Uzun çizgi (—) Türkçede yalnız konuşma çizgisidir.** TDK başka işlev tanımaz; Ataç'ta,
  Eyüboğlu'nda, Günyol'da yoktur. Ara söz virgülle, noktalı virgülle, parantezle ya da TDK'nin
  bitişik kısa çizgisiyle kurulur: "Bu karar, hiç beklenmedik biçimde, geri alındı." Tireyi
  kaldırıp "önce tez, sonra keskin hüküm" ritmini noktalı virgülle korumak teli taşır; cümleyi
  yeniden kur. Çizginin yerine ne geleceği, çizginin ne yaptığına bağlıdır:
  - **Ara söz** ("Bu karar — beklenmedik biçimde — geri alındı") → iki virgül.
  - **Sona iliştirilen açıklama** ("…bilmek zorunda değil — bildirmesi yeter") → nokta ile iki
    cümle: "…bilmek zorunda değil. Kendi girdi ve çıktısını bildirmesi yeter."
  - **Örnek ya da liste tanıtımı** ("üç şey gerekir — bellek, zaman, sabır") → iki nokta.
  - **Vurgulu tek sözcük** ("tek bir şey istedi — sessizlik") → iki nokta ya da vurguyu yüklem
    önüne alan kurallı cümle: "Tek bir şey istedi: sessizlik." ya da "Tek istediği sessizlikti."
  Virgül cümleyi ağırlaştırıyorsa sorun çizgide değil, cümlenin iki yargı taşımasındadır; böl.
- **Noktalı virgülden sonra bağlaç yok.** "; bununla birlikte", "; dolayısıyla", "; aynı
  zamanda" hem TDK'ye aykırı hem belirgin tik. Nokta koy.
- **Virgül konmaz:** ve / veya / yahut önünde ve ardında (Oxford virgülü yok); hem…hem, ne…ne'de;
  bağlaç da/de'den sonra; -sa/-se'den sonra; zarf-fiilden sonra. **Konur:** anlam karışıklığını
  önlemek için ("Genç, kadın doktorla görüşmek istedi"); özne olan bu/şu/o'dan sonra ("Bu, kolay
  olmaz").
- **Kesme.** Özel ada gelen çekim eki ayrılır, yapım ve çokluk eki ayrılmaz (Türkçenin, Ahmetler).
  Kurum adına kesme konmaz: "Türk Dil Kurumundan", "TBMM Genel Kurulunda". Kısaltmada konur:
  TDK'nin, ABD'de. Tırnak içindeki söze gelen ek için kesme yok: "Bit Palas"ını.
- **Yabancı terime ek, okunuşa göre:** Google'ı, cache'i, shader'ı, pipeline'a, commit'i,
  build'i, GitHub'a, API'yi. Kısaltmada son harfin okunuşu (TDK'den, TL'nin), kelime gibi
  okunanda kısaltmanın okunuşu (NATO'dan); sert ünsüz yumuşamaz (TÜBİTAK'ın).
- **Sayı ve tarih.** Ondalık virgül, binlik nokta: 15,2 ve 49.750.812. %25 boşluksuz. Sıra
  sayısında ya nokta ya kesme+ek, ikisi değil (8'inci ya da 8., 8.'inci değil). Tarih
  28 Ağustos 2026 ya da 28.08.2026. Cümle rakamla başlamaz.
- **Büyük harf.** Başlıkta title case yok; cümle biçimi, ilk harf büyük. Özel ad içindeki ve /
  ile / ya / veya / ki / da / de / mı küçük. İki noktadan sonra cümle geliyorsa büyük, örnek
  listesi geliyorsa küçük.
- **de/da, ki, mi.** Bağlaç da/de ayrı, uyuma girer, ta/te olmaz. Bitişik "ki" yalnız yedi
  kalıp: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki. Soru eki mi ayrı.
- **Kısaltmalar.** "vb." (vs. değil), "bkz.", tek biçim: ya "örn." ya "ör.", ikisi birden değil.
- **Kalın yazı, madde imi, emoji** düzyazının yerini almaz. Kalın, tanımlanan terim için.

## Terim seçimi

- Yerleşik Türkçe karşılık varsa onu kullan: dosya, dizin, bellek, işlemci, derleme, çalışma
  zamanı, sürüm, hata ayıklama, yığın, sunucu, ağ, veri tabanı, arayüz, önbellek, iş parçacığı,
  gömülü, yazılım, donanım, bilgisayar, bilişim.
- Yerleşmemişse İngilizcesini bırak: commit, branch, pull request, merge, rebase, render, shader,
  pipeline, deploy, mock, refactor. TBD'nin kendi kabulü: "mavidiş" tutmadı, terim zorlamayla
  yerleşmez.
- Terimi ilk geçtiği yerde parantezle tanıt, sonra tek biçimde kullan. Aynı metinde kuram/teori
  karışmaz.
- "buton" değil "düğme"; "tıklatın" değil "tıklayın".

## Kayıt türleri

**Talimat / kılavuz.** Emir kipi "-ın/-in": Tıklayın; Tıklayınız (aşırı resmî) değil; Tıkla
yalnız eğitim ve topluluk içeriğinde. "-ebilirsiniz" dizisi yok, belge okuru talimatla ilerler:
"Bu ayarı değiştirin, derlemeyi yeniden başlatın. Sonuçlar günlük dosyasına yazılır."

**Commit.** Başlık emir kipi, 50 karakterin altında, sonda nokta yok; "Uygulanırsa, bu commit
[başlık]" cümlesi anlamlı olmalı. "Gölge geçişinde derinlik tamponunu yeniden kullan";
"…kullanıldı" ya da "…düzeltmesi yapıldı" değil. Gövde 72 sütun, nedeni anlatır. Proje dili neyse
o, ama tutarlı.

**PR açıklaması.** Ne değişti; neden değişmek zorundaydı; gözden geçiren en çok neye baksın;
nasıl doğrulandı (komut ve çıktı); bilerek yapılmayan ne. Sonuncusu dürüstlüğün en ucuz olduğu yer.

**Tasarım notu / mimari bölüm.** Bildirme kipi, geniş zaman, ağacın şu anki hâli. Tür adı,
dosya, sayı. Tarih changelog'a.

**Sohbet yanıtı.** Önce cevap. Kayıt gevşer, kurallar aynı. Uzunluk soruyla orantılı.

## Önce ve sonra

> Önce: Söz konusu geçiş, gölge haritasının oluşturulması işlemini icra etmekte olup, bu
> sayede render sürecine önemli bir katkı sağlamaktadır.
> Sonra: Bu geçiş gölge haritasını çizer.

> Önce: Ölçümler sırasında çeşitli senaryolar denenmiş, GPU tarafında bariyer sayısının yüksek
> olduğu görülmüş, aritmetik yükün ise beklenenin altında kaldığı anlaşılmıştır. Bu durumda
> darboğazın bariyerlerden kaynaklandığı değerlendirilmektedir.
> Sonra: Darboğaz aritmetik değil, bariyerler. Her kare oranında bariyer sayısı yüksek, aritmetik
> yük beklenenin altında çıktı. Daha hızlı matematik buradan zaman kazandırmaz.

> Önce: Platform hızlı, güvenli ve ölçeklenebilir bir altyapı sunar.
> Sonra: Platform saniyede 40 bin istek kaldırıyor. Güvenlik tarafı henüz denetimden geçmedi.

## Uyarı

Bu dosya üretim içindir, tespit için değil. Türk akademik yazı geleneği LLM'in varsayılan
sesine yapısal olarak benzer ("yapıl-" ile başlayan cümle "-maktadır" ile biter) ve İngilizceye
ayarlı dedektörler ana dili İngilizce olmayan yazarları %61'e varan oranda hatalı işaretler.
Buradaki kuralları başkasının metnini yargılamak için kullanma.
