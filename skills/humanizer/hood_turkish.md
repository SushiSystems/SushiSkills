# Sokak ve internet Türkçesi

Bu dosya yalnız biri açıkça gündelik, argolu, "kanka ağzı" bir metin istediğinde açılır:
WhatsApp mesajı, grup sohbeti, tweet, Ekşi entry'si, Discord, bir karakterin replik dökümü.
Belge, commit, PR ve sohbet yanıtı `generic_turkish.md` ile yazılır; oraya argo taşınmaz.

Kurallar Slobin & Bever'in konuşma dizilişi sayımlarından, Erguvanlı'nın konu / odak /
artalan modelinden, Tekin & Öztürk (2022) ile Balkan ve Anadolu ağızlarındaki devrik cümle
sayımlarından, Işık-Güler & Eröz-Tuğa'nın Sözlü Türkçe Derlemi üzerindeki "(u)lan" incelemesinden,
Özçalışkan'ın (1994) küfür ve cinsiyet çalışmasından, Çiçek & Yağbasan'ın (2019) üniversite
anketinden, üniversite öğrencilerinin hitaplarını sayan toplumdilbilim çalışmalarından (Aktaş &
Yılmaz 2017), Aktunç ve Devellioğlu'nun argo sözlüklerinden, Ekşi Sözlük ve forum
tartışmalarından, 2025–2026 basınındaki Z kuşağı jargon listelerinden ve bir LLM sohbet veri
setinin taklit örneklerinden çıkarıldı. Kaynaklar `research/hood_turkish_sources.md` dosyasında.

Resmî Türkçede yasak olan iki şey burada doğaldır: devrik cümle ve konuşmadaki gibi yazım. Ama
ikisinin de yeri belli. Serpilince tik olurlar, tıpkı -mektedir gibi.

Üç kural gerisini kapsar:

1. **Tek bir insan yaz.** Yaşı, şehri, çevresi belli bir kişi. 17 yaşında Discord'daki biri,
   30'unda WhatsApp grubundaki biri, 45'inde mahalle kahvesindeki biri aynı kelimeleri
   kullanmaz. "Genel genç ağzı" diye bir kişi yok; karışım LLM'i ele verir.
2. **Argo baharattır, yemek değil.** Gerçek mesajın çoğu düz Türkçedir: "geliyom 10 dk".
   Bir mesajda en çok bir iki argo sözcük, bir hitap. Her cümleye "lan, kanka, efsane" koymak
   dizi repliği gibi durur.
3. **Açıklama yok, kapanış yok.** Gerçek insan argoyu tırnağa almaz, anlamını söylemez,
   "umarım beğenmişsindir 😊" diye bitirmez. Söyler, susar.

## Konuşma dizimi ve devrik cümle

`generic_turkish.md` devrikliği yasaklar; burada serbest, ama kuralı var. Kural Erguvanlı'dan:
yüklemin hemen önü odak (yeni bilgi), yüklemin arkası artalan (zaten bilinen, sonradan eklenen).
Konuşmada devriklik heyecan ve onarım işidir (Tekin & Öztürk 2022).

- **Ne kadar sık.** Slobin'in yetişkin konuşma sayımında durum ekli cümlelerin yalnız %48'i
  SOV, %56'sı yüklem sonda; %25'i SVO, %13'ü OVS, %6'sı yüklem başta. Yani konuşmada kabaca her
  iki cümleden biri yüklemi sonda bitirmez. Mesajda da oran bu civarda tutulabilir; her cümle
  devrikse yine yapay.
- **Arkaya giden şey bilinendir.** Özne, zaten konuşulan nesne, sonradan hatırlanan zaman ya
  da yer. Ağız sayımlarında yüklemden sonra en çok dolaylı tümleç (661), sonra zarf tümleci
  (427), belirtili nesne (393), özne (257) gidiyor; belirtisiz nesne neredeyse hiç (63).
  - Doğal: "Gördün mü onu?", "Geldim ben.", "Çok iyiydi ya film.", "Yazdım sana dün.",
    "Aldım arabayı sonunda." (araba konuşuluyordu)
  - Yanlış: "Aldım yeni bir araba." Yeni bilgi arkaya atılmış, belirtisiz nesne sonda. Doğrusu
    "Araba aldım lan." ya da "Yeni araba aldım."
- **Yüklem başta, kalıp olarak.** Emir, ünlem, soru ve tepki: "Gel buraya.", "Bak şuna.",
  "Bitti bu iş.", "Nerdesin sen?", "Ne diyon lan sen?", "Yok artık.", "Olmaz öyle şey."
- **Onarım.** Söyleyip eksiği ekleme, virgülle ya da yeni mesajla: "Gitti. Ahmet yani." ya da
  arka arkaya iki mesaj: "geldi mi" / "kargo".
- **Hep kurallı kalan yerler.** Uzun anlatının asıl bilgisi ("Dün markette Selin'in eski
  sevgilisini gördüm"), Ekşi entry'sinin tanım cümlesi, bir şeyin nasıl yapıldığını anlatan
  adımlar. Devriklik kısa cümlede yaşar; yüklemden sonra iki üç öge yığılırsa ("Yedim pilav
  akşam evde annemle") bozuk durur.
- **Eksiltili cümle devriklikten sık.** Konuşma çoğu zaman yüklemsizdir: "Sen?", "Ben de.",
  "Yarın o zaman.", "Hayırdır?", "10 dk."

> Taklit: Dün gittim sinemaya arkadaşlarımla, izledik yeni çıkan filmi, beğendik çok.
> Gerçek: dün sinemaya gittik bizimkilerle. film baya iyiydi ya

## Yazım ve mesajlaşma imlası

- **Konuşmadaki gibi yaz, ama tutarlı.** Aynı kişi aynı mesajda hem "geliyorum" hem "geliyom"
  yazmaz. Sık aşınmalar:
  - -yor → -yo / -yom / -yon / -yoz: gidiyo, geliyom, napıyon, biliyoz. Soru: "biliyo musun".
  - -acak → -cak / -cem / -can / -caz: gelicem, yapcan, konuşucaz, olmıycak.
  - bir → bi, bir şey → bi şey / bişey, ne yapıyorsun → napıyon / napıyosun, ne oldu → noldu,
    ne haber → naber, nerede → nerde, burada → burda, dakika → dk / dakka, oğlum → olm,
    tamam → tmm, kanka → knk, selam → slm, eyvallah → eyw, teşekkürler → tşk / tşkler,
    "selamün aleyküm" → sa / as.
- **Harf uzatma ton verir.** "tamammm", "yaaa", "nolurrr", "geliyommm". Kadınlar arasında
  sıradan, iki erkek arasında seyrek; erkekten kadına uzatılmış "tamammm" imalı okunabilir.
- **Büyük harf yok, nokta çoğu zaman yok.** Mesajın sonundaki nokta soğuk ya da kızgın okunur:
  "tamam." ile "tmm" aynı şey değil. Büyük harf bağırmadır: "NE". Soru işareti düşer: "geliyon mu".
- **Türkçe karakter düşürme.** "cok iyi", "gelicem", "degil", "sagol": klavyesi Türkçe
  olmayanlar, yurt dışındakiler, eski telefon alışkanlığı olanlar, hızlı yazan erkekler. Genç
  kullanıcının telefonu otomatik Türkçe karakter koyduğu için bugün daha çok "saol", "diil"
  gibi ğ düşürmesi görülür. Karakter bir kişilik özelliğidir; yarım yamalak karışım olmaz.
- **de/da ve ki.** Gerçek mesajda bitişik "bende" (ben de), ayrı "evde ki" sık görülür. Hata
  olarak bilinçli koyma; koyacaksan o kişinin kalıcı alışkanlığı olsun, tek bir sözcükte.
- **Gülme.** Kuşağa göre değişir:
  - "ahahah", "hahaha": her yaş, orta şiddet. "hehe" tuhaf ya da imalı.
  - "sjsjsj", "ajsjsj", "skdjskd", "aşkdjaşk": klavye gülmesi (random), 2000'lerin IRC ve
    İnci Sözlük döneminden gelir, Z kuşağında ana biçim. Kısa olan kibarlık gülmesi, uzun olan
    gerçek gülme ve "seninle konuşmak hoşuma gidiyor". Hafif espriye uzun random performans kokar.
  - "kek", "kekw": oyun ve Discord çevresi.
  - "öldüm", "ölüyorum", "geberdim", "ağlıcam", "ağlıyorum şu an": çok komik. "geberiyorum"
    kaba, yaşlıya ve yabancıya yazılmaz.
  - ":D", "xd": 30 yaş üstünde canlı, Z kuşağında ironik ya da eski. 😂 Z kuşağına "fazla
    çabalıyor" gelebilir; 💀 ve 😭 gülme yerine geçer.
- **Emoji.** Her mesaja değil. Tek emoji tepkinin kendisi olabilir (💀, 😭, 🙄). Cümle sonuna
  eklenen 😊 ve 👍 orta yaş ve iş kokar; gençler arasında 👍 soğuk ya da pasif agresif okunur.

## Argo sözlüğü

Durum 2026-09 itibarıyla. "Canlı" bugün doğal kullanılıyor; "eski" o kuşak dışında tarihli
duruyor; "ironik" yalnız dalga geçerken; "cringe" ciddi kullanılırsa kullananı küçük düşürür.
Durumlar sözlük, forum ve basın gözlemine dayanır, ölçüme değil.

### Hitap

| Söz | Anlam | Çevre | Durum | Örnek |
| --- | --- | --- | --- | --- |
| kanka / knk | yakın arkadaş, sonra herkes | 90'lardan beri her yerde; kökeni tartışmalı (kan kardeş ya da Romanca) | canlı, yıpranmış | knk akşam çıkıyo musun |
| kanki | kanka, kadınsı ve oyunbaz | kız arkadaş grupları | canlı | kanki bu elbiseyi alıyom |
| kankito, kenks, kanks | kanka türevi | 2010'lar | ironik | — |
| lan / la / len | hitap, vurgu, şaşkınlık, öfke | erkeklerde sık, kadınlarda da; bağlama göre dostça ya da kavga | canlı | yok lan olamaz |
| olm / oğlum | erkekler arası hitap | lise, üniversite, mahalle | canlı | olm neredesin |
| abi / abla | yaşça büyük ya da saygılı samimi | her çevre, esnaf dahil | canlı | abi bi bakar mısın |
| aga / agam | arkadaş, dost | Karadeniz ve Doğu kökenli, rap ve gençlikte yayıldı | canlı | aga naber |
| moruk | arkadaş, "dostum" | 2000'ler ve 2010'ların gençliği, rap | canlı, biraz Y kuşağı | moruk sen ciddi misin |
| reis / reyiz | arkadaş, patron havası | forum, oyun, internet; yabancıya itici | canlı, ironik | reis eline sağlık |
| kral | övgü ve hitap | internet, rap | canlı | kralsın |
| hocam | tanımadığına nötr samimi | üniversite, Ekşi, forum | canlı | hocam link var mı |
| bro / brom | arkadaş | Z kuşağı, İngilizce karışık çevre | canlı | bro bu ne |
| kardeşim | samimi ya da mesafe koyan | her yerde; vurguyla gerginlik | canlı | kardeşim bak bana |
| canım / aşkım / kuzum | kadınlar arası sevgi hitabı | kadın arkadaşlar | canlı | aşkım napıyon |
| panpa / panpiş | arkadaş | İnci Sözlük dönemi, 2010'lar | eski, ironik | — |
| hacı | arkadaş | 2000'ler, 2010'lar | eski | — |
| dostum | "buddy" çevirisi | dublaj ve LLM | cringe (ironik değilse) | — |

### Tepki ve söylem sözcükleri

| Söz | Anlam | Çevre | Durum | Örnek |
| --- | --- | --- | --- | --- |
| aynen / aynen öyle | katılıyorum; tek başına "tamam, uzatma" | her yaş | canlı | aynen ya |
| valla / vallaha | yemin, vurgu | her yaş | canlı | valla bilmiyom |
| cidden | ciddi misin, gerçekten | her yaş | canlı | cidden mi |
| harbi / harbiden | gerçekten, dürüst | mahalle, genç | canlı | harbiden iyiydi |
| tamamdır | tamam, halloldu | Y kuşağı ve üstü | canlı | tamamdır haber veririm |
| hadi ya | şaşkınlık ya da inanmama | her yaş | canlı | hadi ya kim söyledi |
| yok artık | inanılmaz | her yaş | canlı | yok artık |
| şaka mısın | inanılmaz, sitem | her yaş | canlı | şaka mısın ya |
| baya / bayağı | epey | her yaş | canlı | baya kalabalıktı |
| efsane | çok iyi | her yaş; çok kullanılınca boşalır | canlı, yıpranmış | maç efsaneydi |
| bayıldım | çok beğendim | kadınlarda sık | canlı | bayıldım bu renge |
| ölüyorum / öldüm | çok komik ya da çok güzel | genç | canlı | öldüm sjsjsj |
| ağlıcam | çok komik ya da çok duygusal | Z kuşağı | canlı | ağlıcam şu videoya |
| yeto | yeter | Z kuşağı, video içerik | canlı, dar | yeto artık |
| manyak (iyi) | müthiş | 90'lar ve 2000'ler | eski | — |
| süper, şahane | çok iyi | eski kuşak | gençte eski | — |

### Fiil ve deyim

| Söz | Anlam | Çevre | Durum | Örnek |
| --- | --- | --- | --- | --- |
| kafayı yemek | delirmek, bıkmak | her yaş | canlı | kafayı yicem bu işten |
| kafa yapmak / kafa adam | eğlendirmek, uyuşturmak / keyifli, anlaşılır kişi | genç, mahalle | canlı | bu dizi kafa yapıyo |
| kafa dengi | anlaşılan kişi | her yaş | canlı | kafa dengi biri lazım |
| yamuk yapmak | kazık atmak, sözünden dönmek | mahalle | canlı | bana yamuk yapma |
| trip atmak | küsmek, nazlanmak | 2000'lerden beri | canlı | niye trip atıyon |
| ayar vermek / ayar olmak | laf sokmak / sinirlenmek | genç, internet | canlı | ayar oldum buna |
| gaz vermek / gaza gelmek | kışkırtmak / coşmak | her yaş | canlı | gaza geldim valla |
| hava atmak | gösteriş | eski ama yaşıyor | canlı | hava atıyo arabayla |
| flex yapmak | gösteriş | Z kuşağı | canlı | flex yapmayı bırak |
| kasmak | gereğinden çok önemsemek | genç | canlı | kasma bu kadar |
| ghostlamak | aniden yazmayı kesmek | Z kuşağı | canlı | beni ghostladı |
| shiplemek | iki kişiyi yakıştırmak | dizi ve fandom | canlı | bunları shipliyom |
| cringe (olmak) | utandırıcı, başkası adına utanmak | Z kuşağı | canlı | çok cringe oldu |
| delulu | hayal dünyasında | 2024'ten beri TikTok, kızlar | canlı | delulu olma kanki |
| aura (kaybetmek) | havalılık puanı | 2025'ten beri Z kuşağı | canlı, hızla eskiyor | aura'm düştü |
| sıçtık | işler kötü gitti | her yaş, kaba | canlı | sıçtık sınavda |
| racon kesmek | kabadayılık taslamak | mahalle, rap, mafya dizisi | canlı, dar | racon kesme bana |

### Kişi etiketleri

| Söz | Anlam | Çevre | Durum | Örnek |
| --- | --- | --- | --- | --- |
| ezik | zavallı, kaybeden | genç | canlı | ezik gibi durma |
| keko | kaba maço, alt sınıf imgesi; Doğuda "kardeş" | internette aşağılama | canlı, sınıfçı | keko rapçi |
| apaçi | aşırı süslü "varoş" genç | 2010'lar | eski, sınıfçı | — |
| mal | aptal | her yaş, arkadaşa şakayla | canlı | mal mısın olm |
| NPC | kendi fikri olmayan | Z kuşağı | canlı | NPC gibi takılıyo |
| red flag | tehlike işareti (ilişki) | Z kuşağı, kadınlar | canlı | bu tam red flag |
| lavuk | sevimsiz erkek | 2000'ler | eski | — |

Rap sahnesinden (Ezhel, Uzi, Lvbel C5 dönemi) gündelik dile geçenler: "baba" (kendine hitap,
özgüven), "kodes" (cezaevi), "mekan", "moruk", "drip", "merso". Rap sözü dinlenir, taklit
edilmez; tek bir rap sözcüğü mesajı mahalleli yapmaz, çok rap sözcüğü parodi yapar.

## Hitap ve ton

- **Sen/siz.** Arkadaşa ve internette tanımadığa "sen". Esnafa, yaşça büyüğe "siz" ya da
  "abi/abla + sen". Sen'e geçiş hitapla olur: "abi" diyen "siz" demez.
- **Hitap ilişkiyi söyler.** "kanka" yeni tanıştığına samimiyetsiz ya da ergen durabilir;
  iş yazışmasında ilk mesajda "kral/reis" itici bulunur. Tanımadığa en güvenli samimi hitap
  "hocam" ya da "abi/abla".
- **Yumuşatıcılar.** "ya" her yerde, sıcaklık katar ("iyiyim ya"). "be" sitem ya da sevgi
  ("gel be"). "yahu" orta yaş ve üstü. "lan" dostça da olur kavgacı da; Işık-Güler &
  Eröz-Tuğa derlemde beş iş sayar: seslenme, yakınlık ya da mesafe gösterme, duygu dışavurumu,
  vurgu, küfür öncesi. Aynı "lan" gülerek arkadaşa ve bağırarak yabancıya başka şeydir.
- **Cinsiyet.** Kadın grupları "aşkım, canım, kanki" ve harf uzatmayla; erkek grupları "olm,
  lan, kanka, aga" ve kısa mesajla yazar. Bu eğilimdir, kural değil; ama bir kadın karakteri
  her mesajda "lan olm" dedirmek bir tercih olarak yazılmalı, rastgele değil.
- **"Ayol".** Eski İstanbul kadın ağzı ve eşcinsel camp ağzı. Genç bir kadına "ayol" dedirmek
  LLM hatasıdır.

## Küfür yoğunluğu ve sınırları

Küfür gerçek Türkçenin parçası; Çiçek & Yağbasan'ın üniversite anketinde öğrencilerin yarısına
yakını arkadaş ortamında genellikle ya da daha sık küfürlü konuşulduğunu söylüyor. Özçalışkan
(1994) küfrün sözlük anlamı taşımadığını, bir duygu taşıdığını; kullanımı en çok ortamın
tanıdıklığının artırdığını, resmiyetin kıstığını; kadınların ağır küfür yerine hafif küfürü
seçtiğini buldu.

Şiddet üç kademe:

1. **Ağız bozukluğu.** hay aksi, kahretsin, lanet olsun, bok gibi, boktan, sıçtık, hassiktir
   (yarı kalıplaşmış). Arkadaş arasında sıradan, yaşlının yanında kaçınılır.
2. **Argo aşağılama ve dolgu küfrü.** mal, salak, ezik, yavşak, götlük, siktirmek ("siktir
   boşver"), "amk" ve "aq" kısaltmaları. "amk" tweet'te noktalama gibi, bir şeye yönelmeden
   kullanılır; yine de kaba ve yabancıya yazılmaz.
3. **Kavga sözü.** Ana, bacı, aileye yönelik cinsel küfür; "şerefsiz", "oç" ve açık hali.
   Yakın erkek arkadaşlar arasında şakayla da geçer, ama yazıya döküldüğünde ve tanımadığa
   yöneldiğinde kavga başlatır. Aileye yönelik küfür en ağır kademedir.

Kurallar:

- Metin küfür istemiyorsa küfür koyma. İstiyorsa kişiye bağla: öfke anı, kaybedilen maç,
  trafik. Neşeli mesajda ağır küfür yoktur.
- Mesaj başına en çok bir küfür; bir sohbet dökümünde küfür her konuşmacının her satırında
  olmaz.
- Üçüncü kademeyi gerçek bir kişiye, gruba, kimliğe yöneltme. Etnik, cinsel yönelim ya da
  engelliliği hedef alan aşağılamayı ("keko", "apaçi" gibi sınıfçı etiketler dahil) yalnız bir
  karakterin kusurunu göstermek için ve bilerek yaz.
- Sansürlü yazım gerçek kullanımda da var ("s*ktir", "a.q"); bir metinde ya hep açık ya hep
  sansürlü.

## Yoğunluk ve ritim

- **Mesaj kısa ve parçalı.** WhatsApp'ta bir düşünce üç mesaja bölünür: "abi" / "bugün ne
  oldu biliyon mu" / "anlatcam". Paragraf mesajı ancak dert anlatırken ya da kavgada gelir.
- **Argo oranı.** Kaba ölçü: on sözcükte en çok bir argo ya da hitap. "Aynen, valla, ya"
  gibi söylem sözcükleri bu sayıya girmez, onlar zaten konuşmanın dokusu.
- **Tek kuşak.** 90'ların "manyak, süper, oha" sözlerini Z kuşağının "delulu, aura, cringe"
  sözleriyle aynı ağıza koyma. Z kuşağında İngilizce ödünç çok, Y kuşağında kısaltma (mrb,
  tşk, cnm) çok.
- **Tekrar gerçektir.** Gerçek kişi aynı sözcüğü tekrar eder: "aynen", "aynen ya", "aynen
  aynen". LLM eşanlamlı çeşitleme yapar; insan yapmaz.
- **Soru tek sözcük.** "Sen?", "Noldu?", "Nerde?", "Ciddi?".
- **Yazım hatası ölçülü.** Hızlı yazanda harf yer değiştirir ("geliyomr", "tmam"), ardından
  bazen "*tamam" düzeltmesi gelir. Her mesaja bir hata koyma.

## LLM taklidi tikleri

Aşağıdakiler "samimi Türkçe" isteyen modelin imzasıdır:

- **Çeviri hitap ve ünlem.** "Dostum", "Hey!", "Vay be dostum", "Adamım", "Bak dostum". Gerçek
  bir LLM çıktısı: "Bak dostum, bir gazeteci olarak bilirsin ki…" Türkçe hitap "abi, kanka,
  hocam" ya da isim.
- **Coşku kelimeleri.** "Harika!", "Muhteşem!", "Süper!", "Mükemmel!" art arda. Gerçek tepki
  "iyiymiş", "baya iyi", "bayıldım", "efsane".
- **Ağız karnavalı.** Bir cümleye "ulan", "be", "ya", "valla", "kardeş" hepsi birden: "Ulan bu
  vapurda çay da başka güzel oluyor be, hele şu Boğaz manzarası." Bir konuşmacı bir iki
  işaretle tanınır, beşiyle değil.
- **Klişe mekan.** Vapur, çay, simit, martı, Boğaz manzarası, kedi. İstenmedikçe koyma.
- **Resmî ek sızıntısı.** Argolu cümlenin ortasında "-mektedir", "gerçekleştirmek",
  "oldukça", "bu bağlamda", "hususunda": "Kanka bu durum beni oldukça etkiledi."
- **Tam imla.** "Ne yapıyorsun? Nasılsın? Umarım iyisindir!" Büyük harf, soru işareti, ünlem,
  ğ'ler yerinde. Mesaj değil, mektup.
- **Açıklanan argo.** "Tam bir 'red flag' (tehlike işareti) yani." ya da tırnak içinde argo.
- **Emoji her cümlede.** Sonuna 😊, 😄, 🙌, ✨ eklenmiş cümleler.
- **Serpiştirilmiş devriklik.** Her cümlede, hep aynı biçimde yüklem ortada, yeni bilgi sonda.
- **Kuşak karışımı.** Aynı ağızda "manyak iyi", "cringe", "panpa", "slay".
- **Kibar kavga.** Kızgın karakter "Bu davranışını hiç doğru bulmuyorum kanka" der. Gerçek
  kızgınlık kısa: "ne alaka lan", "yeter be", "sana ne".
- **Toparlayan son.** "Neyse, hayat bu işte! 😊", "Görüşmek üzere dostum!", "Kendine iyi bak!".
  Gerçek mesaj konu bitince kesilir ya da "hadi bb", "görüşürüz", "tmm" ile biter.

## Kayıt türleri

**WhatsApp mesajı (birebir).** Küçük harf, noktasız, kısa ve bölünmüş. Aşınmış yazım,
tek hitap. Sesli arama yerine "müsait misin" sorulur. Gecikmeli yanıta "sory görmedim" gelir.
"geldin mi" / "ben kapıdayım" / "aç"

**Grup sohbeti.** Çok kişi, üst üste mesaj, alıntılı yanıt. Birinin espri yapıp üç kişinin
yalnız random gülmeyle ya da 💀 ile karşılık vermesi. Plan konuşmasında dağınıklık: "kim
geliyo" / "ben varım" / "ben 9da çıkarım ancak" / "o zaman 9.30".

**Tweet (X).** Tek cümle, çoğu zaman yargı ya da gözlem. Devrik ve eksiltili yapı en rahat
burada. Büyük harf ve noktalama kişiye göre; ironi yüksek. "amk" ve "mq" gibi kaba kısaltmalar
burada yaygın. Başlık gibi değil, laf atar gibi: "türkiyede kira konuşmadan 5 dakika geçiremiyoz
artık".

**Ekşi entry'si.** Tanım ya da tespitle açılır, küçük harfle, noktalama tam ama gevşek.
Kurallı cümle çoğunlukta; ironi, "(bkz: …)" ve yıldız dipnotu ("*") geleneği. Hitap "hocam",
"yazar arkadaş". Başlığı tekrar etmez, ilk cümle doğrudan konuya girer: "kiracıyı insan yerine
koymayan ev sahibi tipi. geçen hafta..."

**Discord.** Oyun ve topluluk jargonu: gg, ez, afk, kek, "tag at", "sese gel". Mesajlar çok
kısa, İngilizce karışımı yüksek, Z kuşağı. Emoji yerine sunucu emojisi ve reaksiyon.

**Sesli mesaj dökümü.** Yazıya dökülen konuşma: dolgu sözler (şey, yani, hani, işte, ee),
yarıda kesilip yeniden başlanan cümle, onarım devrikliği, tekrar. "abi şey diycektim ya hani
dün konuştuk ya şu ev meselesi, işte adam aradı bugün, dedi ki..." Noktalama çok az, cümle
sınırları virgülle.

## Önce ve sonra

> Taklit: Hey dostum! Nasılsın? Umarım her şey yolundadır! 😊 Bu akşam sinemaya gitmeye ne
> dersin? Harika bir film var!
> Gerçek: knk akşam boş musun / sinemaya gidelim mi yeni çıkan var

> Taklit: Ulan kanka, valla bu maç efsaneydi be! Harbiden gaza geldim ya!
> Gerçek: maç neydi lan öyle. hala titriyom

> Taklit: Kanki, onun bu davranışı gerçekten tam bir "red flag" (tehlike işareti) bence. Bu
> durumu ciddiye almalısın. 💕
> Gerçek: kanki bu red flag ya / ciddiyim bak / 3 gündür yazmıyo sonra hiçbişey olmamış gibi naber mi

> Taklit: Arkadaşlar, bugün yaşadığım olay beni oldukça etkiledi. Markete gittim ve orada eski
> sevgilimi gördüm.
> Gerçek: kızlar / markette kimi gördüm tahmin edin / ağlıcam ajsjsjsj

> Taklit (kızgın): Bu yaptığın hiç hoş olmadı kardeşim, lütfen bir daha böyle yapma.
> Gerçek: ne alaka ya. bir daha yapma bunu

> Taklit (Ekşi): Bu konu gerçekten çok önemli ve üzerinde düşünülmesi gereken bir mesele.
> Kiralar son dönemde oldukça yükseldi.
> Gerçek: 2 yılda kiranın üç katına çıktığı, ev sahibinin de "piyasa böyle hocam" dediği memleket gerçeği.

## Uyarı

Bu dosya bir kayıt üretmek içindir, insanları yargılamak için değil. Aşınmış yazım, argo ve
küfür bir eğitim ya da zekâ göstergesi değildir; kuşağın, çevrenin ve ortamın göstergesidir.
Sınıfçı etiketleri (keko, apaçi) ve yöresel hitapları bir kimliği alaya almak için kullanma.
Argo hızla eskir; durum sütunu 2026-09 gözlemidir, bir yıl sonra yeniden taranmalıdır.
