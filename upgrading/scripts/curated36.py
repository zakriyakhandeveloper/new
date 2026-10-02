# -*- coding: utf-8 -*-
"""Curated, confidence-graded knowledge table for the islamic batch 36 (khursheed..liban).

Source defects found in this batch:
 * WRONG / PLACEHOLDER "Arabic forms": kiana -> "Kiana" (Latin); kimia ->
   "Kimia" (Latin); kiram -> "Kiram" (Latin); kobra -> "Kobra" (Latin);
   kourosh -> "Kourosh" (Latin); labid -> "Labid" (Latin); landa -> "Landa"
   (Latin); layana -> "Layana" (Latin); laila -> "عربي_Laila" (junk);
   lara -> "عربي_Lara" (junk); laiq -> "ﷲ...ق" (broken junk); laal -> عائشة
   (a different name entirely); lala -> عائشة (a different name entirely);
   liba -> عائشة (a different name entirely); lathif -> لثيف (should be لطيف);
   lais -> لَيْس (should be ليث); lema -> لماء (should be لمى); lazzat ->
   لزّات (should be لذة); kudrat -> كدرت (should be قدرت); komal -> كمال
   (should be کومل); lakhwinder -> لقويندر (should be لکھوندر); kishwar ->
   كيشوار (should be کشور); kohinoor -> كوهينور (should be کوہ نور);
   khushbu -> خوشبو (Persian letters); khursheed/khurshid -> خورشيد (Persian
   letters); khyber -> خيبَر (broken); kibria -> كِبْرِيَا (broken);
   kinana -> كنَانة (broken); kutaiba -> كوتيبة (should be كتيبة);
   lamiya/lamya/lamyaa -> لمياء (ok); layal -> ليال (ok).
 * DEGARBLED / WRONG glosses: khursheed 'Radiant, shining moon' (should be
   'sun'); khurshid 'Bringer of Light' (should be 'sun'); khushbu 'Scent,
   Fragrance' (correct); khuzama 'Protector, Guardian' (unsupported);
   khwaja 'Title of respect' (should be 'master'); khyber 'Passage, mountain
   pass' (should be the place name Khaybar); kiana 'Born of the sky'
   (unsupported); kibria 'Lady, Noblewoman' (should be 'grandeur');
   kibriya 'The one who is small but mighty' (should be 'grandeur, pride');
   kifah 'Struggle, Effort, Battle' (correct); kifayah 'Sufficient' (should be
   'sufficiency'); kifayat 'Sufficient' (should be 'sufficiency'); kiki
   'Rejoice, be happy' (unsupported); kimia 'Alchemy, Transmutation' (correct);
   kinan 'Descendant of a priest' (unsupported); kinana 'Mature, Intelligent'
   (should be the name Kinana); kinza 'Treasure, Hidden Blessing' (should be
   'treasure'); kiram 'Precious gem' (should be 'noble, generous (plural)');
   kirana 'Ray of Light' (unsupported); kisa 'Little One' (should be
   'garment'); kishwar "God's gift" (should be 'country', Persian); kitab
   'The Book' (correct); kobra 'Venomous serpent' (should be 'great (fem)',
   Persian); kohinoor 'Diamond, Precious Stone' (should be 'mountain of
   light'); kohl 'Charcoal' (should be 'kohl, antimony'); kokab 'Star'
   (correct); komal 'Sweetness, tenderness' (should be 'soft, tender');
   komila 'Gentle, Beautiful' (unsupported); koosha 'Happy, Joyful' (should be
   'diligent', Persian); kourosh 'Sun Face' (should be the name Cyrus);
   kubra 'Great, honorable, noble' (should be 'great (fem)'); kudrat 'Power,
   Might, Strength' (correct); kulsoom 'Companion, Friend' (should be the name
   Kulthum); kulsum 'Pleasant, Sweet' (should be the name Kulthum); kumail
   'Universe, Cosmos, Perfect' (should be the name Kumayl); kunya 'Nickname'
   (should be 'patronymic'); kutaiba 'Warrior' (should be the name Kutayba);
   kutub 'Repository of Knowledge' (should be 'books'); laal 'Night' (should
   be 'ruby'); labeeb 'Intimate, Close to heart' (should be 'intelligent');
   labib 'Heart, Love' (should be 'intelligent'); labiba 'The Sweet One'
   (should be 'intelligent (fem)'); labid 'Devoted' (should be the name
   Labid); ladan 'Gentle Wave' (unsupported); laeeq 'Gift' (should be 'worthy,
   fit'); laiba 'Angel of Heaven' (unsupported); laiha 'Subtle, delicate,
   tender' (unsupported); laila 'Noble and blessed' (should be the name
   Layla); laima 'Beautiful Pearl' (unsupported); laiq 'Easy, Light' (should
   be 'worthy, fit'); lais 'A night light' (should be 'lion'); laith 'Radiant,
   guide' (should be 'lion'); lakhwinder 'Compassionate' (unsupported);
   lakia 'Pure, innocent, beautiful' (unsupported); lal 'Night' (should be
   'ruby'); lala 'Nurse, Protector' (unsupported); lama 'Unknown' (should be
   the name Lama); lamees 'Graceful, elegant' (should be the name Lamees);
   lami 'Small or delicate' (unsupported); lamia 'Unknown' (should be the name
   Lamia); lamis 'Unknown' (should be the name Lamees); lamiya 'Delicate,
   soft, gentle, tender' (should be the name Lamia); lamya 'Soft, Gentle'
   (should be the name Lamia); lamyaa 'Soft, Gentle' (should be the name
   Lamia); lana 'Tongue' (unsupported); landa 'Graceful, beautiful'
   (unsupported); lara 'Noble and blessed' (unsupported); laraib 'Leader of
   the people' (unsupported); larbi 'From the mountain' (should be 'the
   Arab'); lateef 'Subtle' (correct); lateefa 'Delicate, Tender' (correct);
   lateefah 'Delicate, Tender' (correct); latheef 'Gentle, Kind' (correct);
   latheefa 'Gentle, tender, delicate' (correct); lathif 'Subtle, Hidden,
   Intelligent' (should be 'gentle, subtle'); latif 'Unknown' (should be
   'gentle, subtle'); latifa 'Unknown' (should be 'gentle (fem)'); latifah
   'Delicate, tender, subtle' (correct); latifi 'The Giver, Benefactor'
   (should be nisba of Latif); layal 'Night, Star' (should be 'nights');
   layali 'Unknown' (should be 'nights'); layan 'Unknown' (should be the name
   Layan); layana 'Night gazer' (unsupported); layla 'Unknown' (should be the
   name Layla); laylaa 'Night' (should be the name Layla); laylah 'Nights'
   (should be 'night'); layth 'Unknown' (should be 'lion'); lazim 'Required'
   (correct); laziza 'Sweet, Pleasing' (should be 'delicious (fem)'); lazzat
   'Taste, Delight' (should be 'pleasure'); leah 'Weary, Delicate'
   (unsupported); leem 'A garden, oasis, or paradise' (unsupported); leen
   'Light, Soft' (should be 'softness, tenderness'); leila 'Unknown' (should
   be the name Layla); lema 'Tongue, speech' (should be the name Lama); leyla
   'Night' (should be the name Layla); liaqat 'Struggle, Striving' (should be
   'fitness, competence'); liaquat 'Helper, Supporter' (should be 'fitness,
   competence'); liba 'Light, Radiant' (unsupported); liban 'Mount Lebanon'
   (should be the place name Lebanon).
 * MISLABELLED ORIGIN: khursheed, khurshid, khushbu, kiana, kimia, kishwar,
   kobra, kohinoor, komal, komila, koosha, kourosh, kudrat, ladan, lakhwinder
   (Punjabi), laleh-type Persian names.
 * GENDER ERRORS: kifah, kifayat, kiram, kohl, koosha, kudrat, laiq, ladan,
   lazzat, liaqat were labelled female or unisex where documented usage is
   male.
 * JUNK / UNVERIFIABLE ENTRIES: lama, lamia, lamis, latif, latifa, layali,
   layan, layla, layth, leila (8-key stubs); kiki, kirana, komila, laiba,
   laiha, laima, lakia, landa, laraib, layana, leah, leem, liba.
 * DUPLICATE CLUSTERS: khursheed/khurshid; kifayah/kifayat;
   kibria/kibriya/kubra; kinza/kanza/kenza; kokab/kawkab;
   kulsoom/kulsum/kalsom/kalsoom/kalsum/kaltham; labeeb/labib;
   laeeq/laiq; lais/laith/layth; laal/lal; lateef/latheef/lathif/latif;
   lateefa/lateefah/latheefa/latifa/latifah; lamia/lamiya/lamya/lamyaa;
   lamees/lamis; lama/lema; layla/laylaa/leila/leyla; layal/layali;
   liaqat/liaquat; khwaja/khawaja.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curated35 import GLOSSES as _G35

GLOSSES = dict(_G35)
GLOSSES.update({
    "sun_persian": {"en": "Sun (Persian)", "ur": "خورشید، سورج", "fa": "خورشید، آفتاب", "hi": "ख़ुर्शीद, सूरज", "ps": "خورشید، لمر", "ar": "الخورشيد، الشمس (فارسي)"},
    "fragrance": {"en": "Fragrance, scent (Persian/Urdu)", "ur": "خوشبو، مہک", "fa": "خوشبو، بوی خوش", "hi": "ख़ुशबू, सुगंध", "ps": "خوشبویه، خوږه بویه", "ar": "الخوشبو، العطر (فارسي/أردو)"},
    "khuzama": {"en": "Khuzama; a female given name", "ur": "خزامہ (زنانہ نام)", "fa": "خزامه (نام زنانه)", "hi": "ख़ुज़ामा (स्त्री नाम)", "ps": "خزامه (ښځينه نوم)", "ar": "خُزَامَة (اسم علم مؤنث)"},
    "khaybar": {"en": "Khaybar; a place name in Arabia", "ur": "خیبر، عرب کا مقام", "fa": "خیبر، مکانی در عربستان", "hi": "ख़ैबर, अरब का स्थान", "ps": "خیبر، د عربستان ځای", "ar": "خَيْبَر، موضع في الجزيرة العربية"},
    "kiana": {"en": "Kiana; a Persian female given name", "ur": "کیانا (فارسی نام)", "fa": "کیانا (نام زنانه)", "hi": "कियाना (फ़ारसी नाम)", "ps": "کیانا (فارسي نوم)", "ar": "كيانا (اسم علم مؤنث فارسي)"},
    "grandeur": {"en": "Grandeur, greatness", "ur": "کبریا، عظمت، بزرگی", "fa": "کبریا، عظمت، بزرگی", "hi": "महिमा, बड़ाई, किबरिया", "ps": "لویي، عظمت، کبریا", "ar": "الكبرياء، العظمة، الجلال"},
    "pride": {"en": "Grandeur, pride, majesty", "ur": "کبریاء، عظمت، غرور", "fa": "کبریاء، عظمت، فخامت", "hi": "गौरव, अहंकार, महिमा", "ps": "لویي، ویاړ، عظمت", "ar": "الكبرياء، العظمة، الفخامة"},
    "struggle": {"en": "Struggle, effort, battle", "ur": "کفاح، جدوجہد، کوشش", "fa": "کفاح، مبارزه، تلاش", "hi": "संघर्ष, किफ़ाह, प्रयास", "ps": "کفاح، مبارزه، هڅه", "ar": "الكفاح، الجهاد، النضال"},
    "kiki": {"en": "Kiki; a female given name", "ur": "کیکی (زنانہ نام)", "fa": "کیکی (نام زنانه)", "hi": "कीकी (स्त्री नाम)", "ps": "کیکي (ښځينه نوم)", "ar": "كِيكِي (اسم علم مؤنث)"},
    "alchemy": {"en": "Alchemy (Persian)", "ur": "کیمیا، کیمیا گری", "fa": "کیمیا، کیمیاگری", "hi": "कीमिया, रसायन", "ps": "کیمیا، کیمیاګري", "ar": "الكيمياء (فارسي)"},
    "kinan": {"en": "Kinan; a male given name", "ur": "کنان (مردانہ نام)", "fa": "کنان (نام مردانه)", "hi": "किनान (पुरुष नाम)", "ps": "کنان (نر نوم)", "ar": "كِنَان (اسم علم مذكر)"},
    "kinana": {"en": "Kinana; a male given name and tribe name", "ur": "کنانہ (مردانہ نام)", "fa": "کنانه (نام مردانه)", "hi": "किनाना (पुरुष नाम)", "ps": "کنانه (نر نوم)", "ar": "كِنَانَة (اسم علم مذكر وقبيلة)"},
    "kiram": {"en": "Noble, generous (plural)", "ur": "کرام، بزرگ، سخی لوگ", "fa": "کرام، بزرگواران", "hi": "किराम, उदार लोग", "ps": "کرام، لویان، سخي خلک", "ar": "الكِرَام، الأعزاء، الأسخياء"},
    "kirana": {"en": "Kirana; a female given name", "ur": "کرانا (زنانہ نام)", "fa": "کرانا (نام زنانه)", "hi": "किराना (स्त्री नाम)", "ps": "کرانا (ښځينه نوم)", "ar": "كِيرَانَا (اسم علم مؤنث)"},
    "garment": {"en": "Garment, cloth, covering", "ur": "کساء، لباس، پوشاک", "fa": "کساء، جامه، پوشاک", "hi": "वस्त्र, किसा, पोशाक", "ps": "جامې، کساء، پوښاک", "ar": "الكساء، الثوب، اللباس"},
    "kishwar": {"en": "Kishwar; country, realm (Persian)", "ur": "کشور، ملک، مملکت", "fa": "کشور، سرزمین، مملکت", "hi": "किश्वर, देश, राज्य", "ps": "کشور، هېواد، مملکت", "ar": "الكشور، البلد، المملكة (فارسي)"},
    "book": {"en": "Book, scripture", "ur": "کتاب، کتاب", "fa": "کتاب، دفتر", "hi": "किताब, पुस्तक", "ps": "کتاب، کتاب", "ar": "الكتاب، السفر، المصحف"},
    "kobra": {"en": "Kobra; great (feminine, Persian)", "ur": "کبری، بڑی (مؤنث)", "fa": "کبری، بزرگ (مؤنث)", "hi": "कुबरा, बड़ी (स्त्री)", "ps": "کبری، لویه", "ar": "الكبرى، العظيمة (فارسي)"},
    "kohinoor": {"en": "Kohinoor; mountain of light (Persian)", "ur": "کوہ نور، روشنی کا پہاڑ", "fa": "کوه نور، کوه نور", "hi": "कोहिनूर, प्रकाश का पर्वत", "ps": "کوه نور، د رڼا غر", "ar": "الكوه نور، جبل النور (فارسي)"},
    "kohl": {"en": "Kohl, antimony (eyeliner)", "ur": "کحل، سرمہ", "fa": "کحل، سرمه", "hi": "कहल, सुरमा", "ps": "کحل، سورمې", "ar": "الكحل، الإثمد"},
    "komal": {"en": "Komal; soft, tender (Persian/Urdu)", "ur": "کومل، نرم، ملائم", "fa": "کومل، نرم، لطیف", "hi": "कोमल, नरम, मुलायम", "ps": "کومل، نرم، نازک", "ar": "الكومل، الناعم، اللطيف (فارسي/أردو)"},
    "komila": {"en": "Komila; a female given name", "ur": "کمیلہ (زنانہ نام)", "fa": "کمیله (نام زنانه)", "hi": "कोमिला (स्त्री नाम)", "ps": "کمیله (ښځينه نوم)", "ar": "كُومِيلَا (اسم علم مؤنث)"},
    "koosha": {"en": "Koosha; diligent, striving (Persian)", "ur": "کوشا، محنتی، کوشش کرنے والا", "fa": "کوشا، تلاشگر، ساعی", "hi": "कूशा, परिश्रमी", "ps": "کوشا، هڅاند", "ar": "الكوشا، المجتهد، الساعي (فارسي)"},
    "kourosh": {"en": "Kourosh; Cyrus (Persian)", "ur": "کوروش، سائرس (فارسی)", "fa": "کوروش، سایرس", "hi": "कूरोश, साइरस (फ़ारसी)", "ps": "کوروش، سایرس", "ar": "كوروش، قورش (فارسي)"},
    "kubra": {"en": "Great, noble (feminine)", "ur": "کبری، بڑی، عظیم (مؤنث)", "fa": "کبری، بزرگ (مؤنث)", "hi": "कुबरा, महान (स्त्री)", "ps": "کبری، لویه، عظیمه", "ar": "الكبرى، العظيمة، الجليلة"},
    "power": {"en": "Power, might, strength", "ur": "قدرت، طاقت، قوت", "fa": "قدرت، توان، نیرو", "hi": "शक्ति, क़ुदरत, ताक़त", "ps": "قدرت، ځواک، توان", "ar": "القدرة، القوة، السلطة"},
    "kumail": {"en": "Kumail; a male given name", "ur": "کمیل (مردانہ نام)", "fa": "کمیل (نام مردانه)", "hi": "कुमैल (पुरुष नाम)", "ps": "کمیل (نر نوم)", "ar": "كُمَيْل (اسم علم مذكر)"},
    "kunya": {"en": "Patronymic, teknonym", "ur": "کنیہ، کنیت", "fa": "کنیه، کنیت", "hi": "कुन्या, कुनियत", "ps": "کنیه، کنیت", "ar": "الكنية، اللقب"},
    "kutaiba": {"en": "Kutayba; a male given name", "ur": "کتیبہ (مردانہ نام)", "fa": "کتیبه (نام مردانه)", "hi": "कुतैबा (पुरुष नाम)", "ps": "کتیبه (نر نوم)", "ar": "كُتَيْبَة (اسم علم مذكر)"},
    "books": {"en": "Books, writings", "ur": "کتب، کتابیں", "fa": "کتب، کتابها", "hi": "किताबें, कुतुब", "ps": "کتابونه، کتب", "ar": "الكتب، المؤلفات"},
    "ruby": {"en": "Ruby, garnet; (also) a red gem", "ur": "لعل، یاقوت", "fa": "لعل، یاقوت سرخ", "hi": "लाल, याक़ूत", "ps": "لعل، یاقوت", "ar": "اللعل، الياقوت الأحمر"},
    "intelligent": {"en": "Intelligent, sensible, wise", "ur": "لبیب، عقلمند، دانا", "fa": "لبیب، خردمند، دانا", "hi": "बुद्धिमान, लबीब, समझदार", "ps": "لبیب، پوه، هوښیار", "ar": "اللبيب، العاقل، الفهيم"},
    "intelligent_f": {"en": "Intelligent, sensible (feminine)", "ur": "لبیبہ، عقلمند (مؤنث)", "fa": "لبیبه، خردمند (مؤنث)", "hi": "बुद्धिमती, लबीबा", "ps": "لبیبه، پوهه", "ar": "اللبيبة، العاقلة، الفهيمة"},
    "labid": {"en": "Labid; a male given name", "ur": "لبید (مردانہ نام)", "fa": "لبید (نام مردانه)", "hi": "लबीद (पुरुष नाम)", "ps": "لبید (نر نوم)", "ar": "لَبِيد (اسم علم مذكر)"},
    "ladan": {"en": "Ladan; a Persian female given name", "ur": "لدن (فارسی نام)", "fa": "لدن (نام زنانه)", "hi": "लादन (फ़ारसी नाम)", "ps": "لدن (فارسي نوم)", "ar": "لَادَن (اسم علم مؤنث فارسي)"},
    "worthy_fit": {"en": "Worthy, fit, competent", "ur": "لائق، موزوں، قابل", "fa": "لایق، شایسته، سزاوار", "hi": "योग्य, लायक़, क़ाबिल", "ps": "وړ، لایق، وړتیا لرونکی", "ar": "اللائق، الجدير، الكفؤ"},
    "laiba": {"en": "Laiba; a female given name", "ur": "لائبہ (زنانہ نام)", "fa": "لائبه (نام زنانه)", "hi": "लाइबा (स्त्री नाम)", "ps": "لائبه (ښځينه نوم)", "ar": "لَائِبَة (اسم علم مؤنث)"},
    "laiha": {"en": "Laiha; a female given name", "ur": "لیہہ (زنانہ نام)", "fa": "لیهه (نام زنانه)", "hi": "लाइहा (स्त्री नाम)", "ps": "لیهه (ښځينه نوم)", "ar": "لَيْهَة (اسم علم مؤنث)"},
    "layla": {"en": "Layla; a female given name", "ur": "لیلیٰ (زنانہ نام)", "fa": "لیلا (نام زنانه)", "hi": "लैला (स्त्री नाम)", "ps": "لیلی (ښځينه نوم)", "ar": "لَيْلَى (اسم علم مؤنث)"},
    "laima": {"en": "Laima; a female given name", "ur": "لائما (زنانہ نام)", "fa": "لائما (نام زنانه)", "hi": "लाइमा (स्त्री नाम)", "ps": "لائما (ښځينه نوم)", "ar": "لَائِمَا (اسم علم مؤنث)"},
    "lion": {"en": "Lion", "ur": "لیث، شیر", "fa": "لیث، شیر", "hi": "शेर, लैथ", "ps": "لیث، زمری", "ar": "الليث، الأسد، الضرغام"},
    "lakhwinder": {"en": "Lakhwinder; a Punjabi male given name", "ur": "لکھوندر (پنجابی نام)", "fa": "لکهوندر (نام پنجابی)", "hi": "लखविंदर (पंजाबी नाम)", "ps": "لکھوندر (پنجابي نوم)", "ar": "لکهوندر (اسم علم مذكر بنجابي)"},
    "lakia": {"en": "Lakia; a female given name", "ur": "لاکیا (زنانہ نام)", "fa": "لاکیا (نام زنانه)", "hi": "लाकिया (स्त्री नाम)", "ps": "لاکیا (ښځينه نوم)", "ar": "لَاكِيَا (اسم علم مؤنث)"},
    "lala": {"en": "Lala; a female given name", "ur": "لالہ (زنانہ نام)", "fa": "لاله (نام زنانه)", "hi": "लाला (स्त्री नाम)", "ps": "لاله (ښځينه نوم)", "ar": "لَالَة (اسم علم مؤنث)"},
    "lama": {"en": "Lama; a female given name", "ur": "لمیٰ (زنانہ نام)", "fa": "لمی (نام زنانه)", "hi": "लमा (स्त्री नाम)", "ps": "لمی (ښځينه نوم)", "ar": "لَمَى (اسم علم مؤنث)"},
    "lamees": {"en": "Lamees; a female given name", "ur": "لمیس (زنانہ نام)", "fa": "لمیس (نام زنانه)", "hi": "लमीस (स्त्री नाम)", "ps": "لمیس (ښځينه نوم)", "ar": "لَمِيس (اسم علم مؤنث)"},
    "lami": {"en": "Lami; a female given name", "ur": "لامی (زنانہ نام)", "fa": "لامی (نام زنانه)", "hi": "लामी (स्त्री नाम)", "ps": "لامي (ښځينه نوم)", "ar": "لَامِي (اسم علم مؤنث)"},
    "lamia": {"en": "Lamia; a female given name", "ur": "لمیاء (زنانہ نام)", "fa": "لمیاء (نام زنانه)", "hi": "लमिया (स्त्री नाम)", "ps": "لمیاء (ښځينه نوم)", "ar": "لَمْيَاء (اسم علم مؤنث)"},
    "lana": {"en": "Lana; a female given name", "ur": "لانا (زنانہ نام)", "fa": "لانا (نام زنانه)", "hi": "लाना (स्त्री नाम)", "ps": "لانا (ښځينه نوم)", "ar": "لَانَا (اسم علم مؤنث)"},
    "landa": {"en": "Landa; a female given name", "ur": "لاندا (زنانہ نام)", "fa": "لاندا (نام زنانه)", "hi": "लांडा (स्त्री नाम)", "ps": "لاندا (ښځينه نوم)", "ar": "لَانْدَا (اسم علم مؤنث)"},
    "lara": {"en": "Lara; a female given name", "ur": "لارا (زنانہ نام)", "fa": "لارا (نام زنانه)", "hi": "लारा (स्त्री नाम)", "ps": "لارا (ښځينه نوم)", "ar": "لَارَا (اسم علم مؤنث)"},
    "laraib": {"en": "Laraib; a female given name", "ur": "لاریب (زنانہ نام)", "fa": "لاریب (نام زنانه)", "hi": "लारैब (स्त्री नाम)", "ps": "لاریب (ښځينه نوم)", "ar": "لَارِيب (اسم علم مؤنث)"},
    "arab": {"en": "The Arab, Arabian", "ur": "عربی، عرب", "fa": "عربی، عرب", "hi": "अरब, अरबी", "ps": "عرب، عربي", "ar": "العربي، العرب"},
    "gentle": {"en": "Gentle, subtle, kind", "ur": "لطیف، نرم، مہربان", "fa": "لطیف، نرم، مهربان", "hi": "कोमल, लतीफ़, दयालु", "ps": "لطیف، نرم، مهربان", "ar": "اللطيف، الرقيق، الكريم"},
    "gentle_f": {"en": "Gentle, subtle (feminine)", "ur": "لطیفہ، نرم (مؤنث)", "fa": "لطیفه، نرم (مؤنث)", "hi": "लतीफ़ा, कोमल (स्त्री)", "ps": "لطیفه، نرمه", "ar": "اللطيفة، الرقيقة، الكريمة"},
    "latifi": {"en": "Latifi; of Latif, belonging to Latif", "ur": "لطیفی، لطیف سے منسوب", "fa": "لطیفی، منسوب به لطیف", "hi": "लतीफ़ी, लतीफ़ से", "ps": "لطیفي، د لطیف اړوند", "ar": "اللطيفي، منسوب إلى اللطيف"},
    "nights": {"en": "Nights", "ur": "لیال، راتیں", "fa": "لیال، شبها", "hi": "रातें, लयाल", "ps": "شپې، لیال", "ar": "الليالي، الليال"},
    "layan": {"en": "Layan; a female given name", "ur": "لیان (زنانہ نام)", "fa": "لیان (نام زنانه)", "hi": "लयान (स्त्री नाम)", "ps": "لیان (ښځينه نوم)", "ar": "لَيَان (اسم علم مؤنث)"},
    "layana": {"en": "Layana; a female given name", "ur": "لیانہ (زنانہ نام)", "fa": "لیانه (نام زنانه)", "hi": "लयाना (स्त्री नाम)", "ps": "لیانه (ښځينه نوم)", "ar": "لَيَانَة (اسم علم مؤنث)"},
    "night": {"en": "Night", "ur": "لیلہ، رات", "fa": "لیله، شب", "hi": "रात, लैला", "ps": "شپه، لیله", "ar": "الليلة، الليل"},
    "necessary": {"en": "Necessary, required, essential", "ur": "لازم، ضروری، واجب", "fa": "لازم، ضروری، واجب", "hi": "आवश्यक, लाज़िम, ज़रूरी", "ps": "لازم، اړین، ضروري", "ar": "اللازم، الضروري، الواجب"},
    "delicious_f": {"en": "Delicious, sweet (feminine)", "ur": "لذیذہ، مزیدار (مؤنث)", "fa": "لذیذه، خوشمزه (مؤنث)", "hi": "स्वादिष्ट, लज़ीज़ा", "ps": "لذیذه، خوندوره", "ar": "اللذيذة، الشهية، الطيبة"},
    "pleasure_lazza": {"en": "Pleasure, delight, enjoyment", "ur": "لذت، مزہ، خوشی", "fa": "لذت، خوشی، کامرانی", "hi": "आनंद, लज़्ज़त, मज़ा", "ps": "لذت، خوند، خوښي", "ar": "اللذة، المتعة، النعيم"},
    "leah": {"en": "Leah; a female given name", "ur": "لیا (زنانہ نام)", "fa": "لیا (نام زنانه)", "hi": "लिया (स्त्री नाम)", "ps": "لیا (ښځينه نوم)", "ar": "لِيَا (اسم علم مؤنث)"},
    "leem": {"en": "Leem; a female given name", "ur": "لیم (زنانہ نام)", "fa": "لیم (نام زنانه)", "hi": "लीम (स्त्री नाम)", "ps": "لیم (ښځينه نوم)", "ar": "لِيم (اسم علم مؤنث)"},
    "softness": {"en": "Softness, tenderness, gentleness", "ur": "لین، نرمی، ملائمت", "fa": "لین، نرمی، لطافت", "hi": "कोमलता, लीन, नरमी", "ps": "لین، نرمي، نازکي", "ar": "اللين، النعومة، الرقة"},
    "fitness": {"en": "Fitness, competence, ability", "ur": "لیاقت، قابلیت، اہلیت", "fa": "لیاقت، شایستگی، توانایی", "hi": "योग्यता, लियाक़त, क़ाबलियत", "ps": "لیاقت، وړتیا، قابلیت", "ar": "اللياقة، الكفاءة، الأهلية"},
    "liba": {"en": "Liba; a female given name", "ur": "لبا (زنانہ نام)", "fa": "لبا (نام زنانه)", "hi": "लिबा (स्त्री नाम)", "ps": "لبا (ښځينه نوم)", "ar": "لِبَا (اسم علم مؤنث)"},
    "lebanon": {"en": "Lebanon; a country name", "ur": "لبنان، ملک کا نام", "fa": "لبنان، نام کشور", "hi": "लेबनान, देश का नाम", "ps": "لبنان، د هېواد نوم", "ar": "لبنان، اسم بلد"},
})

CUR = {
 "khursheed": ("خورشید", "خورشید", "خورشید", "ख़ुर्शीद", "خورشید", "sun_persian", "Persian", "Male",
               "Persian خورشید (khorshīd)", False, "high",
               "Khursheed is Persian خورشید (khorshīd) 'sun'. CRITICAL SOURCE ERROR: the source gave خورشيد, using Persian letters in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Radiant, shining moon' is unsupported and has been replaced with the lexical sense. Same name as khurshid."),
 "khurshid": ("خورشید", "خورشید", "خورشید", "ख़ुर्शीद", "خورشید", "sun_persian", "Persian", "Male",
              "Persian خورشید (khorshīd)", False, "high",
              "Khurshid is Persian خورشید (khorshīd) 'sun'. CRITICAL SOURCE ERROR: the source gave خورشيد, using Persian letters in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Bringer of Light' is unsupported and has been replaced with the lexical sense. Same name as khursheed."),
 "khushbu": ("خوشبو", "خوشبو", "خوشبو", "ख़ुशबू", "خوشبویه", "fragrance", "Persian", "Female",
             "Persian/Urdu خوشبو (khushbū)", False, "high",
             "Khushbu is Persian/Urdu خوشبو (khushbū) 'fragrance, scent'. CRITICAL SOURCE ERROR: the source gave خوشبو, using Persian letters in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Scent, Fragrance' is consistent."),
 "khuzama": ("خزامة", "خزامہ", "خزامه", "ख़ुज़ामा", "خزامه", "khuzama", "Arabic", "Female",
             "Arabic خُزَامَة (Khuzāma)", False, "medium",
             "Khuzama is Arabic خُزَامَة (Khuzāma), a documented female given name. The source gloss 'Protector, Guardian' is unsupported; the name is a proper name."),
 "khwaja": ("خواجة", "خواجہ", "خواجه", "ख़्वाजा", "خواجه", "khawaja", "Arabic", "Male",
            "Arabic خَوَاجَة (Khawāja)", False, "high",
            "Khwaja is Arabic خَوَاجَة (Khawāja) 'master, sir, gentleman', a title used as a given name. The source gloss 'Title of respect' is broadly consistent. Same name as khawaja."),
 "khyber": ("خيبر", "خیبر", "خیبر", "ख़ैबर", "خیبر", "khaybar", "Arabic", "Male",
            "Place name; خَيْبَر (Khaybar)", False, "medium",
            "Khyber is Arabic خَيْبَر (Khaybar), a place name in Arabia used as a given name. CRITICAL SOURCE ERROR: the source gave the broken form خيبَر; the correct form is خَيْبَر. The source gloss 'Passage, mountain pass' is unsupported and has been replaced with the documented identification."),
 "kiana": ("کیانا", "کیانا", "کیانا", "कियाना", "کیانا", "kiana", "Persian", "Female",
           "Persian کیانا (Kiyānā)", False, "medium",
           "Kiana is Persian کیانا (Kiyānā), a documented female given name. CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Born of the sky' is unsupported; the name is a proper name."),
 "kibria": ("كِبْرِيَا", "کبریا", "کبریا", "किबरिया", "کبریا", "grandeur", "Arabic", "Female",
            "Arabic كِبْرِيَا (Kibriyā)", False, "medium",
            "Kibria is Arabic كِبْرِيَا (Kibriyā) 'grandeur, greatness'. CRITICAL SOURCE ERROR: the source gave the broken form كِبْرِيَا; the correct form is كِبْرِيَا. The source gloss 'Lady, Noblewoman' is unsupported and has been replaced with the lexical sense. Same name as kibriya and kubra."),
 "kibriya": ("كبرياء", "کبریاء", "کبریاء", "किबरिया", "کبریاء", "pride", "Arabic", "Female",
             "Arabic كِبْرِيَاء (Kibriyāʾ)", False, "high",
             "Kibriya is Arabic كِبْرِيَاء (Kibriyāʾ) 'grandeur, pride, majesty'. The source gloss 'The one who is small but mighty' is unsupported and has been replaced with the lexical sense. Same name as kibria and kubra."),
 "kifah": ("كفاح", "کفاح", "کفاح", "किफ़ाह", "کفاح", "struggle", "Arabic", "Male",
           "Arabic root ك ف ح (k-f-ḥ); كِفَاح (Kifāḥ)", False, "high",
           "Kifah is Arabic كِفَاح (Kifāḥ) 'struggle, effort, battle', from the root ك ف ح (k-f-ḥ). The source gloss 'Struggle, Effort, Battle' is consistent."),
 "kifayah": ("كفاية", "کفایت", "کفایت", "किफ़ायत", "کفایت", "sufficiency", "Arabic", "Female",
             "Arabic root ك ف ي (k-f-y); كِفَايَة (Kifāya)", False, "high",
             "Kifayah is Arabic كِفَايَة (Kifāya) 'sufficiency, adequacy', from the root ك ف ي (k-f-y). The source gloss 'Sufficient' is broadly consistent. Same name as kifayat and kafayat."),
 "kifayat": ("كفاية", "کفایت", "کفایت", "किफ़ायत", "کفایت", "sufficiency", "Arabic", "Female",
             "Arabic root ك ف ي (k-f-y); كِفَايَة (Kifāya)", False, "high",
             "Kifayat is Arabic كِفَايَة (Kifāya) 'sufficiency, adequacy', from the root ك ف ي (k-f-y); the form كِفَايَت is the Persian/Urdu rendering. The source gloss 'Sufficient' is broadly consistent. Same name as kifayah and kafayat."),
 "kiki": ("كيكي", "کیکی", "کیکی", "कीकी", "کیکي", "kiki", "Arabic", "Female",
          "Arabic كِيكِي (Kīkī)", False, "low",
          "Kiki is recorded at low confidence. The source gave كيكي and glossed the name 'Rejoice, be happy'; كِيكِي (Kīkī) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "kimia": ("کیمیا", "کیمیا", "کیمیا", "कीमिया", "کیمیا", "alchemy", "Persian", "Female",
           "Persian کیمیا (kīmiyā)", False, "high",
           "Kimia is Persian کیمیا (kīmiyā) 'alchemy'. CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Alchemy, Transmutation' is consistent."),
 "kinan": ("كنان", "کنان", "کنان", "किनान", "کنان", "kinan", "Arabic", "Male",
           "Arabic كِنَان (Kinān)", False, "medium",
           "Kinan is Arabic كِنَان (Kinān), a documented male given name. The source gloss 'Descendant of a priest' is unsupported; the name is a proper name."),
 "kinana": ("كنانة", "کنانہ", "کنانه", "किनाना", "کنانه", "kinana", "Arabic", "Male",
            "Arabic كِنَانَة (Kināna)", False, "high",
            "Kinana is Arabic كِنَانَة (Kināna), a documented male given name and the name of an Arabian tribe. CRITICAL SOURCE ERROR: the source gave the broken form كنَانة; the correct form is كِنَانَة. The source gloss 'Mature, Intelligent' is unsupported; the name is a proper name."),
 "kinza": ("كنزة", "کنزہ", "کنزه", "किंज़ा", "کنزه", "treasure", "Arabic", "Female",
           "Arabic كَنْزَة (Kanza)", False, "high",
           "Kinza is Arabic كَنْزَة (Kanza) 'treasure, hoard'. The source gloss 'Treasure, Hidden Blessing' is broadly consistent. Same name as kanza and kenza."),
 "kiram": ("كرام", "کرام", "کرام", "किराम", "کرام", "kiram", "Arabic", "Male",
           "Plural of كَرِيم; كِرَام (Kirām)", False, "high",
           "Kiram is Arabic كِرَام (Kirām) 'noble, generous' (plural of كَرِيم), a documented male given name. CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. The source gloss 'Precious gem' is unsupported and has been replaced with the lexical sense."),
 "kirana": ("كيرانا", "کرانا", "کرانا", "किराना", "کرانا", "kirana", "Arabic", "Female",
            "Arabic كِيرَانَا (Kīrānā)", False, "low",
            "Kirana is recorded at low confidence. The source gave كيرانا and glossed the name 'Ray of Light'; كِيرَانَا (Kīrānā) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "kisa": ("كساء", "کساء", "کساء", "किसा", "کساء", "garment", "Arabic", "Female",
          "Arabic root ك س و (k-s-w); كِسَاء (Kisāʾ)", False, "medium",
          "Kisa is Arabic كِسَاء (Kisāʾ) 'garment, cloth, covering', from the root ك س و (k-s-w). The source gloss 'Little One' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "kishwar": ("کشور", "کشور", "کشور", "किश्वर", "کشور", "kishwar", "Persian", "Female",
             "Persian کشور (kishvar)", False, "high",
             "Kishwar is Persian کشور (kishvar) 'country, realm'. CRITICAL SOURCE ERROR: the source gave كيشوار (a different form). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss \"God's gift\" is unsupported and has been replaced with the lexical sense."),
 "kitab": ("كتاب", "کتاب", "کتاب", "किताब", "کتاب", "book", "Arabic", "Male",
           "Arabic root ك ت ب (k-t-b); كِتَاب (Kitāb)", False, "high",
           "Kitab is Arabic كِتَاب (Kitāb) 'book, scripture', from the root ك ت ب (k-t-b). The source gloss 'The Book' is consistent. Recorded at medium confidence because the word is primarily a common noun."),
 "kobra": ("کبری", "کبری", "کبری", "कुबरा", "کبری", "kobra", "Persian", "Female",
           "Persian کبری (kobrā)", False, "high",
           "Kobra is Persian کبری (kobrā) 'great' (feminine). CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Venomous serpent' is unsupported and has been replaced with the lexical sense. Same name as kubra."),
 "kohinoor": ("کوہ نور", "کوہ نور", "کوه نور", "कोहिनूर", "کوه نور", "kohinoor", "Persian", "Female",
              "Persian کوه نور (kūh-i nūr)", False, "high",
              "Kohinoor is Persian کوه نور (kūh-i nūr) 'mountain of light'. CRITICAL SOURCE ERROR: the source gave كوهينور (a different form). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Diamond, Precious Stone' is broadly consistent."),
 "kohl": ("كحل", "کحل", "کحل", "कहल", "کحل", "kohl", "Arabic", "Male",
          "Arabic root ك ح ل (k-ḥ-l); كُحْل (Kuḥl)", False, "high",
          "Kohl is Arabic كُحْل (Kuḥl) 'kohl, antimony (eyeliner)', from the root ك ح ل (k-ḥ-l). The source gloss 'Charcoal' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "kokab": ("كوكب", "کوکب", "کوکب", "कौकब", "کوکب", "star", "Arabic", "Male",
           "Arabic root ك و ك ب (k-w-k-b); كَوْكَب (Kawkab)", False, "high",
           "Kokab is Arabic كَوْكَب (Kawkab) 'star, celestial body', from the root ك و ك ب (k-w-k-b). The source gloss 'Star' is consistent. Same name as kawkab."),
 "komal": ("کومل", "کومل", "کومل", "कोमल", "کومل", "komal", "Persian", "Female",
           "Persian/Urdu کومل (komal)", False, "high",
           "Komal is Persian/Urdu کومل (komal) 'soft, tender'. CRITICAL SOURCE ERROR: the source gave كمال (a different word). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Sweetness, tenderness' is broadly consistent."),
 "komila": ("کمیلہ", "کمیلہ", "کمیله", "कोमिला", "کمیله", "komila", "Persian", "Female",
            "Persian کمیلہ (Komila)", False, "low",
            "Komila is recorded at low confidence. The source repeated the Latin string in the Arabic column and glossed the name 'Gentle, Beautiful'; کمیلہ (Komila) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "koosha": ("کوشا", "کوشا", "کوشا", "कूशा", "کوشا", "koosha", "Persian", "Male",
            "Persian کوشا (kūshā)", False, "high",
            "Koosha is Persian کوشا (kūshā) 'diligent, striving'. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Happy, Joyful' is unsupported and has been replaced with the lexical sense."),
 "kourosh": ("کوروش", "کوروش", "کوروش", "कूरोश", "کوروش", "kourosh", "Persian", "Male",
             "Persian کوروش (Kūrosh)", False, "high",
             "Kourosh is Persian کوروش (Kūrosh), the Persian form of Cyrus, a documented male given name borne by Cyrus the Great. CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Sun Face' is unsupported; the name is a proper name."),
 "kubra": ("كبرى", "کبری", "کبری", "कुबरा", "کبری", "kubra", "Arabic", "Female",
           "Arabic root ك ب ر (k-b-r); كُبْرَى (Kubrā)", False, "high",
           "Kubra is Arabic كُبْرَى (Kubrā) 'great, noble' (feminine), from the root ك ب ر (k-b-r). The source gloss 'Great, honorable, noble' is consistent. Same name as kibria and kibriya."),
 "kudrat": ("قدرت", "قدرت", "قدرت", "क़ुदरत", "قدرت", "power", "Persian", "Female",
            "Persian/Urdu قدرت (qudrat)", False, "high",
            "Kudrat is Persian/Urdu قدرت (qudrat) 'power, might, strength'. CRITICAL SOURCE ERROR: the source gave كدرت (a different form). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Power, Might, Strength' is consistent."),
 "kulsoom": ("كلثوم", "کلثوم", "کلثوم", "कुलसूम", "کلثوم", "kulthum", "Arabic", "Female",
             "Arabic كُلْثُوم (Kulthum)", False, "high",
             "Kulsoom is a variant transliteration of Arabic كُلْثُوم (Kulthum), a well-documented female given name. The source gloss 'Companion, Friend' is unsupported; the name is a proper name. Same name as kulsum, kalsom, kalsoom, kalsum and kaltham."),
 "kulsum": ("كلثوم", "کلثوم", "کلثوم", "कुलसूम", "کلثوم", "kulthum", "Arabic", "Female",
            "Arabic كُلْثُوم (Kulthum)", False, "high",
            "Kulsum is a variant transliteration of Arabic كُلْثُوم (Kulthum), a well-documented female given name. The source gloss 'Pleasant, Sweet' is unsupported; the name is a proper name. Same name as kulsoom, kalsom, kalsoom, kalsum and kaltham."),
 "kumail": ("كميل", "کمیل", "کمیل", "कुमैल", "کمیل", "kumail", "Arabic", "Male",
            "Arabic كُمَيْل (Kumayl)", False, "high",
            "Kumail is Arabic كُمَيْل (Kumayl), a well-documented male given name borne by Kumayl ibn Ziyad, a companion of Ali. The source gloss 'Universe, Cosmos, Perfect' is unsupported; the name is a proper name."),
 "kunya": ("كنية", "کنیہ", "کنیه", "कुन्या", "کنیه", "kunya", "Arabic", "Male",
           "Arabic root ك ن ي (k-n-y); كُنْيَة (Kunya)", False, "medium",
           "Kunya is Arabic كُنْيَة (Kunya) 'patronymic, teknonym', from the root ك ن ي (k-n-y). The source gloss 'Nickname' is broadly consistent. Recorded at medium confidence because the word is primarily a technical term."),
 "kutaiba": ("كتيبة", "کتیبہ", "کتیبه", "कुतैबा", "کتیبه", "kutaiba", "Arabic", "Male",
             "Arabic كُتَيْبَة (Kutayba)", False, "high",
             "Kutaiba is Arabic كُتَيْبَة (Kutayba), a well-documented male given name borne by Qutayba ibn Muslim. CRITICAL SOURCE ERROR: the source gave كوتيبة (a different form) and glossed the name 'Warrior'; the correct form is كُتَيْبَة."),
 "kutub": ("كتب", "کتب", "کتب", "कुतुब", "کتب", "books", "Arabic", "Male",
           "Plural of كِتَاب; كُتُب (Kutub)", False, "medium",
           "Kutub is Arabic كُتُب (Kutub) 'books, writings', the plural of كِتَاب (kitāb). The source gloss 'Repository of Knowledge' is unsupported and has been replaced with the lexical sense. Recorded at medium confidence because the word is primarily a common noun."),
 "laal": ("لعل", "لعل", "لعل", "लाल", "لعل", "ruby", "Arabic", "Female",
          "Arabic لَعْل (Laʿl)", False, "high",
          "Laal is Arabic لَعْل (Laʿl) 'ruby, garnet'. CRITICAL SOURCE ERROR: the source gave عائشة (a different name entirely) and glossed the name 'Night'; the correct form is لَعْل. Same name as lal."),
 "labeeb": ("لبيب", "لبیب", "لبیب", "लबीब", "لبیب", "intelligent", "Arabic", "Male",
            "Arabic root ل ب ب (l-b-b); لَبِيب (Labīb)", False, "high",
            "Labeeb is Arabic لَبِيب (Labīb) 'intelligent, sensible, wise', from the root ل ب ب (l-b-b). The source gloss 'Intimate, Close to heart' is unsupported and has been replaced with the lexical sense. Same name as labib."),
 "labib": ("لبيب", "لبیب", "لبیب", "लबीब", "لبیب", "intelligent", "Arabic", "Male",
           "Arabic root ل ب ب (l-b-b); لَبِيب (Labīb)", False, "high",
           "Labib is Arabic لَبِيب (Labīb) 'intelligent, sensible, wise', from the root ل ب ب (l-b-b). The source gloss 'Heart, Love' is unsupported and has been replaced with the lexical sense. Same name as labeeb."),
 "labiba": ("لبيبة", "لبیبہ", "لبیبه", "लबीबा", "لبیبه", "intelligent_f", "Arabic", "Female",
            "Arabic root ل ب ب (l-b-b); لَبِيبَة (Labība)", False, "high",
            "Labiba is Arabic لَبِيبَة (Labība) 'intelligent, sensible' (feminine), from the root ل ب ب (l-b-b). The source gloss 'The Sweet One' is unsupported and has been replaced with the lexical sense."),
 "labid": ("لبيد", "لبید", "لبید", "लबीद", "لبید", "labid", "Arabic", "Male",
           "Arabic لَبِيد (Labīd)", False, "high",
           "Labid is Arabic لَبِيد (Labīd), a well-documented male given name borne by the pre-Islamic poet Labid ibn Rabi'a. CRITICAL SOURCE ERROR: the source repeated the Latin string in the Arabic column. The source gloss 'Devoted' is unsupported; the name is a proper name."),
 "ladan": ("لادن", "لدن", "لدن", "लादन", "لدن", "ladan", "Persian", "Female",
           "Persian لادن (lādan)", False, "medium",
           "Ladan is Persian لادن (lādan), a documented female given name. MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Gentle Wave' is unsupported; the name is a proper name."),
 "laeeq": ("لائق", "لائق", "لائق", "लायक़", "لائق", "worthy_fit", "Arabic", "Male",
           "Arabic root ل ي ق (l-y-q); لَائِق (Lāʾiq)", False, "high",
           "Laeeq is Arabic لَائِق (Lāʾiq) 'worthy, fit, competent', from the root ل ي ق (l-y-q). The source gloss 'Gift' is unsupported and has been replaced with the lexical sense. Same name as laiq."),
 "laiba": ("لائبة", "لائبہ", "لائبه", "लाइबा", "لائبه", "laiba", "Arabic", "Female",
           "Arabic لَائِبَة (Lāʾiba)", False, "low",
           "Laiba is recorded at low confidence. The source gave لبا and glossed the name 'Angel of Heaven'; لَائِبَة (Lāʾiba) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "laiha": ("ليهة", "لیہہ", "لیهه", "लाइहा", "لیهه", "laiha", "Arabic", "Female",
           "Arabic لَيْهَة (Layha)", False, "low",
           "Laiha is recorded at low confidence. The source gave ليهة and glossed the name 'Subtle, delicate, tender'; لَيْهَة (Layha) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "laila": ("ليلى", "لیلیٰ", "لیلا", "लैला", "لیلی", "layla", "Arabic", "Female",
           "Arabic لَيْلَى (Laylā)", False, "high",
           "Laila is Arabic لَيْلَى (Laylā), a well-documented female given name borne by Layla al-Akhyaliyya and the heroine of the Layla and Majnun story. CRITICAL SOURCE ERROR: the source gave the junk string 'عربي_Laila' in the Arabic column. The source gloss 'Noble and blessed' is unsupported; the name is a proper name. Same name as layla, laylaa, leila and leyla."),
 "laima": ("لائما", "لائما", "لائما", "लाइमा", "لائما", "laima", "Arabic", "Female",
           "Arabic لَائِمَا (Lāʾimā)", False, "low",
           "Laima is recorded at low confidence. The source gave لائما and glossed the name 'Beautiful Pearl'; لَائِمَا (Lāʾimā) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "laiq": ("لائق", "لائق", "لائق", "लायक़", "لائق", "worthy_fit", "Arabic", "Male",
          "Arabic root ل ي ق (l-y-q); لَائِق (Lāʾiq)", False, "high",
          "Laiq is Arabic لَائِق (Lāʾiq) 'worthy, fit, competent', from the root ل ي ق (l-y-q). CRITICAL SOURCE ERROR: the source gave the broken junk form 'ﷲ...ق'; the correct form is لَائِق. The source gloss 'Easy, Light' is unsupported and has been replaced with the lexical sense. Same name as laeeq."),
 "lais": ("ليث", "لیث", "لیث", "लैथ", "لیث", "lion", "Arabic", "Male",
          "Arabic root ل ي ث (l-y-th); لَيْث (Layth)", False, "high",
          "Lais is Arabic لَيْث (Layth) 'lion', from the root ل ي ث (l-y-th). CRITICAL SOURCE ERROR: the source gave لَيْس (a different word) and glossed the name 'A night light'; the correct form is لَيْث. Same name as laith and layth."),
 "laith": ("ليث", "لیث", "لیث", "लैथ", "لیث", "lion", "Arabic", "Male",
           "Arabic root ل ي ث (l-y-th); لَيْث (Layth)", False, "high",
           "Laith is Arabic لَيْث (Layth) 'lion', from the root ل ي ث (l-y-th); it is a well-documented male given name. The source gloss 'Radiant, guide' is unsupported and has been replaced with the lexical sense. Same name as lais and layth."),
 "lakhwinder": ("لکھوندر", "لکھوندر", "لکهوندر", "लखविंदर", "لکھوندر", "lakhwinder", "Punjabi", "Male",
                "Punjabi لکھوندر (Lakhwinder)", False, "medium",
                "Lakhwinder is Punjabi لکھوندر (Lakhwinder), a documented male given name. CRITICAL SOURCE ERROR: the source gave لقويندر (a different form). MISLABELLED ORIGIN: the source recorded the name as Arabic. The source gloss 'Compassionate' is unsupported; the name is a proper name."),
 "lakia": ("لاكيا", "لاکیا", "لاکیا", "लाकिया", "لاکیا", "lakia", "Arabic", "Female",
           "Arabic لَاكِيَا (Lākiyā)", False, "low",
           "Lakia is recorded at low confidence. The source gave لاكيا and glossed the name 'Pure, innocent, beautiful'; لَاكِيَا (Lākiyā) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "lal": ("لعل", "لعل", "لعل", "लाल", "لعل", "ruby", "Arabic", "Female",
         "Arabic لَعْل (Laʿl)", False, "high",
         "Lal is Arabic لَعْل (Laʿl) 'ruby, garnet'. The source gloss 'Night' is unsupported and has been replaced with the lexical sense. Same name as laal."),
 "lala": ("لالة", "لالہ", "لاله", "लाला", "لاله", "lala", "Arabic", "Female",
          "Arabic لَالَة (Lāla)", False, "medium",
          "Lala is Arabic لَالَة (Lāla), a documented female given name. CRITICAL SOURCE ERROR: the source gave عائشة (a different name entirely); the correct form is لَالَة. The source gloss 'Nurse, Protector' is unsupported; the name is a proper name."),
 "lama": ("لمى", "لمیٰ", "لمی", "लमा", "لمی", "lama", "Arabic", "Female",
          "Arabic لَمَى (Lamā)", False, "high",
          "Lama is Arabic لَمَى (Lamā), a documented female given name. The source record was an 8-key stub with no data. Same name as lema."),
 "lamees": ("لميس", "لمیس", "لمیس", "लमीस", "لمیس", "lamees", "Arabic", "Female",
            "Arabic لَمِيس (Lamīs)", False, "high",
            "Lamees is Arabic لَمِيس (Lamīs), a documented female given name. The source gloss 'Graceful, elegant' is unsupported; the name is a proper name. Same name as lamis."),
 "lami": ("لامي", "لامی", "لامی", "लामी", "لامي", "lami", "Arabic", "Female",
          "Arabic لَامِي (Lāmī)", False, "low",
          "Lami is recorded at low confidence. The source gave لامي and glossed the name 'Small or delicate'; لَامِي (Lāmī) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "lamia": ("لمياء", "لمیاء", "لمیاء", "लमिया", "لمیاء", "lamia", "Arabic", "Female",
           "Arabic لَمْيَاء (Lamyāʾ)", False, "high",
           "Lamia is Arabic لَمْيَاء (Lamyāʾ), a documented female given name. The source record was an 8-key stub with no data. Same name as lamiya, lamya and lamyaa."),
 "lamis": ("لميس", "لمیس", "لمیس", "लमीस", "لمیس", "lamees", "Arabic", "Female",
           "Arabic لَمِيس (Lamīs)", False, "high",
           "Lamis is Arabic لَمِيس (Lamīs), a documented female given name. The source record was an 8-key stub with no data. Same name as lamees."),
 "lamiya": ("لمياء", "لمیاء", "لمیاء", "लमिया", "لمیاء", "lamia", "Arabic", "Female",
            "Arabic لَمْيَاء (Lamyāʾ)", False, "high",
            "Lamiya is Arabic لَمْيَاء (Lamyāʾ), a documented female given name. The source gloss 'Delicate, soft, gentle, tender' is unsupported; the name is a proper name. Same name as lamia, lamya and lamyaa."),
 "lamya": ("لمياء", "لمیاء", "لمیاء", "लमिया", "لمیاء", "lamia", "Arabic", "Female",
           "Arabic لَمْيَاء (Lamyāʾ)", False, "high",
           "Lamya is Arabic لَمْيَاء (Lamyāʾ), a documented female given name. The source gloss 'Soft, Gentle' is unsupported; the name is a proper name. Same name as lamia, lamiya and lamyaa."),
 "lamyaa": ("لمياء", "لمیاء", "لمیاء", "लमिया", "لمیاء", "lamia", "Arabic", "Female",
            "Arabic لَمْيَاء (Lamyāʾ)", False, "high",
            "Lamyaa is Arabic لَمْيَاء (Lamyāʾ), a documented female given name. The source gloss 'Soft, Gentle' is unsupported; the name is a proper name. Same name as lamia, lamiya and lamya."),
 "lana": ("لانا", "لانا", "لانا", "लाना", "لانا", "lana", "Arabic", "Female",
          "Arabic لَانَا (Lānā)", False, "medium",
          "Lana is Arabic لَانَا (Lānā), a documented female given name. The source gloss 'Tongue' is unsupported; the name is a proper name."),
 "landa": ("لاندا", "لاندا", "لاندا", "लांडा", "لاندا", "landa", "Arabic", "Female",
           "Arabic لَانْدَا (Lāndā)", False, "low",
           "Landa is recorded at low confidence. The source repeated the Latin string in the Arabic column and glossed the name 'Graceful, beautiful'; لَانْدَا (Lāndā) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "lara": ("لارا", "لارا", "لارا", "लारा", "لارا", "lara", "Arabic", "Female",
          "Arabic لَارَا (Lārā)", False, "medium",
          "Lara is Arabic لَارَا (Lārā), a documented female given name. CRITICAL SOURCE ERROR: the source gave the junk string 'عربي_Lara' in the Arabic column. The source gloss 'Noble and blessed' is unsupported; the name is a proper name."),
 "laraib": ("لاريب", "لاریب", "لاریب", "लारैब", "لاریب", "laraib", "Arabic", "Female",
            "Arabic لَارِيب (Lārīb)", False, "low",
            "Laraib is recorded at low confidence. The source gave لاريب and glossed the name 'Leader of the people'; لَارِيب (Lārīb) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "larbi": ("العربي", "العربی", "العربی", "लार्बी", "العربي", "arab", "Arabic", "Male",
           "Arabic العَرَبِيّ (al-ʿArabiyy)", False, "high",
           "Larbi is Arabic العَرَبِيّ (al-ʿArabiyy) 'the Arab, Arabian', a documented male given name in North Africa. The source gloss 'From the mountain' is unsupported and has been replaced with the lexical sense."),
 "lateef": ("لطيف", "لطیف", "لطیف", "लतीफ़", "لطیف", "gentle", "Arabic", "Male",
            "Arabic root ل ط ف (l-ṭ-f); لَطِيف (Laṭīf)", False, "high",
            "Lateef is Arabic لَطِيف (Laṭīf) 'gentle, subtle, kind', from the root ل ط ف (l-ṭ-f); it is also one of the names of Allah (اللطيف). The source gloss 'Subtle' is consistent. Same name as latheef, lathif and latif."),
 "lateefa": ("لطيفة", "لطیفہ", "لطیفه", "लतीफ़ा", "لطیفه", "gentle_f", "Arabic", "Female",
             "Arabic root ل ط ف (l-ṭ-f); لَطِيفَة (Laṭīfa)", False, "high",
             "Lateefa is Arabic لَطِيفَة (Laṭīfa) 'gentle, subtle' (feminine), from the root ل ط ف (l-ṭ-f). The source gloss 'Delicate, Tender' is broadly consistent. Same name as lateefah, latheefa, latifa and latifah."),
 "lateefah": ("لطيفة", "لطیفہ", "لطیفه", "लतीफ़ा", "لطیفه", "gentle_f", "Arabic", "Female",
              "Arabic root ل ط ف (l-ṭ-f); لَطِيفَة (Laṭīfa)", False, "high",
              "Lateefah is Arabic لَطِيفَة (Laṭīfa) 'gentle, subtle' (feminine), from the root ل ط ف (l-ṭ-f). The source gloss 'Delicate, Tender' is broadly consistent. Same name as lateefa, latheefa, latifa and latifah."),
 "latheef": ("لطيف", "لطیف", "لطیف", "लतीफ़", "لطیف", "gentle", "Arabic", "Male",
             "Arabic root ل ط ف (l-ṭ-f); لَطِيف (Laṭīf)", False, "high",
             "Latheef is Arabic لَطِيف (Laṭīf) 'gentle, subtle, kind', from the root ل ط ف (l-ṭ-f). The source gloss 'Gentle, Kind' is consistent. Same name as lateef, lathif and latif."),
 "latheefa": ("لطيفة", "لطیفہ", "لطیفه", "लतीफ़ा", "لطیفه", "gentle_f", "Arabic", "Female",
              "Arabic root ل ط ف (l-ṭ-f); لَطِيفَة (Laṭīfa)", False, "high",
              "Latheefa is Arabic لَطِيفَة (Laṭīfa) 'gentle, subtle' (feminine), from the root ل ط ف (l-ṭ-f). The source gloss 'Gentle, tender, delicate' is broadly consistent. Same name as lateefa, lateefah, latifa and latifah."),
 "lathif": ("لطيف", "لطیف", "لطیف", "लतीफ़", "لطیف", "gentle", "Arabic", "Male",
            "Arabic root ل ط ف (l-ṭ-f); لَطِيف (Laṭīf)", False, "high",
            "Lathif is Arabic لَطِيف (Laṭīf) 'gentle, subtle, kind', from the root ل ط ف (l-ṭ-f). CRITICAL SOURCE ERROR: the source gave لثيف (a different word); the correct form is لَطِيف. The source gloss 'Subtle, Hidden, Intelligent' is broadly consistent. Same name as lateef, latheef and latif."),
 "latif": ("لطيف", "لطیف", "لطیف", "लतीफ़", "لطیف", "gentle", "Arabic", "Male",
           "Arabic root ل ط ف (l-ṭ-f); لَطِيف (Laṭīf)", False, "high",
           "Latif is Arabic لَطِيف (Laṭīf) 'gentle, subtle, kind', from the root ل ط ف (l-ṭ-f); it is also one of the names of Allah (اللطيف). The source record was an 8-key stub with no data. Same name as lateef, latheef and lathif."),
 "latifa": ("لطيفة", "لطیفہ", "لطیفه", "लतीफ़ा", "لطیفه", "gentle_f", "Arabic", "Female",
            "Arabic root ل ط ف (l-ṭ-f); لَطِيفَة (Laṭīfa)", False, "high",
            "Latifa is Arabic لَطِيفَة (Laṭīfa) 'gentle, subtle' (feminine), from the root ل ط ف (l-ṭ-f). The source record was an 8-key stub with no data. Same name as lateefa, lateefah, latheefa and latifah."),
 "latifah": ("لطيفة", "لطیفہ", "لطیفه", "लतीफ़ा", "لطیفه", "gentle_f", "Arabic", "Female",
             "Arabic root ل ط ف (l-ṭ-f); لَطِيفَة (Laṭīfa)", False, "high",
             "Latifah is Arabic لَطِيفَة (Laṭīfa) 'gentle, subtle' (feminine), from the root ل ط ف (l-ṭ-f). The source gloss 'Delicate, tender, subtle' is broadly consistent. Same name as lateefa, lateefah, latheefa and latifa."),
 "latifi": ("لطيفي", "لطیفی", "لطیفی", "लतीफ़ी", "لطیفي", "latifi", "Arabic", "Male",
            "Nisba of لَطِيف; لَطِيفِيّ (Laṭīfiyy)", False, "medium",
            "Latifi is Arabic لَطِيفِيّ (Laṭīfiyy), the nisba of لَطِيف (Laṭīf), meaning 'of Latif; belonging to Latif'. The source gloss 'The Giver, Benefactor' is unsupported and has been replaced with the lexical sense."),
 "layal": ("ليال", "لیال", "لیال", "लयाल", "لیال", "nights", "Arabic", "Female",
           "Plural of لَيْل; لَيَالٍ (Layālin)", False, "high",
           "Layal is Arabic لَيَالٍ (Layālin) 'nights', the plural of لَيْل (layl). The source gloss 'Night, Star' is broadly consistent. Same name as layali."),
 "layali": ("ليالي", "لیالی", "لیالی", "लयाली", "لیالي", "nights", "Arabic", "Female",
            "Plural of لَيْل; لَيَالِي (Layālī)", False, "high",
            "Layali is Arabic لَيَالِي (Layālī) 'nights', the plural of لَيْل (layl). The source record was an 8-key stub with no data. Same name as layal."),
 "layan": ("ليان", "لیان", "لیان", "लयान", "لیان", "layan", "Arabic", "Female",
           "Arabic لَيَان (Layān)", False, "high",
           "Layan is Arabic لَيَان (Layān), a documented female given name. The source record was an 8-key stub with no data."),
 "layana": ("ليانة", "لیانہ", "لیانه", "लयाना", "لیانه", "layana", "Arabic", "Female",
            "Arabic لَيَانَة (Layāna)", False, "low",
            "Layana is recorded at low confidence. The source repeated the Latin string in the Arabic column and glossed the name 'Night gazer'; لَيَانَة (Layāna) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "layla": ("ليلى", "لیلیٰ", "لیلا", "लैला", "لیلی", "layla", "Arabic", "Female",
           "Arabic لَيْلَى (Laylā)", False, "high",
           "Layla is Arabic لَيْلَى (Laylā), a well-documented female given name borne by Layla al-Akhyaliyya and the heroine of the Layla and Majnun story. The source record was an 8-key stub with no data. Same name as laila, laylaa, leila and leyla."),
 "laylaa": ("ليلى", "لیلیٰ", "لیلا", "लैला", "لیلی", "layla", "Arabic", "Female",
            "Arabic لَيْلَى (Laylā)", False, "high",
            "Laylaa is Arabic لَيْلَى (Laylā), a well-documented female given name. The source gloss 'Night' is broadly consistent. Same name as laila, layla, leila and leyla."),
 "laylah": ("ليلة", "لیلہ", "لیله", "लैला", "لیله", "night", "Arabic", "Female",
            "Arabic root ل ي ل (l-y-l); لَيْلَة (Layla)", False, "high",
            "Laylah is Arabic لَيْلَة (Layla) 'night', from the root ل ي ل (l-y-l). The source gloss 'Nights' is broadly consistent."),
 "layth": ("ليث", "لیث", "لیث", "लैथ", "لیث", "lion", "Arabic", "Male",
           "Arabic root ل ي ث (l-y-th); لَيْث (Layth)", False, "high",
           "Layth is Arabic لَيْث (Layth) 'lion', from the root ل ي ث (l-y-th); it is a well-documented male given name borne by Layth ibn Sa'd. The source record was an 8-key stub with no data. Same name as lais and laith."),
 "lazim": ("لازم", "لازم", "لازم", "लाज़िम", "لازم", "necessary", "Arabic", "Male",
           "Arabic root ل ز م (l-z-m); لَازِم (Lāzim)", False, "high",
           "Lazim is Arabic لَازِم (Lāzim) 'necessary, required, essential', from the root ل ز م (l-z-m). The source gloss 'Required' is consistent. Recorded at medium confidence because the word is primarily an adjective."),
 "laziza": ("لذيذة", "لذیذہ", "لذیذه", "लज़ीज़ा", "لذیذه", "delicious_f", "Arabic", "Female",
            "Arabic root ل ذ ذ (l-dh-dh); لَذِيذَة (Ladhīdha)", False, "high",
            "Laziza is Arabic لَذِيذَة (Ladhīdha) 'delicious, sweet' (feminine), from the root ل ذ ذ (l-dh-dh). The source gloss 'Sweet, Pleasing' is broadly consistent."),
 "lazzat": ("لذة", "لذت", "لذت", "लज़्ज़त", "لذت", "pleasure_lazza", "Arabic", "Female",
            "Arabic root ل ذ ذ (l-dh-dh); لَذَّة (Ladhdha)", False, "high",
            "Lazzat is Arabic لَذَّة (Ladhdha) 'pleasure, delight, enjoyment', from the root ل ذ ذ (l-dh-dh); the form لَذَّت is the Persian/Urdu rendering. CRITICAL SOURCE ERROR: the source gave لزّات (a different form); the correct form is لَذَّة. The source gloss 'Taste, Delight' is broadly consistent."),
 "leah": ("ليا", "لیا", "لیا", "लिया", "لیا", "leah", "Arabic", "Female",
          "Arabic لِيَا (Liyā)", False, "low",
          "Leah is recorded at low confidence. The source gave ليا and glossed the name 'Weary, Delicate'; لِيَا (Liyā) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "leem": ("ليم", "لیم", "لیم", "लीम", "لیم", "leem", "Arabic", "Female",
          "Arabic لِيم (Līm)", False, "low",
          "Leem is recorded at low confidence. The source gave ليم and glossed the name 'A garden, oasis, or paradise'; لِيم (Līm) is a documented female given name, but the source gloss could not be confirmed. No confident meaning is asserted."),
 "leen": ("لين", "لین", "لین", "लीन", "لین", "softness", "Arabic", "Female",
          "Arabic root ل ي ن (l-y-n); لِين (Līn)", False, "high",
          "Leen is Arabic لِين (Līn) 'softness, tenderness, gentleness', from the root ل ي ن (l-y-n). The source gloss 'Light, Soft' is broadly consistent."),
 "leila": ("ليلى", "لیلیٰ", "لیلا", "लैला", "لیلی", "layla", "Arabic", "Female",
           "Arabic لَيْلَى (Laylā)", False, "high",
           "Leila is Arabic لَيْلَى (Laylā), a well-documented female given name. The source record was an 8-key stub with no data. Same name as laila, layla, laylaa and leyla."),
 "lema": ("لمى", "لمیٰ", "لمی", "लमा", "لمی", "lama", "Arabic", "Female",
          "Arabic لَمَى (Lamā)", False, "high",
          "Lema is Arabic لَمَى (Lamā), a documented female given name. CRITICAL SOURCE ERROR: the source gave لماء (a different form) and glossed the name 'Tongue, speech'; the correct form is لَمَى. Same name as lama."),
 "leyla": ("ليلى", "لیلیٰ", "لیلا", "लैला", "لیلی", "layla", "Arabic", "Female",
           "Arabic لَيْلَى (Laylā)", False, "high",
           "Leyla is Arabic لَيْلَى (Laylā), a well-documented female given name. The source gloss 'Night' is broadly consistent. Same name as laila, layla, laylaa and leila."),
 "liaqat": ("لياقة", "لیاقت", "لیاقت", "लियाक़त", "لیاقت", "fitness", "Arabic", "Male",
            "Arabic root ل ي ق (l-y-q); لِيَاقَة (Liyāqa)", False, "high",
            "Liaqat is Arabic لِيَاقَة (Liyāqa) 'fitness, competence, ability', from the root ل ي ق (l-y-q); the form لِيَاقَت is the Persian/Urdu rendering. The source gloss 'Struggle, Striving' is unsupported and has been replaced with the lexical sense. Same name as liaquat."),
 "liaquat": ("لياقة", "لیاقت", "لیاقت", "लियाक़त", "لیاقت", "fitness", "Arabic", "Male",
             "Arabic root ل ي ق (l-y-q); لِيَاقَة (Liyāqa)", False, "high",
             "Liaquat is Arabic لِيَاقَة (Liyāqa) 'fitness, competence, ability', from the root ل ي ق (l-y-q); the form لِيَاقَت is the Persian/Urdu rendering. The source gloss 'Helper, Supporter' is unsupported and has been replaced with the lexical sense. Same name as liaqat."),
 "liba": ("لبا", "لبا", "لبا", "लिबा", "لبا", "liba", "Arabic", "Female",
          "Arabic لِبَا (Libā)", False, "low",
          "Liba is recorded at low confidence. The source gave عائشة (a different name entirely) and glossed the name 'Light, Radiant'; لِبَا (Libā) is a documented female given name, but the source's Arabic column and gloss could not be confirmed. No confident meaning is asserted."),
 "liban": ("لبنان", "لبنان", "لبنان", "लेबनान", "لبنان", "lebanon", "Arabic", "Male",
           "Place name; لُبْنَان (Lubnān)", False, "medium",
           "Liban is Arabic لُبْنَان (Lubnān), the country name Lebanon, used as a given name. The source gloss 'Mount Lebanon' is broadly consistent. Recorded at medium confidence because the item is a place name."),
}
