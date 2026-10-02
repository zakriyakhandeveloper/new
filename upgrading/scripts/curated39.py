# -*- coding: utf-8 -*-
"""Curated, confidence-graded knowledge table for the islamic batch 39 (mamoona..mashooq).

Source defects found in this batch:
 * WRONG / PLACEHOLDER "Arabic forms": mandal -> "Mandal" (Latin); manel ->
   "Ahmad" (a different name entirely); manizha -> "N/A"; manja -> عائشة (a
   different name entirely); manolya -> عائشة (a different name entirely);
   manuchehr -> علي (a different name entirely); marjina -> "Aisha" (a
   different name entirely); marziya -> "Muzayyah" (a different name);
   mashel -> احمد (a different name entirely); mann -> "Mann" (Latin);
   mamoona -> مموونة (should be مأمونة); mamoor -> مامور (should be مأمور);
   mamun -> ممن (should be مأمون); mana -> منا (should be منى); manaal ->
   منال (ok); manab -> مَنَب (should be مناب); manaf -> مناف (ok); manahel ->
   مناهل (ok); manahil -> مناهل (ok); manar -> منار (ok); manara -> منارة
   (ok); manazir -> مناظر (ok); manha -> منحة (ok); manhal -> منحَل (should be
   منهل); mannan -> منان (ok); mannat -> منت (should be منّت); mansab ->
   منصب (ok); mansha -> منشأ (ok); mansura -> منصورة (ok); mansurah ->
   منصوره (should be منصورة); mansuri -> منصوري (ok); manus -> مانوس (should
   be مانوس, ok); manzar -> منظر (ok); manzoor -> منظور (ok); manzur ->
   منظوr (should be منظور); maqbool -> مقبول (ok); maqbul -> مقبول (ok);
   maqsood -> مَقصود (ok); maqsud -> مَقصود (ok); maraam -> مرام (ok);
   marah -> مرح (should be مراح); mardhiah -> مردحية (should be مرضية);
   mardin -> ماردين (ok); mardiya -> مردية (should be مردية, ok); mareen ->
   مارين (ok); marhaba -> مَرْحَبَ (should be مرحبا); maria -> ماريا (ok);
   mariah -> مريم (should be مارية); marii -> ماري (should be ماري); marin ->
   مَرين (should be مارين); marium -> مريم (ok); mariyah -> ماريه (should be
   مارية); mariyam -> مريم (ok); marjan -> مرجان (ok); marjana -> مرجانة
   (ok); marjani -> مرجاني (ok); marmar -> مرمر (ok); maroof -> مَرُوف
   (should be معروف); maruf -> معروف (ok); maruff -> مروٴف (should be معروف);
   marva -> مارفا (should be مروة); marvan -> مروان (ok); marwaan -> مروان
   (ok); marwah -> مروة (ok); marwan -> مروان (ok); marwana -> ماروانة
   (should be مروانة); marwani -> مرواني (ok); marwat -> مروة (should be
   مروت); maryamah -> مريم (should be مريمه); maryum -> مريم (ok); marzi ->
   مرزي (should be مرضي); marzia -> مَرْزِيَة (should be مرضية); marzieh ->
   مرزیه (should be مرضیه); marzooq -> مرزوق (ok); marzouq -> مرزوق (ok);
   mas -> مَصْعُود (should be مسعود); masad -> مَسَاد (should be مسعد);
   masar -> مسارات (should be مسار); masarra -> مسرّة (should be مسرة);
   masbah -> مصباح (ok); maseeh -> مسيح (ok); mashaal -> مشعل (ok); mashael
   -> مشعل (should be مشاعل); mashal -> مشعل (ok); mashar -> مَشَار (should
   be مشار); mashari -> ماشاري (should be مشاري); mashhood -> مشهود (should
   be مشهود, ok); mashhoor -> مشهور (ok); mashkoor -> ماشكور (should be
   مشكور); mashood -> مشود (should be مشهود); mashooq -> ماشوق (should be
   معشوق).
 * DEGARBLED / WRONG glosses: mamoona 'Reliable, Trustworthy, Dependable'
   (should be 'trusted (fem)'); mamoor 'Determined, Resolute' (should be
   'commanded'); mamun 'Trustworthy, faithful, believer' (should be 'trusted');
   man 'Man, Human' (should be the name Man); mana 'Fortune, Wealth' (should
   be the name Mana); manaal 'From the root MAN (to be in a state' (should be
   'attainment'); manab 'Gift from God' (should be the name Manab); manaf
   'Generous, Gracious' (should be the name Manaf); manahel 'Guide, Helper'
   (should be 'springs'); manahil 'Traveler' (should be 'springs'); manal
   'Unknown' (should be 'attainment'); manar 'Lighthouse, Guide' (should be
   'lighthouse'); manara 'Guide, Beacon' (should be 'lighthouse (fem)');
   manazir 'Constellation, Arrangement, Plan' (should be 'views'); mandal
   'Brave warrior' (unsupported); manel 'Little One' (unsupported); manha
   'Support, Aid' (should be 'grant, gift'); manhal 'Resting place, shelter'
   (should be 'watering place'); manizha 'Gift of the Earth' (should be the
   Persian name Manizha); manja 'Jasmine flower' (unsupported); mann 'Man'
   (should be 'favour, grace'); mannan 'Support, Comfort' (should be
   'bountiful'); mannat 'Wish, Desire' (should be 'wish, vow'); manolya
   'Graceful, Gentle One' (should be the Turkish name Manolya); mansab 'Rank,
   Position' (correct); mansha 'Intellectual, Intelligent' (should be 'origin,
   source'); mansoor 'Unknown' (should be 'victorious'); mansour 'Victorious'
   (correct); mansur 'Triumphant, Victorious' (correct); mansura 'Protector'
   (should be 'victorious (fem)'); mansurah 'Victorious, Triumphant' (correct);
   mansuri 'Victorious, Successful' (should be nisba of Mansur); manuchehr
   'Man of Victory' (should be the Persian name Manuchehr); manus 'Follower of
   Prophet Moses' (unsupported); manzar 'View, Scene' (correct); manzoor
   'Capable, Able' (should be 'regarded, approved'); manzur 'Victorious,
   Triumphant' (should be 'regarded, approved'); maqbool 'Accepted by Allah'
   (should be 'accepted'); maqbul 'Accepted, Welcomed' (correct); maqsood
   'Desired, Intended, Wished For' (correct); maqsud 'Intended, Desired,
   Purpose' (correct); maraam 'Guide, Companion' (should be 'aim, purpose');
   marah 'Bitter, Affliction, Test' (should be 'joy'); maram 'Desire,
   aspiration' (correct); mardhiah 'Helpful one' (should be 'pleasing,
   content'); mardin 'City, fortress' (should be the place name Mardin);
   mardiya 'Dewdrop' (unsupported); mareen 'Gardener, night lover'
   (unsupported); marhaba 'Welcome' (correct); maria 'Rebellious one, bitter,
   or rebelliou' (should be the name Maria); mariah 'Rebellious' (should be
   the name Maria); mariam 'Unknown' (should be the name Maryam); marii
   'Bitter' (should be the name Mari); marin 'From the sea' (unsupported);
   marium 'My blessed one' (should be the name Maryam); mariyah 'Mary' (should
   be the name Maria); mariyam 'Bitter or wished-for child' (should be the
   name Maryam); marjan 'Coral' (correct); marjana 'Gentle, Jasmine' (should
   be 'coral (fem)'); marjani 'Exalted, Noble, Radiant' (should be nisba of
   Marjan); marjina 'Gentle, tender, delicate' (unsupported); marmar
   'Lighthouse, Guiding Light' (should be 'marble'); maroof 'Friend' (should
   be 'known'); maruf 'Known, Famous, Renowned' (correct); maruff 'Friend of
   Allah' (should be 'known'); marva 'Bitter, rebellious' (should be the name
   Marwa); marvan 'Lord of the forest' (should be the name Marwan); marwa
   'Unknown' (should be the name Marwa); marwaan 'Born of a warrior' (should
   be the name Marwan); marwah 'Source of water' (should be the name Marwa);
   marwan 'A stone or a small pebble' (should be the name Marwan); marwana
   'Flower of Paradise' (should be 'of Marwan (fem)'); marwani 'From Marwan'
   (correct); marwat 'Worthy, Deserving' (should be the name Marwat); maryam
   'Unknown' (should be the name Maryam); maryamah 'Blessed, Pious' (should be
   the name Maryam); maryum 'Praiseworthy' (should be the name Maryam); marzi
   'Graceful, Delicate' (should be 'pleasing'); marzia 'Bitter or Wished-for
   Child' (should be 'pleasing (fem)'); marzieh 'Beloved, Precious' (should be
   'pleasing (fem)'); marziya 'Exalted, Noble' (should be 'pleasing (fem)');
   marzooq 'He who is rich, wealthy' (should be 'provided for'); marzouq 'One
   who crushes, subdues' (should be 'provided for'); mas 'Fortunate, Happy'
   (should be the name Masud); masad 'Stone' (should be the name Masaad);
   masar 'Path, Way' (correct); masarra 'Delicate, Graceful' (should be
   'joy'); masbah 'Lamp, Light' (correct); maseeh 'Messiah, Savior' (correct);
   mashaal 'Torch' (correct); mashael 'A gentle breeze' (should be 'torches');
   mashal 'Torch, Light' (correct); mashar 'Traveler on the path to God'
   (should be 'way, path'); mashari 'Guide, path, way' (should be 'paths');
   mashel 'Scorpion' (unsupported); mashhood 'Wronged, Oppressed, Unjustly
   Treated' (should be 'witnessed'); mashhoor 'Famous, Renowned' (correct);
   mashkoor 'Grateful to God' (should be 'thanked'); mashood 'Honored' (should
   be 'witnessed'); mashooq 'Beloved, Lover, Adored' (correct).
 * MISLABELLED ORIGIN: manizha (Persian), manolya (Turkish), manuchehr
   (Persian), marzieh (Persian), marziya (Persian), marjan (Persian),
   marjani (Persian), mardin (place name), marhaba (Arabic greeting).
 * GENDER ERRORS: man, manaal, manab, manar, manhal, mann, mansha, maram,
   marhaba, marin, marjan, marjani, marmar, marwah, marwat, marzi, mashal,
   mashari, mashooq were labelled female or unisex where documented usage is
   male.
 * JUNK / UNVERIFIABLE ENTRIES: manal, mansoor, mariam, marwa, maryam (8-key
   stubs); mandal, manel, manizha, manja, manolya, manus, mardiya, mareen,
   marin, marjina, mashel.
 * DUPLICATE CLUSTERS: mamoona/mamun; mansoor/mansour/mansur;
   mansura/mansurah; maqbool/maqbul; maqsood/maqsud; maraam/maram;
   maria/mariah/marii/mariyah; mariam/marium/mariyam/maryam/maryamah/maryum;
   maroof/maruf/maruff; marva/marwa/marwah/marwat;
   marvan/marwaan/marwan; marzi/marzia/marzieh/marziya;
   marzooq/marzouq; mashaal/mashal; mashael/mashari;
   mashhood/mashood; manar/manara; manahel/manahil.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curated38 import GLOSSES as _G38

GLOSSES = dict(_G38)
GLOSSES.update({
    "trusted_f": {"en": "Trusted, reliable (feminine)", "ur": "مأمونہ، قابل اعتماد (مؤنث)", "fa": "مأمونه، قابل اعتماد (مؤنث)", "hi": "मामूना, विश्वसनीय (स्त्री)", "ps": "مأمونه، باوري", "ar": "المأمونة، الموثوقة، الأمينة"},
    "commanded": {"en": "Commanded, ordered, appointed", "ur": "مأمور، حکم یافتہ، مقرر", "fa": "مأمور، فرمانیافته، گماشته", "hi": "आदेशित, मामूर, नियुक्त", "ps": "مأمور، امر شوی، ټاکل شوی", "ar": "المأمور، المأمور به، المعين"},
    "trusted_m": {"en": "Trusted, reliable, faithful", "ur": "مأمون، قابل اعتماد، امین", "fa": "مأمون، قابل اعتماد، امین", "hi": "मामून, विश्वसनीय, अमीन", "ps": "مأمون، باوري، امین", "ar": "المأمون، الموثوق، الأمين"},
    "man": {"en": "Man; a male given name", "ur": "مان (مردانہ نام)", "fa": "مان (نام مردانه)", "hi": "मान (पुरुष नाम)", "ps": "مان (نر نوم)", "ar": "مَان (اسم علم مذكر)"},
    "mana": {"en": "Mana; a female given name", "ur": "منیٰ (زنانہ نام)", "fa": "منی (نام زنانه)", "hi": "मना (स्त्री नाम)", "ps": "منی (ښځينه نوم)", "ar": "مَنَى (اسم علم مؤنث)"},
    "attainment": {"en": "Attainment, achievement, acquisition", "ur": "منال، حصول، کامیابی", "fa": "منال، دستیابی، کامیابی", "hi": "प्राप्ति, मनाल, उपलब्धि", "ps": "منال، ترلاسه کول، بریا", "ar": "المنال، التحصيل، الإنجاز"},
    "manab": {"en": "Manab; a male given name", "ur": "مناب (مردانہ نام)", "fa": "مناب (نام مردانه)", "hi": "मनाब (पुरुष नाम)", "ps": "مناب (نر نوم)", "ar": "مَنَاب (اسم علم مذكر)"},
    "manaf": {"en": "Manaf; a male given name", "ur": "مناف (مردانہ نام)", "fa": "مناف (نام مردانه)", "hi": "मनाफ़ (पुरुष नाम)", "ps": "مناف (نر نوم)", "ar": "مَنَاف (اسم علم مذكر)"},
    "springs": {"en": "Springs, watering places", "ur": "مناحل، چشمے", "fa": "مناهل، چشمهها", "hi": "झरने, मनाहिल", "ps": "مناهل، چینې", "ar": "المناهل، العيون، الينابيع"},
    "lighthouse": {"en": "Lighthouse, minaret, beacon", "ur": "منار، مینار، روشنی کا مینار", "fa": "منار، مناره، فانوس", "hi": "मीनार, मनार, प्रकाश-स्तंभ", "ps": "منار، مینار، روښانه برج", "ar": "المنار، المنارة، الفنار"},
    "lighthouse_f": {"en": "Lighthouse, beacon (feminine)", "ur": "منارہ، روشنی کا مینار", "fa": "مناره، فانوس", "hi": "मनारा, प्रकाश-स्तंभ", "ps": "مناره، روښانه برج", "ar": "المنارة، الفنار، المشكاة"},
    "views": {"en": "Views, scenes, perspectives", "ur": "مناظر، نظارے", "fa": "مناظر، چشماندازها", "hi": "दृश्य, मनाज़िर", "ps": "مناظر، لیدونه", "ar": "المناظر، المشاهد، المرائي"},
    "mandal": {"en": "Mandal; a male given name", "ur": "منڈل (مردانہ نام)", "fa": "مندل (نام مردانه)", "hi": "मंडल (पुरुष नाम)", "ps": "منډل (نر نوم)", "ar": "مَنْدَل (اسم علم مذكر)"},
    "manel": {"en": "Manel; a female given name", "ur": "مانیل (زنانہ نام)", "fa": "مانل (نام زنانه)", "hi": "मनेल (स्त्री नाम)", "ps": "مانل (ښځينه نوم)", "ar": "مَانِل (اسم علم مؤنث)"},
    "grant": {"en": "Grant, gift, bestowal", "ur": "منحة، عطیہ، بخشش", "fa": "منحه، بخشش، عطا", "hi": "अनुदान, मिन्हा, उपहार", "ps": "منحه، بسنه، عطا", "ar": "المنحة، العطاء، الهبة"},
    "watering_place": {"en": "Watering place, resting place", "ur": "منہل، پانی کا مقام", "fa": "منهل، آبشخور", "hi": "जलस्थल, मनहल", "ps": "منهل، د اوبو ځای", "ar": "المنهل، المورد، المشرب"},
    "manizha": {"en": "Manizha; a Persian female given name", "ur": "منیژہ (فارسی نام)", "fa": "منیژه (نام زنانه)", "hi": "मनीज़ा (फ़ारसी नाम)", "ps": "منیژه (فارسي نوم)", "ar": "مَنِيزْه (اسم علم مؤنث فارسي)"},
    "manja": {"en": "Manja; a female given name", "ur": "مانجا (زنانہ نام)", "fa": "مانجا (نام زنانه)", "hi": "मंजा (स्त्री नाम)", "ps": "مانجا (ښځينه نوم)", "ar": "مَانْجَا (اسم علم مؤنث)"},
    "favour": {"en": "Favour, grace, bounty", "ur": "من، فضل، احسان", "fa": "من، لطف، بخشش", "hi": "कृपा, मन्न, अनुग्रह", "ps": "من، لطف، احسان", "ar": "المن، الفضل، الإحسان"},
    "bountiful": {"en": "Bountiful, generous, gracious", "ur": "منان، بے حد دینے والا", "fa": "منان، بخشنده، کریم", "hi": "दानशील, मन्नान, कृपालु", "ps": "منان، سخي، بخښونکی", "ar": "المنان، الكريم، الوهاب"},
    "wish_vow": {"en": "Wish, vow, prayer", "ur": "منت، مراد، دعا", "fa": "منت، آرزو، دعا", "hi": "मन्नत, इच्छा, प्रार्थना", "ps": "منت، هیله، دعا", "ar": "المنة، الأمنية، الدعاء"},
    "manolya": {"en": "Manolya; a Turkish female given name", "ur": "مانولیا (ترکی نام)", "fa": "مانولیا (نام ترکی)", "hi": "मनोल्या (तुर्की नाम)", "ps": "مانولیا (ترکي نوم)", "ar": "مَانُولْيَا (اسم علم مؤنث تركي)"},
    "rank": {"en": "Rank, position, office", "ur": "منصب، عہدہ، درجہ", "fa": "منصب، مقام، رتبه", "hi": "पद, मनसब, ओहदा", "ps": "منصب، دنده، رتبه", "ar": "المنصب، المقام، الرتبة"},
    "origin_source": {"en": "Origin, source, derivation", "ur": "منشأ، اصل، سرچشمہ", "fa": "منشأ، اصل، سرچشمه", "hi": "उद्गम, मंशा, स्रोत", "ps": "منشأ، اصل، سرچینه", "ar": "المنشأ، الأصل، المصدر"},
    "victorious": {"en": "Victorious, triumphant, aided", "ur": "منصور، فاتح، کامیاب", "fa": "منصور، پیروز، کامیاب", "hi": "विजयी, मंसूर, विजेता", "ps": "منصور، بریالی، بریالی", "ar": "المنصور، المظفر، الغالب"},
    "victorious_f": {"en": "Victorious, triumphant (feminine)", "ur": "منصورہ، فاتح (مؤنث)", "fa": "منصوره، پیروز (مؤنث)", "hi": "मंसूरा, विजयी (स्त्री)", "ps": "منصوره، بریالې", "ar": "المنصورة، المظفرة، الغالبة"},
    "mansuri": {"en": "Mansuri; of Mansur, belonging to Mansur", "ur": "منصوری، منصور سے منسوب", "fa": "منصوری، منسوب به منصور", "hi": "मंसूरी, मंसूर से", "ps": "منصوري، د منصور اړوند", "ar": "المنصوري، منسوب إلى المنصور"},
    "manuchehr": {"en": "Manuchehr; a Persian male given name", "ur": "منوچہر (فارسی نام)", "fa": "منوچهر (نام مردانه)", "hi": "मनूचेहर (फ़ारसी नाम)", "ps": "منوچهر (فارسي نوم)", "ar": "مَنُوچِهْر (اسم علم مذكر فارسي)"},
    "manus": {"en": "Manus; a male given name", "ur": "مانوس (مردانہ نام)", "fa": "مانوس (نام مردانه)", "hi": "मानूस (पुरुष नाम)", "ps": "مانوس (نر نوم)", "ar": "مَانُوس (اسم علم مذكر)"},
    "view_scene": {"en": "View, scene, spectacle", "ur": "منظر، نظارہ، منظر", "fa": "منظر، چشمانداز، نمایش", "hi": "दृश्य, मंज़र, नज़ारा", "ps": "منظر، لید، ننداره", "ar": "المنظر، المشهد، المرأى"},
    "regarded": {"en": "Regarded, approved, looked upon", "ur": "منظور، منظور شدہ، قبول", "fa": "منظور، پذیرفته، مورد نظر", "hi": "स्वीकृत, मंज़ूर, विचारित", "ps": "منظور، منل شوی، قبول", "ar": "المنظور، المقبول، المعتبر"},
    "accepted": {"en": "Accepted, approved, received", "ur": "مقبول، قبول شدہ، پسندیدہ", "fa": "مقبول، پذیرفته، پسندیده", "hi": "स्वीकृत, मक़बूल, पसंदीदा", "ps": "مقبول، منل شوی، خوښ", "ar": "المقبول، المرضي، المستجاب"},
    "desired": {"en": "Desired, intended, wished for", "ur": "مقصود، مراد، مطلوب", "fa": "مقصود، مراد، خواسته", "hi": "अभीष्ट, मक़सूद, इच्छित", "ps": "مقصود، مراد، غوښتل شوی", "ar": "المقصود، المراد، المطلوب"},
    "aim": {"en": "Aim, purpose, intention", "ur": "مرام، مقصد، ارادہ", "fa": "مرام، مقصود، هدف", "hi": "लक्ष्य, मराम, उद्देश्य", "ps": "مرام، مقصد، هدف", "ar": "المرام، المقصد، الغرض"},
    "joy": {"en": "Joy, happiness, delight", "ur": "مراح، خوشی، مسرت", "fa": "مراح، شادی، خوشی", "hi": "आनंद, मराह, ख़ुशी", "ps": "مراح، خوښي، مېله", "ar": "المراح، الفرح، السرور"},
    "pleasing": {"en": "Pleasing, content, satisfactory", "ur": "مرضی، راضی، پسندیدہ", "fa": "مرضی، راضی، پسندیده", "hi": "प्रसन्न, मरज़ी, संतुष्ट", "ps": "مرضي، راضي، خوښ", "ar": "المرضي، الراضي، المقبول"},
    "mardin": {"en": "Mardin; a city in Turkey", "ur": "ماردین، ترکی کا شہر", "fa": "ماردین، شهری در ترکیه", "hi": "मार्दिन, तुर्की का शहर", "ps": "ماردین، د ترکيې ښار", "ar": "مَارْدِين، مدينة في تركيا"},
    "mardiya": {"en": "Mardiya; a female given name", "ur": "مردیہ (زنانہ نام)", "fa": "مردیه (نام زنانه)", "hi": "मर्दिया (स्त्री नाम)", "ps": "مردیه (ښځينه نوم)", "ar": "مَرْدِيَة (اسم علم مؤنث)"},
    "mareen": {"en": "Mareen; a female given name", "ur": "مارین (زنانہ نام)", "fa": "مارین (نام زنانه)", "hi": "मरीन (स्त्री नाम)", "ps": "مارین (ښځينه نوم)", "ar": "مَارِين (اسم علم مؤنث)"},
    "welcome": {"en": "Welcome, greeting", "ur": "مرحبا، خوش آمدید", "fa": "مرحبا، خوش آمدید", "hi": "स्वागत, मरहबा", "ps": "مرحبا، ښه راغلاست", "ar": "مرحبا، أهلاً وسهلاً"},
    "maria": {"en": "Maria; a female given name", "ur": "ماریہ (زنانہ نام)", "fa": "ماریه (نام زنانه)", "hi": "मारिया (स्त्री नाम)", "ps": "ماریه (ښځينه نوم)", "ar": "مَارِيَة (اسم علم مؤنث)"},
    "maryam": {"en": "Maryam; a female given name, mother of Jesus", "ur": "مریم (زنانہ نام)", "fa": "مریم (نام زنانه)", "hi": "मरयम (स्त्री नाम)", "ps": "مریم (ښځينه نوم)", "ar": "مَرْيَم (اسم علم مؤنث)"},
    "marii": {"en": "Mari; a female given name", "ur": "ماری (زنانہ نام)", "fa": "ماری (نام زنانه)", "hi": "मारी (स्त्री नाम)", "ps": "ماري (ښځينه نوم)", "ar": "مَارِي (اسم علم مؤنث)"},
    "marin": {"en": "Marin; a female given name", "ur": "مارین (زنانہ نام)", "fa": "مارین (نام زنانه)", "hi": "मारिन (स्त्री नाम)", "ps": "مارین (ښځينه نوم)", "ar": "مَارِين (اسم علم مؤنث)"},
    "coral": {"en": "Coral", "ur": "مرجان، مونگا", "fa": "مرجان، مرجان", "hi": "मूंगा, मरजान", "ps": "مرجان، مرجان", "ar": "المرجان، البسذ"},
    "coral_f": {"en": "Coral (feminine)", "ur": "مرجانہ، مونگا", "fa": "مرجانه، مرجان", "hi": "मरजाना, मूंगा", "ps": "مرجانه، مرجان", "ar": "المرجانة، البسذة"},
    "marjani": {"en": "Marjani; of coral, belonging to coral", "ur": "مرجانی، مرجان سے منسوب", "fa": "مرجانی، منسوب به مرجان", "hi": "मरजानी, मूंगे से", "ps": "مرجاني، د مرجان اړوند", "ar": "المرجاني، منسوب إلى المرجان"},
    "marjina": {"en": "Marjina; a female given name", "ur": "مرجینہ (زنانہ نام)", "fa": "مرجینه (نام زنانه)", "hi": "मरजीना (स्त्री नाम)", "ps": "مرجینه (ښځينه نوم)", "ar": "مَرْجِينَة (اسم علم مؤنث)"},
    "marble": {"en": "Marble", "ur": "مرمر، سنگ مرمر", "fa": "مرمر، سنگ مرمر", "hi": "संगमरमर, मरमर", "ps": "مرمر، مرمر ډبره", "ar": "المرمر، الرخام"},
    "marwa": {"en": "Marwa; a female given name and place name", "ur": "مروہ (زنانہ نام)", "fa": "مروه (نام زنانه)", "hi": "मरवा (स्त्री नाम)", "ps": "مروه (ښځينه نوم)", "ar": "مَرْوَة (اسم علم مؤنث وموضع)"},
    "marwan": {"en": "Marwan; a male given name", "ur": "مروان (مردانہ نام)", "fa": "مروان (نام مردانه)", "hi": "मरवान (पुरुष नाम)", "ps": "مروان (نر نوم)", "ar": "مَرْوَان (اسم علم مذكر)"},
    "marwana": {"en": "Marwana; of Marwan (feminine)", "ur": "مروانہ، مروان سے منسوب (مؤنث)", "fa": "مروانه، منسوب به مروان (مؤنث)", "hi": "मरवाना, मरवान से (स्त्री)", "ps": "مروانه، د مروان اړوند", "ar": "مَرْوَانَة، منسوبة إلى مروان"},
    "marwani": {"en": "Marwani; of Marwan, belonging to Marwan", "ur": "مروانی، مروان سے منسوب", "fa": "مروانی، منسوب به مروان", "hi": "मरवानी, मरवान से", "ps": "مرواني، د مروان اړوند", "ar": "المرواني، منسوب إلى مروان"},
    "marwat": {"en": "Marwat; a male given name", "ur": "مروت (مردانہ نام)", "fa": "مروت (نام مردانه)", "hi": "मरवत (पुरुष नाम)", "ps": "مروت (نر نوم)", "ar": "مَرْوَت (اسم علم مذكر)"},
    "marzi": {"en": "Marzi; pleasing, content", "ur": "مرضی، راضی، پسندیدہ", "fa": "مرضی، راضی، پسندیده", "hi": "मरज़ी, प्रसन्न, संतुष्ट", "ps": "مرضي، راضي، خوښ", "ar": "المرضي، الراضي، المقبول"},
    "marzia": {"en": "Marzia; pleasing (feminine)", "ur": "مرضیہ، راضی (مؤنث)", "fa": "مرضیه، راضی (مؤنث)", "hi": "मरज़िया, प्रसन्न (स्त्री)", "ps": "مرضیه، راضي", "ar": "المرضية، الراضية، المقبولة"},
    "marzieh": {"en": "Marzieh; pleasing (feminine, Persian)", "ur": "مرضیہ، راضی (مؤنث)", "fa": "مرضیه، راضی (مؤنث)", "hi": "मरज़ीह, प्रसन्न (स्त्री)", "ps": "مرضیه، راضي", "ar": "المرضية، الراضية، المقبولة (فارسي)"},
    "marziya": {"en": "Marziya; pleasing (feminine)", "ur": "مرضیہ، راضی (مؤنث)", "fa": "مرضیه، راضی (مؤنث)", "hi": "मरज़िया, प्रसन्न (स्त्री)", "ps": "مرضیه، راضي", "ar": "المرضية، الراضية، المقبولة"},
    "provided": {"en": "Provided for, sustained, blessed with provision", "ur": "مرزوق، رزق والا، روزی یافتہ", "fa": "مرزوق، روزیدار، بهرهمند", "hi": "रज़्क़याफ़्ता, मरज़ूक़, भरण-पोषित", "ps": "مرزوق، روزي لرونکی", "ar": "المرزوق، المنعَم عليه، الموفور"},
    "masud": {"en": "Masud; fortunate, happy", "ur": "مسعود، خوش نصیب، سعید", "fa": "مسعود، خوشبخت، سعید", "hi": "मसऊद, भाग्यशाली, सुखी", "ps": "مسعود، نیکمرغه، خوشحاله", "ar": "المسعود، السعيد، المحظوظ"},
    "masad": {"en": "Masaad; a male given name", "ur": "مسعد (مردانہ نام)", "fa": "مسعد (نام مردانه)", "hi": "मसअद (पुरुष नाम)", "ps": "مسعد (نر نوم)", "ar": "مَسْعَد (اسم علم مذكر)"},
    "path": {"en": "Path, way, course", "ur": "مسار، راستہ، راہ", "fa": "مسار، مسیر، راه", "hi": "मार्ग, मसार, रास्ता", "ps": "مسار، لار، مسیر", "ar": "المسار، الطريق، السبيل"},
    "joy_masarra": {"en": "Joy, delight, happiness", "ur": "مسرت، خوشی، شادمانی", "fa": "مسرت، شادی، خوشحالی", "hi": "प्रसन्नता, मसर्रत, ख़ुशी", "ps": "مسرت، خوښي، مېله", "ar": "المسرة، الفرح، السرور"},
    "lamp": {"en": "Lamp, light, lantern", "ur": "مصباح، چراغ، روشنی", "fa": "مصباح، چراغ، نور", "hi": "दीपक, मिस्बाह, प्रकाश", "ps": "مصباح، څراغ، رڼا", "ar": "المصباح، السراج، النور"},
    "messiah": {"en": "Messiah, anointed one", "ur": "مسیح، نجات دہندہ", "fa": "مسیح، نجاتدهنده", "hi": "मसीह, उद्धारक", "ps": "مسیح، ژغورونکی", "ar": "المسيح، المخلص، المدهون"},
    "torch": {"en": "Torch, flame, light", "ur": "مشعل، شمع، روشنی", "fa": "مشعل، شعله، نور", "hi": "मशाल, मशअल, प्रकाश", "ps": "مشعل، بل، رڼا", "ar": "المشعل، الشعلة، النور"},
    "torches": {"en": "Torches, flames", "ur": "مشاعل، مشعلیں", "fa": "مشاعل، مشعلها", "hi": "मशालें, मशाइल", "ps": "مشاعل، بلونه", "ar": "المشاعل، الشعلات، الأنوار"},
    "way_path": {"en": "Way, path, course", "ur": "مشار، راستہ، راہ", "fa": "مشار، راه، مسیر", "hi": "मार्ग, मशार, रास्ता", "ps": "مشار، لار، مسیر", "ar": "المشار، الطريق، السبيل"},
    "paths": {"en": "Paths, ways, courses", "ur": "مشاري، راستے", "fa": "مشاری، راهها", "hi": "मार्ग, मशारी", "ps": "مشاري، لارې", "ar": "المشاري، الطرق، السبل"},
    "mashel": {"en": "Mashel; a male given name", "ur": "مشیل (مردانہ نام)", "fa": "مشیل (نام مردانه)", "hi": "मशेल (पुरुष नाम)", "ps": "مشیل (نر نوم)", "ar": "مَشِيل (اسم علم مذكر)"},
    "witnessed": {"en": "Witnessed, attested, seen", "ur": "مشہود، گواہ، دیکھا ہوا", "fa": "مشهود، گواه، دیدهشده", "hi": "साक्षी, मशहूद, देखा हुआ", "ps": "مشهود، شاهد، لیدل شوی", "ar": "المشهود، الشاهد، المرئي"},
    "famous": {"en": "Famous, renowned, well-known", "ur": "مشہور، نامور، معروف", "fa": "مشهور، نامدار، معروف", "hi": "प्रसिद्ध, मशहूर, नामी", "ps": "مشهور، نامتو، پېژندل شوی", "ar": "المشهور، المعروف، الذائع"},
    "thanked": {"en": "Thanked, appreciated, grateful", "ur": "مشکور، شکر گزار، مشکور", "fa": "مشکور، سپاسگزار، قدردان", "hi": "कृतज्ञ, मशकूर, आभारी", "ps": "مشکور، شکرګزار، منندوی", "ar": "المشكور، الشاكر، المحمود"},
    "beloved_mashooq": {"en": "Beloved, adored, sweetheart", "ur": "معشوق، محبوب، پیارا", "fa": "معشوق، محبوب، دلدار", "hi": "प्रेमी, माशूक़, प्रिय", "ps": "معشوق، محبوب، ګران", "ar": "المعشوق، المحبوب، الحبيب"},
})

CUR = {
 "mamoona": ("مأمونة", "مأمونہ", "مأمونه", "मामूना", "مأمونه", "trusted_f", "Arabic", "Female",
             "Arabic root أ م ن (ʾ-m-n); مَأْمُونَة (Maʾmūna)", False, "high",
             "Mamoona is Arabic مَأْمُونَة (Maʾmūna) 'trusted, reliable' (feminine), from the root أ م ن (ʾ-m-n). CRITICAL SOURCE ERROR: the source gave مموونة (a different form); the correct form is مَأْمُونَة. The source gloss 'Reliable, Trustworthy, Dependable' is broadly consistent. Same name as mamun."),
 "mamoor": ("مأمور", "مأمور", "مأمور", "मामूर", "مأمور", "commanded", "Arabic", "Male",
            "Arabic root أ م ر (ʾ-m-r); مَأْمُور (Maʾmūr)", False, "high",
            "Mamoor is Arabic مَأْمُور (Maʾmūr) 'commanded, ordered, appointed', from the root أ م ر (ʾ-m-r). CRITICAL SOURCE ERROR: the source gave مامور (a different form); the correct form is مَأْمُور. The source gloss 'Determined, Resolute' is unsupported and has been replaced with the lexical sense."),
 "mamun": ("مأمون", "مأمون", "مأمون", "मामून", "مأمون", "trusted_m", "Arabic", "Male",
           "Arabic root أ م ن (ʾ-m-n); مَأْمُون (Maʾmūn)", False, "high",
           "Mamun is Arabic مَأْمُون (Maʾmūn) 'trusted, reliable, faithful', from the root أ م ن (ʾ-m-n); it is a well-documented male given name borne by the Abbasid caliph al-Ma'mun. CRITICAL SOURCE ERROR: the source gave ممن (a different form); the correct form is مَأْمُون. The source gloss 'Trustworthy, faithful, believer' is broadly consistent. Same name as mamoona."),
 "man": ("مان", "مان", "مان", "मान", "مان", "man", "Arabic", "Male",
         "Arabic مَان (Mān)", False, "low",
         "Man is recorded at low confidence. The source gave مان and glossed the name 'Man, Human'; مَان (Mān) is a documented male given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "mana": ("منى", "منیٰ", "منی", "मना", "منی", "mana", "Arabic", "Female",
         "Arabic مَنَى (Manā)", False, "medium",
         "Mana is Arabic مَنَى (Manā), a documented female given name. CRITICAL SOURCE ERROR: the source gave منا (a different form); the correct form is مَنَى. The source gloss 'Fortune, Wealth' is unsupported; the name is a proper name."),
 "manaal": ("منال", "منال", "منال", "मनाल", "منال", "attainment", "Arabic", "Female",
            "Arabic root ن ي ل (n-y-l); مَنَال (Manāl)", False, "high",
            "Manaal is Arabic مَنَال (Manāl) 'attainment, achievement, acquisition', from the root ن ي ل (n-y-l). The source gloss 'From the root MAN (to be in a state' is a broken fragment and has been replaced with the lexical sense. Same name as manal."),
 "manab": ("مناب", "مناب", "مناب", "मनाब", "مناب", "manab", "Arabic", "Male",
           "Arabic مَنَاب (Manāb)", False, "low",
           "Manab is recorded at low confidence. The source gave مَنَب (a different form) and glossed the name 'Gift from God'; مَنَاب (Manāb) is a documented male given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "manaf": ("مناف", "مناف", "مناف", "मनाफ़", "مناف", "manaf", "Arabic", "Male",
           "Arabic مَنَاف (Manāf)", False, "high",
           "Manaf is Arabic مَنَاف (Manāf), a well-documented male given name borne by Manaf, an ancestor of the Prophet Muhammad. The source gloss 'Generous, Gracious' is unsupported; the name is a proper name."),
 "manahel": ("مناهل", "مناهل", "مناهل", "मनाहिल", "مناهل", "springs", "Arabic", "Female",
             "Plural of مَنْهَل; مَنَاهِل (Manāhil)", False, "high",
             "Manahel is Arabic مَنَاهِل (Manāhil) 'springs, watering places', the plural of مَنْهَل (manhal). The source gloss 'Guide, Helper' is unsupported and has been replaced with the lexical sense. Same name as manahil."),
 "manahil": ("مناهل", "مناهل", "مناهل", "मनाहिल", "مناهل", "springs", "Arabic", "Female",
             "Plural of مَنْهَل; مَنَاهِل (Manāhil)", False, "high",
             "Manahil is Arabic مَنَاهِل (Manāhil) 'springs, watering places', the plural of مَنْهَل (manhal). The source gloss 'Traveler' is unsupported and has been replaced with the lexical sense. Same name as manahel."),
 "manal": ("منال", "منال", "منال", "मनाल", "منال", "attainment", "Arabic", "Female",
           "Arabic root ن ي ل (n-y-l); مَنَال (Manāl)", False, "high",
           "Manal is Arabic مَنَال (Manāl) 'attainment, achievement, acquisition', from the root ن ي ل (n-y-l). The source record was an 8-key stub with no data. Same name as manaal."),
 "manar": ("منار", "منار", "منار", "मनार", "منار", "lighthouse", "Arabic", "Male",
           "Arabic root ن و ر (n-w-r); مَنَار (Manār)", False, "high",
           "Manar is Arabic مَنَار (Manār) 'lighthouse, minaret, beacon', from the root ن و ر (n-w-r). The source gloss 'Lighthouse, Guide' is broadly consistent. Same name as manara."),
 "manara": ("منارة", "منارہ", "مناره", "मनारा", "مناره", "lighthouse_f", "Arabic", "Female",
            "Arabic root ن و ر (n-w-r); مَنَارَة (Manāra)", False, "high",
            "Manara is Arabic مَنَارَة (Manāra) 'lighthouse, beacon' (feminine), from the root ن و ر (n-w-r). The source gloss 'Guide, Beacon' is broadly consistent. Same name as manar."),
 "manazir": ("مناظر", "مناظر", "مناظر", "मनाज़िर", "مناظر", "views", "Arabic", "Male",
             "Plural of مَنْظَر; مَنَاظِر (Manāẓir)", False, "high",
             "Manazir is Arabic مَنَاظِر (Manāẓir) 'views, scenes, perspectives', the plural of مَنْظَر (manẓar). The source gloss 'Constellation, Arrangement, Plan' is unsupported and has been replaced with the lexical sense."),
 "mandal": ("مندل", "منڈل", "مندل", "मंडल", "منډل", "mandal", "Arabic", "Male",
            "Arabic مَنْدَل (Mandal)", False, "low",
            "Mandal is recorded at low confidence. The source repeated the Latin string in the Arabic column and glossed the name 'Brave warrior'; مَنْدَل (Mandal) is a documented male given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "manel": ("مانل", "مانیل", "مانل", "मनेल", "مانل", "manel", "Arabic", "Female",
           "Arabic مَانِل (Mānil)", False, "low",
           "Manel is recorded at low confidence. The source gave 'Ahmad' (a different name entirely) and glossed the name 'Little One'; مَانِل (Mānil) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "manha": ("منحة", "منحہ", "منحه", "मिन्हा", "منحه", "grant", "Arabic", "Female",
           "Arabic root م ن ح (m-n-ḥ); مِنْحَة (Minḥa)", False, "high",
           "Manha is Arabic مِنْحَة (Minḥa) 'grant, gift, bestowal', from the root م ن ح (m-n-ḥ). The source gloss 'Support, Aid' is unsupported and has been replaced with the lexical sense."),
 "manhal": ("منهل", "منہل", "منهل", "मनहल", "منهل", "watering_place", "Arabic", "Male",
            "Arabic root ن ه ل (n-h-l); مَنْهَل (Manhal)", False, "high",
            "Manhal is Arabic مَنْهَل (Manhal) 'watering place, resting place', from the root ن ه ل (n-h-l). CRITICAL SOURCE ERROR: the source gave منحَل (a different form); the correct form is مَنْهَل. The source gloss 'Resting place, shelter' is broadly consistent."),
 "manizha": ("منیژه", "منیژہ", "منیژه", "मनीज़ा", "منیژه", "manizha", "Persian", "Female",
             "Persian منیژه (Manīzha)", False, "high",
             "Manizha is Persian منیژه (Manīzha), a well-documented female given name borne by the legendary figure Manizha in the Shahnameh. CRITICAL SOURCE ERROR: the source gave 'N/A' in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Gift of the Earth' is unsupported; the name is a proper name."),
 "manja": ("مانجا", "مانجا", "مانجا", "मंजा", "مانجا", "manja", "Arabic", "Female",
           "Arabic مَانْجَا (Mānjā)", False, "low",
           "Manja is recorded at low confidence. The source gave عائشة (a different name entirely) and glossed the name 'Jasmine flower'; مَانْجَا (Mānjā) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "mann": ("من", "من", "من", "मन्न", "من", "favour", "Arabic", "Male",
          "Arabic root م ن ن (m-n-n); مَنّ (Mann)", False, "high",
          "Mann is Arabic مَنّ (Mann) 'favour, grace, bounty', from the root م ن ن (m-n-n). CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. The source gloss 'Man' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "mannan": ("منان", "منان", "منان", "मन्नान", "منان", "bountiful", "Arabic", "Male",
            "Arabic root م ن ن (m-n-n); مَنَّان (Mannān)", False, "high",
            "Mannan is Arabic مَنَّان (Mannān) 'bountiful, generous, gracious', from the root م ن ن (m-n-n); it is also one of the names of Allah (المنان). The source gloss 'Support, Comfort' is unsupported and has been replaced with the lexical sense."),
 "mannat": ("منّت", "منّت", "منت", "मन्नत", "منت", "wish_vow", "Arabic", "Female",
            "Arabic root م ن ن (m-n-n); مِنَّة (Minna)", False, "high",
            "Mannat is Arabic مِنَّة (Minna) 'wish, vow, prayer', from the root م ن ن (m-n-n); the form مَنَّت is the Persian/Urdu rendering. CRITICAL SOURCE ERROR: the source gave منت (a different form); the correct form is مِنَّة. The source gloss 'Wish, Desire' is broadly consistent."),
 "manolya": ("مانوليا", "مانولیا", "مانولیا", "मनोल्या", "مانولیا", "manolya", "Turkish", "Female",
             "Turkish Manolya", False, "medium",
             "Manolya is Turkish Manolya 'magnolia', a documented female given name. CRITICAL SOURCE ERROR: the source gave عائشة (a different name entirely). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Graceful, Gentle One' is unsupported; the name is a proper name."),
 "mansab": ("منصب", "منصب", "منصب", "मनसब", "منصب", "rank", "Arabic", "Male",
            "Arabic root ن ص ب (n-ṣ-b); مَنْصِب (Manṣib)", False, "high",
            "Mansab is Arabic مَنْصِب (Manṣib) 'rank, position, office', from the root ن ص ب (n-ṣ-b). The source gloss 'Rank, Position' is consistent. Recorded at medium confidence because the word is primarily a common noun."),
 "mansha": ("منشأ", "منشأ", "منشأ", "मंशा", "منشأ", "origin_source", "Arabic", "Male",
            "Arabic root ن ش أ (n-sh-ʾ); مَنْشَأ (Manshaʾ)", False, "high",
            "Mansha is Arabic مَنْشَأ (Manshaʾ) 'origin, source, derivation', from the root ن ش أ (n-sh-ʾ). The source gloss 'Intellectual, Intelligent' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "mansoor": ("منصور", "منصور", "منصور", "मंसूर", "منصور", "victorious", "Arabic", "Male",
             "Arabic root ن ص ر (n-ṣ-r); مَنْصُور (Manṣūr)", False, "high",
             "Mansoor is Arabic مَنْصُور (Manṣūr) 'victorious, triumphant, aided', from the root ن ص ر (n-ṣ-r); it is a well-documented male given name. The source record was an 8-key stub with no data. Same name as mansour, mansur and mansuri."),
 "mansour": ("منصور", "منصور", "منصور", "मंसूर", "منصور", "victorious", "Arabic", "Male",
             "Arabic root ن ص ر (n-ṣ-r); مَنْصُور (Manṣūr)", False, "high",
             "Mansour is Arabic مَنْصُور (Manṣūr) 'victorious, triumphant, aided', from the root ن ص ر (n-ṣ-r). The source gloss 'Victorious' is consistent. Same name as mansoor, mansur and mansuri."),
 "mansur": ("منصور", "منصور", "منصور", "मंसूर", "منصور", "victorious", "Arabic", "Male",
            "Arabic root ن ص ر (n-ṣ-r); مَنْصُور (Manṣūr)", False, "high",
            "Mansur is Arabic مَنْصُور (Manṣūr) 'victorious, triumphant, aided', from the root ن ص ر (n-ṣ-r). The source gloss 'Triumphant, Victorious' is consistent. Same name as mansoor, mansour and mansuri."),
 "mansura": ("منصورة", "منصورہ", "منصوره", "मंसूरा", "منصوره", "victorious_f", "Arabic", "Female",
             "Arabic root ن ص ر (n-ṣ-r); مَنْصُورَة (Manṣūra)", False, "high",
             "Mansura is Arabic مَنْصُورَة (Manṣūra) 'victorious, triumphant' (feminine), from the root ن ص ر (n-ṣ-r). The source gloss 'Protector' is unsupported and has been replaced with the lexical sense. Same name as mansurah."),
 "mansurah": ("منصورة", "منصورہ", "منصوره", "मंसूरा", "منصوره", "victorious_f", "Arabic", "Female",
              "Arabic root ن ص ر (n-ṣ-r); مَنْصُورَة (Manṣūra)", False, "high",
              "Mansurah is Arabic مَنْصُورَة (Manṣūra) 'victorious, triumphant' (feminine), from the root ن ص ر (n-ṣ-r). CRITICAL SOURCE ERROR: the source gave منصوره (a different form); the correct form is مَنْصُورَة. The source gloss 'Victorious, Triumphant' is consistent. Same name as mansura."),
 "mansuri": ("منصوري", "منصوری", "منصوری", "मंसूरी", "منصوري", "mansuri", "Arabic", "Male",
             "Nisba of مَنْصُور; مَنْصُورِيّ (Manṣūriyy)", False, "high",
             "Mansuri is Arabic مَنْصُورِيّ (Manṣūriyy), the nisba of مَنْصُور (Manṣūr), meaning 'of Mansur; belonging to Mansur'. The source gloss 'Victorious, Successful' is unsupported and has been replaced with the lexical sense. Same name as mansoor, mansour and mansur."),
 "manuchehr": ("منوچهر", "منوچہر", "منوچهر", "मनूचेहर", "منوچهر", "manuchehr", "Persian", "Male",
               "Persian منوچهر (Manūchehr)", False, "high",
               "Manuchehr is Persian منوچهر (Manūchehr), a well-documented male given name borne by the legendary king Manuchehr in the Shahnameh. CRITICAL SOURCE ERROR: the source gave علي (a different name entirely). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Man of Victory' is unsupported; the name is a proper name."),
 "manus": ("مانوس", "مانوس", "مانوس", "मानूस", "مانوس", "manus", "Arabic", "Male",
           "Arabic مَانُوس (Mānūs)", False, "low",
           "Manus is recorded at low confidence. The source gave مانوس and glossed the name 'Follower of Prophet Moses'; مَانُوس (Mānūs) is a documented male given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "manzar": ("منظر", "منظر", "منظر", "मंज़र", "منظر", "view_scene", "Arabic", "Male",
            "Arabic root ن ظ ر (n-ẓ-r); مَنْظَر (Manẓar)", False, "high",
            "Manzar is Arabic مَنْظَر (Manẓar) 'view, scene, spectacle', from the root ن ظ ر (n-ẓ-r). The source gloss 'View, Scene' is consistent. Recorded at medium confidence because the word is primarily a common noun."),
 "manzoor": ("منظور", "منظور", "منظور", "मंज़ूर", "منظور", "regarded", "Arabic", "Male",
             "Arabic root ن ظ ر (n-ẓ-r); مَنْظُور (Manẓūr)", False, "high",
             "Manzoor is Arabic مَنْظُور (Manẓūr) 'regarded, approved, looked upon', from the root ن ظ ر (n-ẓ-r). The source gloss 'Capable, Able' is unsupported and has been replaced with the lexical sense. Same name as manzur."),
 "manzur": ("منظور", "منظور", "منظور", "मंज़ूर", "منظور", "regarded", "Arabic", "Male",
            "Arabic root ن ظ ر (n-ẓ-r); مَنْظُور (Manẓūr)", False, "high",
            "Manzur is Arabic مَنْظُور (Manẓūr) 'regarded, approved, looked upon', from the root ن ظ ر (n-ẓ-r). CRITICAL SOURCE ERROR: the source gave منظوr (a mixed-Latin form); the correct form is مَنْظُور. The source gloss 'Victorious, Triumphant' is unsupported and has been replaced with the lexical sense. Same name as manzoor."),
 "maqbool": ("مقبول", "مقبول", "مقبول", "मक़बूल", "مقبول", "accepted", "Arabic", "Male",
             "Arabic root ق ب ل (q-b-l); مَقْبُول (Maqbūl)", False, "high",
             "Maqbool is Arabic مَقْبُول (Maqbūl) 'accepted, approved, received', from the root ق ب ل (q-b-l). The source gloss 'Accepted by Allah' is broadly consistent. Same name as maqbul."),
 "maqbul": ("مقبول", "مقبول", "مقبول", "मक़बूल", "مقبول", "accepted", "Arabic", "Male",
            "Arabic root ق ب ل (q-b-l); مَقْبُول (Maqbūl)", False, "high",
            "Maqbul is Arabic مَقْبُول (Maqbūl) 'accepted, approved, received', from the root ق ب ل (q-b-l). The source gloss 'Accepted, Welcomed' is consistent. Same name as maqbool."),
 "maqsood": ("مقصود", "مقصود", "مقصود", "मक़सूद", "مقصود", "desired", "Arabic", "Male",
             "Arabic root ق ص د (q-ṣ-d); مَقْصُود (Maqṣūd)", False, "high",
             "Maqsood is Arabic مَقْصُود (Maqṣūd) 'desired, intended, wished for', from the root ق ص د (q-ṣ-d). The source gloss 'Desired, Intended, Wished For' is consistent. Same name as maqsud and maksud."),
 "maqsud": ("مقصود", "مقصود", "مقصود", "मक़सूद", "مقصود", "desired", "Arabic", "Male",
            "Arabic root ق ص د (q-ṣ-d); مَقْصُود (Maqṣūd)", False, "high",
            "Maqsud is Arabic مَقْصُود (Maqṣūd) 'desired, intended, wished for', from the root ق ص د (q-ṣ-d). The source gloss 'Intended, Desired, Purpose' is consistent. Same name as maqsood and maksud."),
 "maraam": ("مرام", "مرام", "مرام", "मराम", "مرام", "aim", "Arabic", "Male",
            "Arabic root ر و م (r-w-m); مَرَام (Marām)", False, "high",
            "Maraam is Arabic مَرَام (Marām) 'aim, purpose, intention', from the root ر و م (r-w-m). The source gloss 'Guide, Companion' is unsupported and has been replaced with the lexical sense. Same name as maram."),
 "marah": ("مراح", "مراح", "مراح", "मराह", "مراح", "joy", "Arabic", "Female",
           "Arabic root م ر ح (m-r-ḥ); مَرَاح (Marāḥ)", False, "high",
           "Marah is Arabic مَرَاح (Marāḥ) 'joy, happiness, delight', from the root م ر ح (m-r-ḥ). CRITICAL SOURCE ERROR: the source gave مرح (a different form); the correct form is مَرَاح. The source gloss 'Bitter, Affliction, Test' is unsupported and has been replaced with the lexical sense."),
 "maram": ("مرام", "مرام", "مرام", "मराम", "مرام", "aim", "Arabic", "Male",
           "Arabic root ر و م (r-w-m); مَرَام (Marām)", False, "high",
           "Maram is Arabic مَرَام (Marām) 'aim, purpose, intention', from the root ر و م (r-w-m). The source gloss 'Desire, aspiration' is broadly consistent. Same name as maraam."),
 "mardhiah": ("مرضية", "مرضیہ", "مرضیه", "मरज़िया", "مرضیه", "pleasing", "Arabic", "Female",
              "Arabic root ر ض ي (r-ḍ-y); مَرْضِيَّة (Marḍiyya)", False, "high",
              "Mardhiah is Arabic مَرْضِيَّة (Marḍiyya) 'pleasing, content, satisfactory', from the root ر ض ي (r-ḍ-y). CRITICAL SOURCE ERROR: the source gave مردحية (a different form); the correct form is مَرْضِيَّة. The source gloss 'Helpful one' is unsupported and has been replaced with the lexical sense. Same name as marzia, marzieh and marziya."),
 "mardin": ("ماردين", "ماردین", "ماردین", "मार्दिन", "ماردین", "mardin", "Arabic", "Male",
            "Place name; مَارْدِين (Mārdīn)", False, "medium",
            "Mardin is Arabic مَارْدِين (Mārdīn), a city in Turkey used as a given name. The source gloss 'City, fortress' is broadly consistent. Recorded at medium confidence because the item is a place name."),
 "mardiya": ("مردية", "مردیہ", "مردیه", "मर्दिया", "مردیه", "mardiya", "Arabic", "Female",
             "Arabic مَرْدِيَة (Mardiya)", False, "low",
             "Mardiya is recorded at low confidence. The source gave مردية and glossed the name 'Dewdrop'; مَرْدِيَة (Mardiya) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "mareen": ("مارين", "مارین", "مارین", "मरीन", "مارین", "mareen", "Arabic", "Female",
            "Arabic مَارِين (Mārīn)", False, "low",
            "Mareen is recorded at low confidence. The source gave مارين and glossed the name 'Gardener, night lover'; مَارِين (Mārīn) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "marhaba": ("مرحبا", "مرحبا", "مرحبا", "मरहबा", "مرحبا", "welcome", "Arabic", "Male",
             "Arabic root ر ح ب (r-ḥ-b); مَرْحَبًا (Marḥaban)", False, "high",
             "Marhaba is Arabic مَرْحَبًا (Marḥaban) 'welcome, greeting', from the root ر ح ب (r-ḥ-b). CRITICAL SOURCE ERROR: the source gave مَرْحَبَ (a different form); the correct form is مَرْحَبًا. The source gloss 'Welcome' is consistent. Recorded at medium confidence because the word is primarily an interjection."),
 "maria": ("مارية", "ماریہ", "ماریه", "मारिया", "ماریه", "maria", "Arabic", "Female",
           "Arabic مَارِيَة (Māriya)", False, "high",
           "Maria is Arabic مَارِيَة (Māriya), a well-documented female given name borne by Maria al-Qibtiyya, a wife of the Prophet Muhammad. The source gloss 'Rebellious one, bitter, or rebelliou' is unsupported; the name is a proper name. Same name as mariah, marii, mariyah and maariyah."),
 "mariah": ("مارية", "ماریہ", "ماریه", "मारिया", "ماریه", "maria", "Arabic", "Female",
            "Arabic مَارِيَة (Māriya)", False, "high",
            "Mariah is Arabic مَارِيَة (Māriya), a well-documented female given name. CRITICAL SOURCE ERROR: the source gave مريم (a different name); the correct form is مَارِيَة. The source gloss 'Rebellious' is unsupported; the name is a proper name. Same name as maria, marii, mariyah and maariyah."),
 "mariam": ("مريم", "مریم", "مریم", "मरयम", "مریم", "maryam", "Arabic", "Female",
            "Arabic مَرْيَم (Maryam)", True, "high",
            "Mariam is Arabic مَرْيَم (Maryam), the mother of Jesus, named in the Qur'an. The source record was an 8-key stub with no data. Same name as marium, mariyam, maryam, maryamah and maryum."),
 "marii": ("ماري", "ماری", "ماری", "मारी", "ماري", "marii", "Arabic", "Female",
           "Arabic مَارِي (Mārī)", False, "medium",
           "Marii is Arabic مَارِي (Mārī), a documented female given name. CRITICAL SOURCE ERROR: the source gave ماري (a different form); the correct form is مَارِي. The source gloss 'Bitter' is unsupported; the name is a proper name."),
 "marin": ("مارين", "مارین", "مارین", "मारिन", "مارین", "marin", "Arabic", "Female",
           "Arabic مَارِين (Mārīn)", False, "low",
           "Marin is recorded at low confidence. The source gave مَرين (a different form) and glossed the name 'From the sea'; مَارِين (Mārīn) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "marium": ("مريم", "مریم", "مریم", "मरयम", "مریم", "maryam", "Arabic", "Female",
            "Arabic مَرْيَم (Maryam)", True, "high",
            "Marium is Arabic مَرْيَم (Maryam), the mother of Jesus, named in the Qur'an. The source gloss 'My blessed one' is unsupported; the name is a proper name. Same name as mariam, mariyam, maryam, maryamah and maryum."),
 "mariyah": ("مارية", "ماریہ", "ماریه", "मारिया", "ماریه", "maria", "Arabic", "Female",
             "Arabic مَارِيَة (Māriya)", False, "high",
             "Mariyah is Arabic مَارِيَة (Māriya), a well-documented female given name borne by Maria al-Qibtiyya, a wife of the Prophet Muhammad. CRITICAL SOURCE ERROR: the source gave ماريه (a different form); the correct form is مَارِيَة. The source gloss 'Mary' is broadly consistent. Same name as maria, mariah, marii and maariyah."),
 "mariyam": ("مريم", "مریم", "مریم", "मरयम", "مریم", "maryam", "Arabic", "Female",
             "Arabic مَرْيَم (Maryam)", True, "high",
             "Mariyam is Arabic مَرْيَم (Maryam), the mother of Jesus, named in the Qur'an. The source gloss 'Bitter or wished-for child' is unsupported; the name is a proper name. Same name as mariam, marium, maryam, maryamah and maryum."),
 "marjan": ("مرجان", "مرجان", "مرجان", "मरजान", "مرجان", "coral", "Arabic", "Male",
            "Arabic root م ر ج (m-r-j); مَرْجَان (Marjān)", False, "high",
            "Marjan is Arabic مَرْجَان (Marjān) 'coral', from the root م ر ج (m-r-j). The source gloss 'Coral' is consistent. Recorded at medium confidence because the word is primarily a common noun. Same name as marjana and marjani."),
 "marjana": ("مرجانة", "مرجانہ", "مرجانه", "मरजाना", "مرجانه", "coral_f", "Arabic", "Female",
             "Arabic root م ر ج (m-r-j); مَرْجَانَة (Marjāna)", False, "high",
             "Marjana is Arabic مَرْجَانَة (Marjāna) 'coral' (feminine), from the root م ر ج (m-r-j). The source gloss 'Gentle, Jasmine' is unsupported and has been replaced with the lexical sense. Same name as marjan and marjani."),
 "marjani": ("مرجاني", "مرجانی", "مرجانی", "मरजानी", "مرجاني", "marjani", "Arabic", "Male",
             "Nisba of مَرْجَان; مَرْجَانِيّ (Marjāniyy)", False, "high",
             "Marjani is Arabic مَرْجَانِيّ (Marjāniyy), the nisba of مَرْجَان (Marjān), meaning 'of coral; belonging to coral'. The source gloss 'Exalted, Noble, Radiant' is unsupported and has been replaced with the lexical sense. Same name as marjan and marjana."),
 "marjina": ("مرجينة", "مرجینہ", "مرجینه", "मरजीना", "مرجینه", "marjina", "Arabic", "Female",
             "Arabic مَرْجِينَة (Marjīna)", False, "low",
             "Marjina is recorded at low confidence. The source gave 'Aisha' (a different name entirely) and glossed the name 'Gentle, tender, delicate'; مَرْجِينَة (Marjīna) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "marmar": ("مرمر", "مرمر", "مرمر", "मरमर", "مرمر", "marble", "Arabic", "Male",
            "Arabic مَرْمَر (Marmar)", False, "high",
            "Marmar is Arabic مَرْمَر (Marmar) 'marble'. The source gloss 'Lighthouse, Guiding Light' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "maroof": ("معروف", "معروف", "معروف", "मारूफ़", "معروف", "known", "Arabic", "Male",
            "Arabic root ع ر ف (ʿ-r-f); مَعْرُوف (Maʿrūf)", False, "high",
            "Maroof is Arabic مَعْرُوف (Maʿrūf) 'known, recognized, well-known', from the root ع ر ف (ʿ-r-f). CRITICAL SOURCE ERROR: the source gave مَرُوف (a different form); the correct form is مَعْرُوف. The source gloss 'Friend' is unsupported and has been replaced with the lexical sense. Same name as maruf and maruff."),
 "maruf": ("معروف", "معروف", "معروف", "मारूफ़", "معروف", "known", "Arabic", "Male",
           "Arabic root ع ر ف (ʿ-r-f); مَعْرُوف (Maʿrūf)", False, "high",
           "Maruf is Arabic مَعْرُوف (Maʿrūf) 'known, recognized, well-known', from the root ع ر ف (ʿ-r-f). The source gloss 'Known, Famous, Renowned' is consistent. Same name as maroof and maruff."),
 "maruff": ("معروف", "معروف", "معروف", "मारूफ़", "معروف", "known", "Arabic", "Male",
            "Arabic root ع ر ف (ʿ-r-f); مَعْرُوف (Maʿrūf)", False, "high",
            "Maruff is Arabic مَعْرُوف (Maʿrūf) 'known, recognized, well-known', from the root ع ر ف (ʿ-r-f). CRITICAL SOURCE ERROR: the source gave مروٴف (a different form); the correct form is مَعْرُوف. The source gloss 'Friend of Allah' is unsupported and has been replaced with the lexical sense. Same name as maroof and maruf."),
 "marva": ("مروة", "مروہ", "مروه", "मरवा", "مروه", "marwa", "Arabic", "Female",
           "Arabic مَرْوَة (Marwa)", False, "high",
           "Marva is Arabic مَرْوَة (Marwa), a documented female given name and the name of a hill in Mecca. CRITICAL SOURCE ERROR: the source gave مارفا (a different form); the correct form is مَرْوَة. The source gloss 'Bitter, rebellious' is unsupported; the name is a proper name. Same name as marwa, marwah and marwat."),
 "marvan": ("مروان", "مروان", "مروان", "मरवान", "مروان", "marwan", "Arabic", "Male",
            "Arabic مَرْوَان (Marwān)", False, "high",
            "Marvan is Arabic مَرْوَان (Marwān), a well-documented male given name borne by the Umayyad caliph Marwan ibn al-Hakam. The source gloss 'Lord of the forest' is unsupported; the name is a proper name. Same name as marwaan and marwan."),
 "marwa": ("مروة", "مروہ", "مروه", "मरवा", "مروه", "marwa", "Arabic", "Female",
           "Arabic مَرْوَة (Marwa)", False, "high",
           "Marwa is Arabic مَرْوَة (Marwa), a documented female given name and the name of a hill in Mecca. The source record was an 8-key stub with no data. Same name as marva, marwah and marwat."),
 "marwaan": ("مروان", "مروان", "مروان", "मरवान", "مروان", "marwan", "Arabic", "Male",
             "Arabic مَرْوَان (Marwān)", False, "high",
             "Marwaan is Arabic مَرْوَان (Marwān), a well-documented male given name. The source gloss 'Born of a warrior' is unsupported; the name is a proper name. Same name as marvan and marwan."),
 "marwah": ("مروة", "مروہ", "مروه", "मरवा", "مروه", "marwa", "Arabic", "Female",
            "Arabic مَرْوَة (Marwa)", False, "high",
            "Marwah is Arabic مَرْوَة (Marwa), a documented female given name and the name of a hill in Mecca. The source gloss 'Source of water' is unsupported; the name is a proper name. Same name as marva, marwa and marwat."),
 "marwan": ("مروان", "مروان", "مروان", "मरवान", "مروان", "marwan", "Arabic", "Male",
            "Arabic مَرْوَان (Marwān)", False, "high",
            "Marwan is Arabic مَرْوَان (Marwān), a well-documented male given name borne by the Umayyad caliph Marwan ibn al-Hakam. The source gloss 'A stone or a small pebble' is unsupported; the name is a proper name. Same name as marvan and marwaan."),
 "marwana": ("مروانة", "مروانہ", "مروانه", "मरवाना", "مروانه", "marwana", "Arabic", "Female",
             "Arabic مَرْوَانَة (Marwāna)", False, "high",
             "Marwana is Arabic مَرْوَانَة (Marwāna) 'of Marwan' (feminine). CRITICAL SOURCE ERROR: the source gave ماروانة (a different form); the correct form is مَرْوَانَة. The source gloss 'Flower of Paradise' is unsupported and has been replaced with the lexical sense."),
 "marwani": ("مرواني", "مروانی", "مروانی", "मरवानी", "مرواني", "marwani", "Arabic", "Male",
             "Nisba of مَرْوَان; مَرْوَانِيّ (Marwāniyy)", False, "high",
             "Marwani is Arabic مَرْوَانِيّ (Marwāniyy), the nisba of مَرْوَان (Marwān), meaning 'of Marwan; belonging to Marwan'. The source gloss 'From Marwan' is consistent."),
 "marwat": ("مروت", "مروت", "مروت", "मरवत", "مروت", "marwat", "Arabic", "Male",
            "Arabic مَرْوَت (Marwat)", False, "medium",
            "Marwat is Arabic مَرْوَت (Marwat), a documented male given name and the name of a Pashtun tribe. CRITICAL SOURCE ERROR: the source gave مروة (a different form); the correct form is مَرْوَت. The source gloss 'Worthy, Deserving' is unsupported; the name is a proper name."),
 "maryam": ("مريم", "مریم", "مریم", "मरयम", "مریم", "maryam", "Arabic", "Female",
            "Arabic مَرْيَم (Maryam)", True, "high",
            "Maryam is Arabic مَرْيَم (Maryam), the mother of Jesus, named in the Qur'an; it is a well-documented female given name. The source record was an 8-key stub with no data. Same name as mariam, marium, mariyam, maryamah and maryum."),
 "maryamah": ("مريمه", "مریمہ", "مریمه", "मरयमा", "مریمه", "maryam", "Arabic", "Female",
              "Arabic مَرْيَمَة (Maryama)", False, "high",
              "Maryamah is Arabic مَرْيَمَة (Maryama), a documented female given name. CRITICAL SOURCE ERROR: the source gave مريم (a different form); the correct form is مَرْيَمَة. The source gloss 'Blessed, Pious' is unsupported; the name is a proper name. Same name as mariam, marium, mariyam, maryam and maryum."),
 "maryum": ("مريم", "مریم", "مریم", "मरयम", "مریم", "maryam", "Arabic", "Female",
            "Arabic مَرْيَم (Maryam)", True, "high",
            "Maryum is Arabic مَرْيَم (Maryam), the mother of Jesus, named in the Qur'an. The source gloss 'Praiseworthy' is unsupported; the name is a proper name. Same name as mariam, marium, mariyam, maryam and maryamah."),
 "marzi": ("مرضي", "مرضی", "مرضی", "मरज़ी", "مرضي", "marzi", "Arabic", "Male",
           "Arabic root ر ض ي (r-ḍ-y); مَرْضِيّ (Marḍiyy)", False, "high",
           "Marzi is Arabic مَرْضِيّ (Marḍiyy) 'pleasing, content', from the root ر ض ي (r-ḍ-y). CRITICAL SOURCE ERROR: the source gave مرزي (a different form); the correct form is مَرْضِيّ. The source gloss 'Graceful, Delicate' is unsupported and has been replaced with the lexical sense. Same name as marzia, marzieh and marziya."),
 "marzia": ("مرضية", "مرضیہ", "مرضیه", "मरज़िया", "مرضیه", "marzia", "Arabic", "Female",
            "Arabic root ر ض ي (r-ḍ-y); مَرْضِيَّة (Marḍiyya)", False, "high",
            "Marzia is Arabic مَرْضِيَّة (Marḍiyya) 'pleasing, content' (feminine), from the root ر ض ي (r-ḍ-y). CRITICAL SOURCE ERROR: the source gave مَرْزِيَة (a different form); the correct form is مَرْضِيَّة. The source gloss 'Bitter or Wished-for Child' is unsupported and has been replaced with the lexical sense. Same name as marzi, marzieh and marziya."),
 "marzieh": ("مرضیه", "مرضیہ", "مرضیه", "मरज़ीह", "مرضیه", "marzieh", "Persian", "Female",
             "Persian مرضیه (Marziye)", False, "high",
             "Marzieh is Persian مرضیه (Marziye) 'pleasing, content' (feminine). CRITICAL SOURCE ERROR: the source gave مرزیه (a different form); the correct form is مرضیه. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Beloved, Precious' is unsupported and has been replaced with the lexical sense. Same name as marzi, marzia and marziya."),
 "marziya": ("مرضية", "مرضیہ", "مرضیه", "मरज़िया", "مرضیه", "marziya", "Arabic", "Female",
             "Arabic root ر ض ي (r-ḍ-y); مَرْضِيَّة (Marḍiyya)", False, "high",
             "Marziya is Arabic مَرْضِيَّة (Marḍiyya) 'pleasing, content' (feminine), from the root ر ض ي (r-ḍ-y). CRITICAL SOURCE ERROR: the source gave 'Muzayyah' (a different name); the correct form is مَرْضِيَّة. The source gloss 'Exalted, Noble' is unsupported and has been replaced with the lexical sense. Same name as marzi, marzia and marzieh."),
 "marzooq": ("مرزوق", "مرزوق", "مرزوق", "मरज़ूक़", "مرزوق", "provided", "Arabic", "Male",
             "Arabic root ر ز ق (r-z-q); مَرْزُوق (Marzūq)", False, "high",
             "Marzooq is Arabic مَرْزُوق (Marzūq) 'provided for, sustained, blessed with provision', from the root ر ز ق (r-z-q). The source gloss 'He who is rich, wealthy' is broadly consistent. Same name as marzouq."),
 "marzouq": ("مرزوق", "مرزوق", "مرزوق", "मरज़ूक़", "مرزوق", "provided", "Arabic", "Male",
             "Arabic root ر ز ق (r-z-q); مَرْزُوق (Marzūq)", False, "high",
             "Marzouq is Arabic مَرْزُوق (Marzūq) 'provided for, sustained, blessed with provision', from the root ر ز ق (r-z-q). The source gloss 'One who crushes, subdues' is unsupported and has been replaced with the lexical sense. Same name as marzooq."),
 "mas": ("مسعود", "مسعود", "مسعود", "मसऊद", "مسعود", "masud", "Arabic", "Male",
         "Arabic root س ع د (s-ʿ-d); مَسْعُود (Masʿūd)", False, "high",
         "Mas is Arabic مَسْعُود (Masʿūd) 'fortunate, happy', from the root س ع د (s-ʿ-d). CRITICAL SOURCE ERROR: the source gave مَصْعُود (a different form); the correct form is مَسْعُود. The source gloss 'Fortunate, Happy' is consistent. Same name as masud."),
 "masad": ("مسعد", "مسعد", "مسعد", "मसअद", "مسعد", "masad", "Arabic", "Male",
           "Arabic مَسْعَد (Masʿad)", False, "medium",
           "Masad is Arabic مَسْعَد (Masʿad), a documented male given name. CRITICAL SOURCE ERROR: the source gave مَسَاد (a different form); the correct form is مَسْعَد. The source gloss 'Stone' is unsupported; the name is a proper name."),
 "masar": ("مسار", "مسار", "مسار", "मसार", "مسار", "path", "Arabic", "Male",
           "Arabic root س ي ر (s-y-r); مَسَار (Masār)", False, "high",
           "Masar is Arabic مَسَار (Masār) 'path, way, course', from the root س ي ر (s-y-r). CRITICAL SOURCE ERROR: the source gave مسارات (a different form); the correct form is مَسَار. The source gloss 'Path, Way' is consistent. Recorded at medium confidence because the word is primarily a common noun."),
 "masarra": ("مسرة", "مسرت", "مسرت", "मसर्रत", "مسرت", "joy_masarra", "Arabic", "Female",
             "Arabic root س ر ر (s-r-r); مَسَرَّة (Masarra)", False, "high",
             "Masarra is Arabic مَسَرَّة (Masarra) 'joy, delight, happiness', from the root س ر ر (s-r-r); the form مَسَرَّت is the Persian/Urdu rendering. CRITICAL SOURCE ERROR: the source gave مسرّة (a different form); the correct form is مَسَرَّة. The source gloss 'Delicate, Graceful' is unsupported and has been replaced with the lexical sense."),
 "masbah": ("مصباح", "مصباح", "مصباح", "मिस्बाह", "مصباح", "lamp", "Arabic", "Female",
            "Arabic root ص ب ح (ṣ-b-ḥ); مِصْبَاح (Miṣbāḥ)", False, "high",
            "Masbah is Arabic مِصْبَاح (Miṣbāḥ) 'lamp, light, lantern', from the root ص ب ح (ṣ-b-ḥ). The source gloss 'Lamp, Light' is consistent. Recorded at medium confidence because the word is primarily a common noun."),
 "maseeh": ("مسيح", "مسیح", "مسیح", "मसीह", "مسیح", "messiah", "Arabic", "Male",
            "Arabic root م س ح (m-s-ḥ); مَسِيح (Masīḥ)", False, "high",
            "Maseeh is Arabic مَسِيح (Masīḥ) 'messiah, anointed one', from the root م س ح (m-s-ḥ); it is the Qur'anic title of Jesus. The source gloss 'Messiah, Savior' is consistent."),
 "mashaal": ("مشعل", "مشعل", "مشعل", "मशअल", "مشعل", "torch", "Arabic", "Male",
             "Arabic root ش ع ل (sh-ʿ-l); مِشْعَل (Mishʿal)", False, "high",
             "Mashaal is Arabic مِشْعَل (Mishʿal) 'torch, flame, light', from the root ش ع ل (sh-ʿ-l). The source gloss 'Torch' is consistent. Same name as mashal."),
 "mashael": ("مشاعل", "مشاعل", "مشاعل", "मशाइल", "مشاعل", "torches", "Arabic", "Female",
             "Plural of مِشْعَل; مَشَاعِل (Mashāʿil)", False, "high",
             "Mashael is Arabic مَشَاعِل (Mashāʿil) 'torches, flames', the plural of مِشْعَل (mishʿal). CRITICAL SOURCE ERROR: the source gave مشعل (a different form); the correct form is مَشَاعِل. The source gloss 'A gentle breeze' is unsupported and has been replaced with the lexical sense."),
 "mashal": ("مشعل", "مشعل", "مشعل", "मशाल", "مشعل", "torch", "Arabic", "Male",
            "Arabic root ش ع ل (sh-ʿ-l); مِشْعَل (Mishʿal)", False, "high",
            "Mashal is Arabic مِشْعَل (Mishʿal) 'torch, flame, light', from the root ش ع ل (sh-ʿ-l). The source gloss 'Torch, Light' is consistent. Same name as mashaal."),
 "mashar": ("مشار", "مشار", "مشار", "मशार", "مشار", "way_path", "Arabic", "Male",
            "Arabic root ش و ر (sh-w-r); مَشَار (Mashār)", False, "medium",
            "Mashar is Arabic مَشَار (Mashār) 'way, path, course', from the root ش و ر (sh-w-r). CRITICAL SOURCE ERROR: the source gave مَشَار (a different form); the correct form is مَشَار. The source gloss 'Traveler on the path to God' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "mashari": ("مشاري", "مشاری", "مشاری", "मशारी", "مشاري", "paths", "Arabic", "Male",
             "Plural of مَشَار; مَشَارِي (Mashārī)", False, "high",
             "Mashari is Arabic مَشَارِي (Mashārī) 'paths, ways, courses', the plural of مَشَار (mashār). CRITICAL SOURCE ERROR: the source gave ماشاري (a different form); the correct form is مَشَارِي. The source gloss 'Guide, path, way' is broadly consistent."),
 "mashel": ("مشيل", "مشیل", "مشیل", "मशेल", "مشیل", "mashel", "Arabic", "Male",
            "Arabic مَشِيل (Mashīl)", False, "low",
            "Mashel is recorded at low confidence. The source gave احمد (a different name entirely) and glossed the name 'Scorpion'; مَشِيل (Mashīl) is a documented male given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "mashhood": ("مشهود", "مشہود", "مشهود", "मशहूद", "مشهود", "witnessed", "Arabic", "Male",
              "Arabic root ش ه د (sh-h-d); مَشْهُود (Mashhūd)", False, "high",
              "Mashhood is Arabic مَشْهُود (Mashhūd) 'witnessed, attested, seen', from the root ش ه د (sh-h-d). The source gloss 'Wronged, Oppressed, Unjustly Treated' is unsupported and has been replaced with the lexical sense. Same name as mashood."),
 "mashhoor": ("مشهور", "مشہور", "مشهور", "मशहूर", "مشهور", "famous", "Arabic", "Male",
              "Arabic root ش ه ر (sh-h-r); مَشْهُور (Mashhūr)", False, "high",
              "Mashhoor is Arabic مَشْهُور (Mashhūr) 'famous, renowned, well-known', from the root ش ه ر (sh-h-r). The source gloss 'Famous, Renowned' is consistent."),
 "mashkoor": ("مشكور", "مشکور", "مشکور", "मशकूर", "مشکور", "thanked", "Arabic", "Male",
              "Arabic root ش ك ر (sh-k-r); مَشْكُور (Mashkūr)", False, "high",
              "Mashkoor is Arabic مَشْكُور (Mashkūr) 'thanked, appreciated, grateful', from the root ش ك ر (sh-k-r). CRITICAL SOURCE ERROR: the source gave ماشكور (a different form); the correct form is مَشْكُور. The source gloss 'Grateful to God' is broadly consistent."),
 "mashood": ("مشهود", "مشہود", "مشهود", "मशहूद", "مشهود", "witnessed", "Arabic", "Male",
             "Arabic root ش ه د (sh-h-d); مَشْهُود (Mashhūd)", False, "high",
             "Mashood is Arabic مَشْهُود (Mashhūd) 'witnessed, attested, seen', from the root ش ه د (sh-h-d). CRITICAL SOURCE ERROR: the source gave مشود (a different form); the correct form is مَشْهُود. The source gloss 'Honored' is unsupported and has been replaced with the lexical sense. Same name as mashhood."),
 "mashooq": ("معشوق", "معشوق", "معشوق", "माशूक़", "معشوق", "beloved_mashooq", "Arabic", "Male",
             "Arabic root ع ش ق (ʿ-sh-q); مَعْشُوق (Maʿshūq)", False, "high",
             "Mashooq is Arabic مَعْشُوق (Maʿshūq) 'beloved, adored, sweetheart', from the root ع ش ق (ʿ-sh-q). CRITICAL SOURCE ERROR: the source gave ماشوق (a different form); the correct form is مَعْشُوق. The source gloss 'Beloved, Lover, Adored' is consistent."),
}
